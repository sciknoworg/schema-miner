import os
import sys
from utils.utils import read_json_file, read_text_file, write_text_file, save_json_file, extract_json_schema, read_yaml_file
from services.LLM_Inference.LLM_inference import LLM_Inference
from services.LLM_Inference.openai_llm_inference import Openai_LLM_Inference
from services.LLM_Inference.saia_llm_inference import SAIA_LLM_Inference
from services.LLM_Inference.ollama_llm_inference import OLLAMA_LLM_Inference
from services.LLM_Inference.huggingface_llm_inference import HuggingFace_LLM_Inference
from prompts.schema_extraction import prompt_template2

def llm_inference(llm_inference_obj: LLM_Inference, llm_model_name: str, result_path: str, initial_schema_path: str, expert_review_path: str, literature_path: str):
    """
    Performs the Inference on the given LLM model with the specified prompt template. The outputs from the model is then saved into a text file and the final schema into a json file.

    :param LLM_Inference llm_inference_obj: The Inference object used to query the specified LLM with the prompt template
    :param str llm_model_name: The name of the Large Language Model(LLM)
    :param str result_path: The file path to store the final json schema
    :param str initial_schema_path: The file path to extract the initial schema from stage-1
    :param str expert_review_path: The file path to extract the domain expert reviews about the initial schema
    :param str literature_path: The file path to read the scientific literature
    """
    #Initializing the object for LLM Inference
    llm = llm_inference_obj(llm_model_name)
    print(f'Using {llm}')

    #Formatting the model name with special characters
    llm_model_name = llm_model_name.replace(':', '-')
    llm_model_name = llm_model_name.replace('/', '-')

    #Reading the Process description
    process_config = read_yaml_file('src/config/process_config.yml')
    if not process_config:
        print('Cannot read process configuration, Stopping the inference from the LLM...')
        sys.exit(1)

    #Reading the schema from stage-1
    print(f'\nReading the schema from stage-1: {initial_schema_path}/{llm_model_name}.json')
    schema = read_json_file(f'{initial_schema_path}/{llm_model_name}.json')
    
    #Reading the domain expert reviews
    print(f'\nReading the domain expert review on the initial schema: {expert_review_path}/{llm_model_name}.txt')
    review = read_text_file(f'{expert_review_path}/{llm_model_name}.txt')

    #Initializing the counter
    index = 0

    #Iterating over the scientific literature
    for filename in os.listdir(literature_path):
        if not filename.endswith('.md'): continue

        print(f'\n========================== Iteration {index + 1} =================================')

        #Reading the full text of the scientific paper
        print(f'\nReading the scientific paper: {literature_path}/{filename}')
        full_text = read_text_file(f'{literature_path}/{filename}')

        #Extracting the schema from the LLM
        print('\nCalling the completion API of the model')
        var_dict = {'process_name': process_config['name'],
                    'stage2_objectives': process_config['stage2_objectives'],
                    'stage2_user_prompt_conditions': process_config['stage2_user_prompt_conditions'],
                    'current_schema': schema,
                    'full_text': full_text,
                    'domain_expert_review': review}
        model_output = llm.completion(prompt_template2, var_dict)

        #Returns None, if any exception occurrs during the LLM Inference
        if not model_output:
            print(f'No output from model: {llm_model_name}, continuing to the next paper..')
            continue
        
        #Saving the model response
        print(f'Writing the model\'s response to the file at the specified location: {result_path}')
        file_path = f'{result_path}/Intermediate-responses/{llm_model_name}/{llm_model_name}_{index + 1}.txt'
        write_text_file(file_path, model_output)
        
        #Extracting the updated schema
        updated_schema = extract_json_schema(model_output, json_encl_expr = [('```json', '```'), ('```', '```')])
        if not updated_schema:
            print('Unable to extract JSON, stopping the inference from the LLM...')
            break

        #Updating the previous schema with the current schema and clearing the expert review for next iteration
        schema = updated_schema
        index += 1
        # review = ''
        
        #Updating the domain-expert's feedback
        # print('\nDo you want to provide feedback?')
        # provide_feedback = input('Feedback (yes/no)> ')

        # review = ''
        # if provide_feedback.lower() == 'yes':
        #     print('\nPlease input your feedback')
        #     review = input('Feedback> ')
        
        # print('\nDo you want to continue with the next paper?')
        # cont = input('Continue (yes)/Stop (no)> ')
        # if cont.lower() == 'no':
        #     break
        
    #Saving the final json schema
    file_saved = save_json_file(result_path, f'{llm_model_name}.json', schema)
    if file_saved: print(f'JSON schema updated with LLM: {llm_model_name}')

if __name__ == "__main__":

    #Dictionary containing the class mapping for different LLM types
    llm_type_mappings = {
        'gpt-4o': Openai_LLM_Inference,
        'gpt-4-turbo': Openai_LLM_Inference,
        'meta-llama-3.1-8b-instruct': SAIA_LLM_Inference,
        'Qwen/Qwen2.5-0.5B-Instruct': HuggingFace_LLM_Inference
    }
    
    print('\nLLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models ')
    print('Stage 2: Preliminary Schema Refinement\n')
    
    print('Please specify the LLM name to perform schema mining...')
    print('''List of possible LLMs:
    1. OPENAI Models:
        - gpt-4o
        - gpt-4-turbo
    2. LLAMA Models:
        - meta-llama-3.1-8b-instruct
    3. HuggingFace Models:
        - Qwen/Qwen2.5-0.5B-Instruct
    4. Any other local OLLAMA Model
    ''')
    model_name = input('LLM> ')
    llm_inference_class = llm_type_mappings[model_name] if model_name in llm_type_mappings.keys() else OLLAMA_LLM_Inference

    print('\nPlease specify the location to the schema from stage 1')
    initial_schema_dir = input('Stage 1 - schema location> ')

    print('\nPlease specify the location to the domain-expert feedbacks on stage 1 schema')
    expert_review_dir = input('Expert feedback location> ')

    print('\nPlease specify the location to the small domain-expert curated collection of research papers')
    literature_dir = input('Research papers location> ')

    print('\nPlease specify the location to save the schema')
    results_dir = input('Schema location> ')

    print(f'\nPerforming LLM ({model_name}) Inference to extract updated experimental schema...')
    llm_inference(llm_inference_class, model_name, results_dir, initial_schema_dir, expert_review_dir, literature_dir)