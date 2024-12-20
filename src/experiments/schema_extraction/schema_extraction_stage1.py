from utils.utils import write_text_file, read_text_file, extract_json_schema, save_json_file
from services.LLM_inference import LLM_Inference
from services.openai_llm_inference import Openai_LLM_Inference
from services.saia_llm_inference import SAIA_LLM_Inference
from services.ollama_llm_inference import OLLAMA_LLM_Inference
from prompts import prompt_template1

def llm_inference(llm_inference_obj: LLM_Inference, llm_model_name: str, var_dict: dict, result_file_path: str):
    """
    Performs the Inference on the given LLM model with the specified prompt template. The output from the model is then saved into a text file.

    :param LLM_Inference llm_inference_obj: The Inference object used to query the specified LLM with the prompt template
    :param str llm_model_name: The name of the Large Language Model(LLM)
    :param dict var_dict: A dictionary containing the variables for formatting the prompt template
    :param str result_file_path: The file path to store the model's output
    :return str: Returns the Initial Schema
    """
    try:
        #Extracting the data schema from the LLM
        llm = llm_inference_obj(llm_model_name)
        print(f'Using {llm}')
        model_output = llm.completion(prompt_template1, var_dict)

        #Returns None, if any exception occurrs during the LLM Inference
        if not model_output:
            print(f'No Output from the Model: {llm_model_name}, terminating the workflow')
            return None

        #Saving the model response
        print(f'\nWriting the model\'s response to the file at the specified location: {result_file_path}')
        file_path = f'{result_file_path}/{model_name}.txt'
        write_text_file(file_path, model_output)

        #Extracting the updated schema
        print('\nExtracting the JSON object from the model\'s output...')
        initial_schema = extract_json_schema(model_output, json_encl_expr = [('```json', '```'), ('```', '```')])
        if not initial_schema:
            print('Stopping the inference from the LLM...')
            return None
        
        #Saving the final json schema
        file_saved = save_json_file(result_file_path, f'{llm_model_name}.json', initial_schema)
        if file_saved: print(f'JSON schema Saved at location: {result_file_path}')
    except Exception as e:
        print(f'Exception Occurred while doing LLM ({llm_model_name}) Inference')
        print(f'Exception: {e}')

if __name__ == "__main__":

    #Dictionary containing the class mapping for different LLM types
    llm_type_mappings = {
        'gpt-4o': Openai_LLM_Inference,
        'gpt-4-turbo': Openai_LLM_Inference,
        'meta-llama-3.1-8b-instruct': SAIA_LLM_Inference
    }
    
    print('\nLLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models')
    print('Stage 1: Initial Schema Mining\n')
    
    print('Please specify the LLM name to perform schema mining...')
    print('''List of possible LLMs:
    1. OPENAI Models:
        - gpt-4o
        - gpt-4-turbo
    2. LLAMA Models:
        - meta-llama-3.1-8b-instruct
    3. Any other local OLLAMA Model
    ''')
    model_name = input('LLM> ').lower()
    llm_inference_class = llm_type_mappings[model_name] if model_name in llm_type_mappings.keys() else OLLAMA_LLM_Inference

    print('\nPlease specify the location of the process specification document')
    context_location = input('Document location> ')
    context = read_text_file(context_location)

    print('\nPlease specify the location to save the schema')
    results_dir = input('Schema location> ')

    print(f'\nPerforming LLM ({model_name}) Inference to extract schema...')
    var_dict = {'context': context}
    llm_inference(llm_inference_class, model_name, var_dict, results_dir)