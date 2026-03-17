import logging
from pathlib import Path

from schema_miner.config.llmRegistry import LLMRegistry
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.config.cliConfig import CLIConfig
from schema_miner.config.envConfig import EnvConfig
from schema_miner.prompts.schema_extraction import prompt_template1, prompt_template2
from schema_miner.services.LLM_Inference.inference_runner import llm_inference
from schema_miner.utils.file_utils import load_json_input, load_text_input, save_json_file


def extract_schema_stage1(save_schema: bool = False) -> dict | None:
    """
    Extract the initial process schema from a given process specification document using the specified Large Language Model (LLM).

    :param bool, optional save_schema: If True, save the extracted schema to the specified result file path. Defaults to False.
    :returns dict | None: A dictionary representing the extracted schema, or None if no schema could be extracted.
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.info(
        f"LLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models for {ProcessConfig.Process_name} process"
    )
    logger.info("Stage 1: Initial Schema Mining")

    # Retrieve LLM inference class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(EnvConfig.LLM_MODEL)

    # Read process specification document
    logger.info("Reading the process specification document...")
    context = load_text_input(CLIConfig.STAGE1_SPECIFICATION_PATH)

    # Extract process schema using LLM and process specification document
    logger.info(f"Performing LLM ({EnvConfig.LLM_MODEL}) Inference to extract schema...")
    var_dict = {
        "process_name": ProcessConfig.Process_name,
        "process_description": ProcessConfig.Process_description,
        "context": context,
    }
    schema = llm_inference(llm_inference_class, EnvConfig.LLM_MODEL, prompt_template1, var_dict, CLIConfig.RESULTS_PATH)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(CLIConfig.RESULTS_PATH, f"{EnvConfig.LLM_MODEL.replace(':', '-').replace('/', '-')}.json", schema)
        if file_saved:
            logger.info(f"JSON schema saved at location: {CLIConfig.RESULTS_PATH}")

    # Return extracted JSON schema
    return schema


def extract_schema_stage2(initial_schema: dict | Path, expert_review: str | Path, scientific_paper: str | Path, save_schema: bool = False) -> dict | None:
    """
    Refine the initial schema from Stage 1 using domain-expert feedback and scientific publications.

    :param dict | Path initial_schema: The initial schema produced in Stage 1, provided either as a dictionary or as a file path to a serialized schema.
    :param str | Path expert_review: Domain-expert feedback on the initial schema, provided either as a direct string or as a file path to a text document.
    :param str | Path scientific_paper: Relevant scientific publication for schema refinement.
    :param bool, optional save_schema: If True, save the refined schema to the specified result file path. Defaults to False.
    :returns dict | None: A dictionary representing the refined schema, or None if refinement was unsuccessful.
    """

    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.info(
        f"LLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models for {ProcessConfig.Process_name} process"
    )
    logger.info("Stage 2: Preliminary Schema Refinement")

    # Retrieve LLM Inference Class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(EnvConfig.LLM_MODEL)

    # Read the initial schema from stage-1
    logger.info("Reading the schema...")
    schema = load_json_input(initial_schema)

    # Read the domain-expert reviews
    review = ""
    if expert_review:
        logger.info("Reading the domain expert review on the schema...")
        review = load_text_input(expert_review)

    # Read the scientific paper
    logger.info("Reading the scientific paper...")
    full_text = load_text_input(scientific_paper)

    # Extract the updated schema from the LLM
    logger.info("Calling the completion API of the model...")
    var_dict = {
        "process_name": ProcessConfig.Process_name,
        "current_schema": schema,
        "full_text": full_text,
        "domain_expert_review": review,
    }

    # Update the Schema using the LLM and a Scientific Paper as Input
    schema = llm_inference(llm_inference_class, EnvConfig.LLM_MODEL, prompt_template2, var_dict, CLIConfig.RESULTS_PATH)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(CLIConfig.RESULTS_PATH, f"{EnvConfig.LLM_MODEL.replace(':', '-').replace('/', '-')}.json", schema)
        if file_saved:
            logger.info(f"JSON schema updated with LLM: {EnvConfig.LLM_MODEL}")

    # Returning the Updated Process Schema
    return schema


def extract_schema_stage3(refined_schema: dict | Path, expert_review: str | Path, scientific_paper: str | Path, save_schema: bool = False) -> dict | None:
    """
    Finalize the Refined schema from Stage 2 using domain-expert feedback and scientific publications.

    :param dict | Path refined_schema: The refined schema produced in Stage 2, provided either as a dictionary or as a file path to a serialized schema.
    :param str | Path expert_review: Domain-expert feedback on the initial schema, provided either as a direct string or as a file path to a text document.
    :param str | Path scientific_paper: Relevant scientific publication for schema refinement.
    :param bool, optional save_schema: If True, save the refined schema to the specified result file path. Defaults to False.
    :returns dict | None: A dictionary representing the refined schema, or None if refinement was unsuccessful.
    """

    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.info(
        f"LLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models for {ProcessConfig.Process_name} process"
    )
    logger.info("Stage 3: Finalize Schema Refinement")

    # Retrieve LLM Inference Class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(EnvConfig.LLM_MODEL)

    # Read the initial schema from stage-1
    logger.info("Reading the schema...")
    schema = load_json_input(refined_schema)

    # Read the domain-expert reviews
    review = ""
    if expert_review:
        logger.info("Reading the domain expert review on the schema...")
        review = load_text_input(expert_review)

    # Read the scientific paper
    logger.info("Reading the scientific paper...")
    full_text = load_text_input(scientific_paper)

    # Extract the updated schema from the LLM
    logger.info("Calling the completion API of the model...")
    var_dict = {
        "process_name": ProcessConfig.Process_name,
        "current_schema": schema,
        "full_text": full_text,
        "domain_expert_review": review,
    }

    # Update the Schema using the LLM and a Scientific Paper as Input
    schema = llm_inference(llm_inference_class, EnvConfig.LLM_MODEL, prompt_template2, var_dict, CLIConfig.RESULTS_PATH)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(CLIConfig.RESULTS_PATH, f"{EnvConfig.LLM_MODEL.replace(':', '-').replace('/', '-')}.json", schema)
        if file_saved:
            logger.info(f"JSON schema updated with LLM: {EnvConfig.LLM_MODEL}")

    # Returning the Updated Process Schema
    return schema
