import logging
from pathlib import Path
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.services.LLM_Inference.inference_runner import llm_inference
from schema_miner.config.llmRegistry import LLMRegistry
from schema_miner.prompts.schema_extraction import prompt_template1, prompt_template2, prompt_template3
from schema_miner.utils.file_utils import save_json_file, load_text_input, load_json_input

def extract_schema_stage1(llm_model_name: str, process_specification: str | Path, result_file_path: str, save_schema: bool = False) -> dict | None:
    """
    Extract the initial process schema from a given process specification document using the specified Large Language Model (LLM).

    :param str llm_model_name: The name of the Large Language Model to use for extraction.
    :param str | Path process_specification: The process specification document, provided either as a file path or as a direct string containing the specification content.
    :param str result_file_path: The file path where the model's output will be stored.
    :param bool, optional save_schema: If True, save the extracted schema to the specified result file path. Defaults to False.
    :returns dict | None: A dictionary representing the extracted schema, or None if no schema could be extracted.
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.info(f'\nLLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models for {ProcessConfig.Process_name} process')
    logger.info('Stage 1: Initial Schema Mining\n')
    
    # Retrieve LLM inference class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(llm_model_name)

    # Read process specification document
    logger.info('Reading the process specification document...')
    context = load_text_input(process_specification)

    # Extract process schema using LLM and process specification document
    logger.info(f'\nPerforming LLM ({llm_model_name}) Inference to extract schema...')
    var_dict = {'process_name': ProcessConfig.Process_name, 'process_description': ProcessConfig.Process_description, 'context': context}
    schema = llm_inference(llm_inference_class, llm_model_name, prompt_template1, var_dict, result_file_path)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(result_file_path, f'{llm_model_name.replace(':', '-').replace('/', '-')}.json', schema)
        if file_saved: logger.info(f'JSON schema saved at location: {result_file_path}')

    # Return extracted JSON schema
    return schema

def extract_schema_stage2(llm_model_name: str, initial_schema: dict | Path, expert_review: str | Path, scientific_paper: str | Path, result_file_path: str, save_schema: bool = False) -> dict | None:
    """
    Refine the initial schema from Stage 1 using domain-expert feedback and scientific publications.

    :param str llm_model_name: The name of the Large Language Model to use for refinement.
    :param dict | Path initial_schema: The initial schema produced in Stage 1, provided either as a dictionary or as a file path to a serialized schema.
    :param str | Path expert_review: Domain-expert feedback on the initial schema, provided either as a direct string or as a file path to a text document.
    :param str | Path scientific_paper: Relevant scientific publication for schema refinement.
    :param str result_file_path: The file path where the refined schema will be stored.
    :param bool, optional save_schema: If True, save the refined schema to the specified result file path. Defaults to False.
    :returns dict | None: A dictionary representing the refined schema, or None if refinement was unsuccessful.
    """

    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.info(f'\nLLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models for {ProcessConfig.Process_name} process')
    logger.info('Stage 2: Preliminary Schema Refinement\n')

    # Retrieve LLM Inference Class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(llm_model_name)

    # Read the initial schema from stage-1
    logger.info(f'\nReading the schema from stage-1')
    schema = load_json_input(initial_schema)

    # Read the domain-expert reviews
    logger.info(f'\nReading the domain expert review on the initial schema')
    review = load_text_input(expert_review)

    # Read the scientific paper
    logger.info(f'\nReading the scientific paper')
    full_text = load_text_input(scientific_paper) 

    #Extract the updated schema from the LLM
    logger.info('\nCalling the completion API of the model')
    var_dict = {'process_name': ProcessConfig.Process_name, 'current_schema': schema, 'full_text': full_text, 'domain_expert_review': review}
        
    #Update the Schema using the LLM and a Scientific Paper as Input
    schema = llm_inference(llm_inference_class, llm_model_name, prompt_template2, var_dict, result_file_path)
    
    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(result_file_path, f'{llm_model_name.replace(':', '-').replace('/', '-')}.json', schema)
        if file_saved: logger.info(f'JSON schema updated with LLM: {llm_model_name}')

    #Returning the Updated Process Schema
    return schema

def extract_schema_stage3(llm_model_name: str, refined_schema: dict | Path, expert_review: str | Path, scientific_paper: str | Path, result_file_path: str, save_schema: bool = False) -> dict | None:
    """
    Finalize the Refined schema from Stage 2 using domain-expert feedback and scientific publications.

    :param str llm_model_name: The name of the Large Language Model to use for refinement.
    :param dict | Path refined_schema: The refined schema produced in Stage 2, provided either as a dictionary or as a file path to a serialized schema.
    :param str | Path expert_review: Domain-expert feedback on the initial schema, provided either as a direct string or as a file path to a text document.
    :param str | Path scientific_paper: Relevant scientific publication for schema refinement.
    :param str result_file_path: The file path where the refined schema will be stored.
    :param bool, optional save_schema: If True, save the refined schema to the specified result file path. Defaults to False.
    :returns dict | None: A dictionary representing the refined schema, or None if refinement was unsuccessful.
    """

    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.info(f'\nLLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models for {ProcessConfig.Process_name} process')
    logger.info('Stage 3: Finalize Schema Refinement\n')

    # Retrieve LLM Inference Class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(llm_model_name)

    # Read the initial schema from stage-1
    logger.info(f'\nReading the refined schema from stage-2')
    schema = load_json_input(refined_schema)

    # Read the domain-expert reviews
    logger.info(f'\nReading the domain expert review on the refined schema')
    review = load_text_input(expert_review)

    # Read the scientific paper
    logger.info(f'\nReading the scientific paper')
    full_text = load_text_input(scientific_paper) 

    #Extract the updated schema from the LLM
    logger.info('\nCalling the completion API of the model')
    var_dict = {'process_name': ProcessConfig.Process_name, 'current_schema': schema, 'full_text': full_text, 'domain_expert_review': review}
        
    #Update the Schema using the LLM and a Scientific Paper as Input
    schema = llm_inference(llm_inference_class, llm_model_name, prompt_template2, var_dict, result_file_path)
    
    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(result_file_path, f'{llm_model_name.replace(':', '-').replace('/', '-')}.json', schema)
        if file_saved: logger.info(f'JSON schema updated with LLM: {llm_model_name}')

    #Returning the Updated Process Schema
    return schema