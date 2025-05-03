import sys
from utils.utils import write_text_file, extract_json_schema, save_json_file, read_yaml_file, read_json_file
from services.LLM_Inference.LLM_inference import LLM_Inference
from services.LLM_Inference.openai_llm_inference import Openai_LLM_Inference
from services.LLM_Inference.saia_llm_inference import SAIA_LLM_Inference
from services.LLM_Inference.ollama_llm_inference import OLLAMA_LLM_Inference
from services.LLM_Inference.huggingface_llm_inference import HuggingFace_LLM_Inference
from prompts.ontology_grounding import prompt_template

def ground_ontology_to_schema(llm_inference_obj: LLM_Inference, llm_model_name: str, ontology_structure_path: str, process_schema_path: str, result_file_path: str, process_config_path: str):
    """
    Performs the Inference on the given LLM model with the specified prompt template. The output from the model is then saved into a text file.

    :param LLM_Inference llm_inference_obj: The Inference object used to query the specified LLM with the prompt template
    :param str llm_model_name: The name of the Large Language Model(LLM)
    :param str ontology_structure: The file path for ontology structure to embed inside the process schema
    :param str process_schema_path: The file path containing the final process schema
    :param str result_file_path: The file path to store the model's output
    :param str process_config_path: The file path containing details for the scientific process being used.
    :return str: Returns the Initial Schema
    """
    try:
        #Grounding the Schema with an ontology using LLM prompting
        llm = llm_inference_obj(llm_model_name)
        print(f'Using {llm}')

        #Reading the Process description
        process_config = read_yaml_file(process_config_path)
        if not process_config:
            print('Cannot read process configuration, Stopping the inference from the LLM...')
            sys.exit(1)

        #Reading the schema from stage-1
        print(f'\nReading the final process schema: {process_schema_path}')
        schema = read_json_file(f'{process_schema_path}')

        #Reading the ontology structure
        print(f'\nReading the Ontology Structure to be used by the LLM')
        ontology_structure = read_json_file(ontology_structure_path)

        #Grounding the Schema with the Ontology
        var_dict = {'process_name': process_config['name'],
                    'process_description': process_config['description'],
                    'ontology_structure': ontology_structure,
                    'process_schema': schema}
        model_output = llm.completion(prompt_template, var_dict)

        #Returns None, if any exception occurrs during the LLM Inference
        if not model_output:
            print(f'No Output from the Model: {llm_model_name}, terminating the workflow')
            return None
        
        #Formatting the model name with special characters
        llm_model_name = llm_model_name.replace(':', '-')
        llm_model_name = llm_model_name.replace('/', '-')

        #Saving the response
        print(f'\nWriting the model\'s response to the file at the specified location: {result_file_path}')
        file_path = f'{result_file_path}/{llm_model_name}.txt'
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
        print(f'Exception Occurred while grounding Schema with LLM ({llm_model_name}) Inference')
        print(f'Exception: {e}')

if __name__ == "__main__":

    #Process Config path
    process_config_path = 'src/config/process_config.yml'

    #Ontology Structure path
    ontology_structure_path = 'src/schemas/QUDT_quantity_schema.json'

    #Dictionary containing the class mapping for different LLM types
    llm_type_mappings = {
        'gpt-4o': Openai_LLM_Inference,
        'gpt-4-turbo': Openai_LLM_Inference,
        'meta-llama-3.1-8b-instruct': SAIA_LLM_Inference,
        'Qwen/Qwen2.5-0.5B-Instruct': HuggingFace_LLM_Inference
    }

    model_name = input('LLM> ')
    llm_inference_class = llm_type_mappings[model_name] if model_name in llm_type_mappings.keys() else OLLAMA_LLM_Inference

    print('\nPlease specify the location to the final schema')
    schema_dir = input('Final schema location> ')

    print('\nPlease specify the location to save the schema')
    results_dir = input('Schema location> ')

    print(f'\nPerforming LLM ({model_name}) Inference to extract schema...')
    ground_ontology_to_schema(llm_inference_class, model_name, ontology_structure_path, schema_dir, results_dir, process_config_path)