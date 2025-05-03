import json
from utils.utils import read_yaml_file

from langchain.agents import Tool, create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool

from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from services.LLM_Inference.openai_llm_inference import Openai_LLM_Inference
from services.ontology_parsers.ontology_parser import Ontology_Parser
from prompts.ontology_grounding import agent_qudt_prompt1, agent_qudt_prompt2

def chunk_text(text: str, chunk_size: int = 40000, chunk_overlap: int = 100):
    """
    Chunk a given the text based on the provided chunk size.

    :param str text: The text which has to be chunked
    :param int chunk_size: The Chunk Size
    :param int chunk_overlap: The overlap characters between two chunks
    :returns list[str] chunked_text: A list of of given text chunks
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        length_function = len,
        separators = ['\n\n', '\n', '.', ' ']
    )
    return splitter.split_text(text)

def create_FAISS_index(text_chunks: list[str]):
    """
    Create a FAISS vector store from the text chunks and embeddings

    :params list[str] text_chunks: A list of text chunks
    :returns VectorStore: VectorStore initialized from documents and embeddings.
    """
    embeddings = OpenAIEmbeddings()
    docs = [Document(page_content = chunk) for chunk in text_chunks]
    return FAISS.from_documents(docs, embeddings)

def search_semantic(query: str, vectorStore: FAISS, k: int = 3):
    """
    Returns the Chunks which matches semantically with the provided user query.

    :params str query: The user query to search within chunks
    :params int k: Number of chunks to return
    :returns str: Concatenated text from matched documents
    """
    docs = vectorStore.similarity_search(query, k = k)
    return '\n'.join([doc.page_content for doc in docs])

def load_qudt_ontology(url: str):
    """
    Load and Reads the Ontology file from the provided URL and return it as a text

    :params str url: The URL containing the Ontology text in turtle format
    :returns str text: The ontology text
    """
    qudt = Ontology_Parser()
    qudt.load(url)
    return qudt.ontology_text

@tool
def ground_qudt_entity(query: str):
    """
    Given a user query, return relevant QUDT classes/properties.

    :params str query: The query containing the property with its description to be grounded by QUDT ontology
    :returns str model_output: The LLMs output containing the relevant entity for the given query
    """
    #Finding the relevant ontology chunks for the given query
    relevantQuantityKind = search_semantic(query, qudt_quantityKind_vecStore)
    relevantQudtUnits = search_semantic(query, qudt_units_vecStore)

    #Reading the Process description
    process_config = read_yaml_file('src/config/process_config.yml')

    #Intializing the OpenAI Inference object
    llm = Openai_LLM_Inference('gpt-4o', temperature = 0)
    
    #Extracting the QUDT entities
    var_dict = {'quantityKind': relevantQuantityKind,
                'units': relevantQudtUnits,
                'process_name': process_config['name'],
                'process_description': process_config['description'],
                'query': query}
    model_output = llm.completion(agent_qudt_prompt1, var_dict)

    #Returning the LLMs output
    return model_output

def call_agent(model_name: str, tools: list, query: str):
    """
    Create an OpenAI Agent with the provided tools to ground the user query with the QUDT ontology.

    :params str model_name: The LLM to be used as an Agent
    :params list tools: A list of tools (functions) to be used by the Agent
    :params str query: The user query to be grounded with the QUDT Ontology
    :returns dict agent_response: A dictionary containing QUDT concepts for the provided user query
    """
    #Formatting the Prompt
    prompt = ChatPromptTemplate.from_messages([
        ('system', agent_qudt_prompt2.system_prompt), MessagesPlaceholder("chat_history", optional=True),
        ('human', agent_qudt_prompt2.user_prompt), MessagesPlaceholder("agent_scratchpad")
    ])

    #Creating an OpenAI Tool Agent
    llm = ChatOpenAI(model = model_name, temperature = 0, model_kwargs={'response_format': {'type': 'json_object'}})
    agent = create_openai_tools_agent(llm = llm, tools = tools, prompt = prompt)

    #Executing the agent with the user query
    agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)
    agent_response = agent_executor.invoke({'query': query})
    
    #Returning the agent's response
    return json.loads(agent_response['output'])

#Loading and chunking the QUDT QuantityKind Ontology
qudt_quantityKind = load_qudt_ontology('https://qudt.org/3.1.0/vocab/quantitykind')
qudt_quantityKind_chunks = chunk_text(qudt_quantityKind)
qudt_quantityKind_vecStore = create_FAISS_index(qudt_quantityKind_chunks)

#Loading and chunking the QUDT Units Ontology
qudt_units = load_qudt_ontology('https://qudt.org/3.1.0/vocab/unit')
qudt_units_chunks = chunk_text(qudt_units)
qudt_units_vecStore = create_FAISS_index(qudt_units_chunks)

if __name__ == "__main__":
    
    qudt_concepts = call_agent(model_name='gpt-4o', tools = [ground_qudt_entity], query = 'EtchedMaterialProperties MaterialProperties Crystallinity - Crystallinity of the etched material.')
    print(qudt_concepts)