import copy
import json
import logging
from pathlib import Path

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.schema import Document
from langchain.text_splitter import TokenTextSplitter
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from schema_miner.config.envConfig import EnvConfig
from schema_miner.config.llmRegistry import LLMRegistry
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.prompts.ontology_grounding import agent_qudt_prompt1, agent_qudt_prompt2
from schema_miner.services.LLM_Inference.openai_llm_inference import Openai_LLM_Inference
from schema_miner.services.ontology.ontology_manager import OntologyManager
from schema_miner.services.schema_manager.schema_manager import SchemaManager
from schema_miner.utils.dictionary_utils import get_schema_leaf_keys
from schema_miner.utils.file_utils import load_json_input, save_json_file


def _chunk_text(text: str, chunk_size: int = 300, chunk_overlap: int = 30) -> list[str]:
    """
    Chunk a given text based on the provided chunk size.

    :param str text: The text which has to be chunked
    :param int chunk_size: The Chunk Size
    :param int chunk_overlap: The overlap characters between two chunks
    :returns list[str] chunked_text: A list of of given text chunks
    """
    splitter = TokenTextSplitter(
        model_name="text-embedding-3-small",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)


def _create_FAISS_index(text_chunks: list[str]) -> FAISS:
    """
    Create a FAISS vector store from the text chunks and embeddings

    :params list[str] text_chunks: A list of text chunks
    :returns FAISS: VectorStore initialized from documents and embeddings.
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    docs = [Document(page_content=chunk) for chunk in text_chunks]
    return FAISS.from_documents(docs, embeddings)


def _search_semantic(query: str, vectorStore: FAISS, k: int = 3) -> str:
    """
    Returns the Chunks which matches semantically with the provided user query.

    :params str query: The user query to search within chunks
    :params int k: Number of chunks to return
    :returns str: Concatenated text from matched documents
    """
    docs = vectorStore.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in docs])


def _load_qudt_ontology(url: str, return_vecStore: bool = True) -> str | FAISS:
    """
    Load and Reads the Ontology file from the provided URL and return its FAISS vector store

    :params str url: The URL containing the Ontology text in turtle format
    :param bool return_vecStore: If True, returns the FAISS vector store. Else ontology text
    :returns str | FAISS: The ontology
    """
    ontology = OntologyManager(url).get()
    if not return_vecStore:
        return ontology
    ontology_chunks = _chunk_text(ontology)
    return _create_FAISS_index(ontology_chunks)


def _inject_quantity_schema(schema: dict, key_path: list[str], ontology_template: dict, agent_response: dict) -> None:
    """
    Injects a QUDT-grounded quantity schema into a given process schema at the location specified by the key path.

    :param dict schema: The JSON schema into which the ontology should be injected.
    :param list[str] key_path: A list of keys representing the path to the target property inside the schema.
    :param dict ontology_template: A template dictionary that contains the ontology structure to inject.
    :param dict agent_response: A dictionary containing the results from the grounding agent.
    """
    # Traverse the schema until the leaf node defined by key_path
    target = schema["properties"]
    for key in key_path:
        target = target[key]["properties"] if "properties" in target[key] else target[key]

    # Update ontology template with agent-provided grounding information
    ontology_unit = ontology_template["quantityValue"]["properties"]["unit"]["properties"]["hasQuantityKind"]
    ontology_unit["enum"] = agent_response.get("quantityKind", [])
    ontology_unit["sameAs"] = agent_response.get("unit", [])
    ontology_template["quantityKind"]["enum"] = agent_response.get("quantityKind", [])

    # Inject enriched ontology schema at the leaf node
    target["type"] = "object"
    target["properties"] = copy.deepcopy(ontology_template)


def agentic_qudt_grounding(llm_model_name: str, process_schema: dict | Path, result_file_path: str, save_schema: bool = False) -> dict | None:
    """
    Ground a process schema with QUDT (QuantityKind and Unit) ontology using an agentic workflow powered by an LLM.

    :param str llm_model_name: Name of the LLM model to use (e.g., "gpt-4o").
    :param dict | Path process_schema: Path to the JSON process schema to be grounded.
    :param str result_file_path: Directory path where the grounded schema will be saved if `save_schema` is True.
    :param bool save_schema: Whether to save the grounded schema to disk.
    :returns dict | None: The modified (grounded) schema dictionary, or None if grounding fails.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"\nQUDT Ontology Grounding for a {ProcessConfig.Process_name} process schema Using Agentic Workflow")

    # Check for OpenAI Model
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(llm_model_name)
    if llm_inference_class is not Openai_LLM_Inference:
        raise ValueError("Only OpenAI models are applicable for Agent-based Ontology grounding\n")

    # Check for OpenAI Key
    EnvConfig.validate_openai_api_key()

    # Read the QUDT Ontology (QuantityKind and Units)
    logger.info("\nReading the QUDT Ontology (QuantityKind and Units) and creating their respective vector stores")
    qudt_quantityKind_vecStore = _load_qudt_ontology("https://qudt.org/3.1.0/vocab/quantitykind")
    qudt_units_vecStore = _load_qudt_ontology("https://qudt.org/3.1.0/vocab/unit")

    # Read the process schema
    logger.info("\nReading the process schema")
    schema = load_json_input(process_schema)
    if not schema:
        raise ValueError('Unable to load JSON Schema for Agent-based Ontology grounding\n')

    # Read the ontology template
    logger.info("\nReading the Ontology Structure to be used by the LLM")
    ontology = SchemaManager.get_schema("QUDT_quantity_schema.json")

    @tool
    def ground_qudt_entity(query: str):
        """
        Given a user query, return relevant QUDT classes/properties.

        :params str query: The query containing the property with its description to be grounded by QUDT ontology
        :returns str model_output: The LLMs output containing the relevant entity for the given query
        """
        # Find the relevant ontology chunks for the given query
        relevantQuantityKind = _search_semantic(query, qudt_quantityKind_vecStore)
        relevantQudtUnits = _search_semantic(query, qudt_units_vecStore)

        # Intialize the OpenAI Inference object
        llm = Openai_LLM_Inference(llm_model_name, temperature=0)

        # Extract the QUDT entities
        var_dict = {
            "quantityKind": relevantQuantityKind,
            "units": relevantQudtUnits,
            "process_name": ProcessConfig.Process_name,
            "process_description": ProcessConfig.Process_description,
            "query": query
        }
        model_output = llm.completion(agent_qudt_prompt1, var_dict)

        # Return the LLMs output
        return model_output

    # Format the Prompt
    prompt = ChatPromptTemplate.from_messages(
        [("system", agent_qudt_prompt2.system_prompt), MessagesPlaceholder("chat_history", optional=True),
         ("human", agent_qudt_prompt2.user_prompt), MessagesPlaceholder("agent_scratchpad")])

    # Create an OpenAI Tool Agent
    llm = ChatOpenAI(
        model=llm_model_name,
        temperature=0,
        model_kwargs={"response_format": {"type": "json_object"}}
    )
    agent = create_openai_tools_agent(llm=llm, tools=[ground_qudt_entity], prompt=prompt)

    # Intialize the agent executer with LLM and tools
    agent_executor = AgentExecutor(agent=agent, tools=[ground_qudt_entity], verbose=False)

    # Extract properties and its description
    schema_properties_desc = get_schema_leaf_keys(schema["properties"])

    # Execute the agent for each key representing a physical quantity
    for key_path, description in schema_properties_desc:
        # Query agent with schema property
        agent_response = agent_executor.invoke({"query": f"{' - '.join(s or "" for s in (key_path, description))}"})
        agent_response = json.loads(agent_response["output"])

        # Skip if grounding is invalid
        if not agent_response["valid"]:
            continue

        # Inject ontology into schema
        _inject_quantity_schema(schema, key_path.split(" "), ontology["properties"], agent_response)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(result_file_path, f"{llm_model_name}.json", schema)
        if file_saved:
            logger.info(f"JSON schema saved at location: {result_file_path}")

    # Return the grounded schema
    return schema
