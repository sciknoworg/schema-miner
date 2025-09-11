import logging
from typing import Any
from schema_miner.utils.file_utils import write_text_file
from schema_miner.utils.json_utils import extract_json_schema
from schema_miner.services.LLM_Inference.LLM_inference import LLM_Inference

def llm_inference(llm_inference_obj: LLM_Inference, llm_model_name: str, prompt_template: Any, var_dict: dict, result_file_path: str) -> dict | None:
    """
    Performs the Inference on the given LLM model with the specified prompt template. The output from the model is then saved into a text file.

    :param LLM_Inference llm_inference_obj: The Inference object used to query the specified LLM with the prompt template
    :param str llm_model_name: The name of the Large Language Model(LLM)
    :param Any prompt_template: The prompt template with System and User prompts for the LLM Inference
    :param dict var_dict: A dictionary containing the variables for formatting the prompt template
    :param str result_file_path: The file path to store the model's output
    :return str: Returns the Initial Schema
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    
    try:
        #Extracting the data schema from the LLM
        llm = llm_inference_obj(llm_model_name)
        logger.debug(f'Using {llm}')

        #Returns None, if any exception occurrs during the LLM Inference
        model_output = llm.completion(prompt_template, var_dict)
        if not model_output:
            logger.debug(f'No Output from the Model: {llm_model_name}, terminating the workflow')
            return None
        
        #Formatting the model name with special characters
        llm_model_name = llm_model_name.replace(':', '-')
        llm_model_name = llm_model_name.replace('/', '-')

        #Saving the model response
        file_path = f'{result_file_path}/Intermediate-Responses/{llm_model_name}.txt'
        logger.debug(f'\nWriting the model\'s response to the file at the specified location: {file_path}')
        write_text_file(file_path, model_output)

        #Extracting the updated schema
        logger.debug('\nExtracting the JSON object from the model\'s output...')
        schema = extract_json_schema(model_output, json_encl_expr = [('```json', '```'), ('```', '```')])
        if not schema:
            logger.debug('Stopping the inference from the LLM...')
            return None
        
        #Returing the extracted JSON Schema
        return schema
    except Exception as e:
        logger.exception(f'Exception Occurred while doing LLM ({llm_model_name}) Inference')
        logger.exception(f'Exception: {e}')
        return None