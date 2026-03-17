import logging
from pathlib import Path

from schema_miner.config.llmRegistry import LLMRegistry
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.config.cliConfig import CLIConfig
from schema_miner.config.envConfig import EnvConfig
from schema_miner.prompts.ontology_grounding import prompt_template
from schema_miner.services.LLM_Inference.inference_runner import llm_inference
from schema_miner.services.schema_manager.schema_manager import SchemaManager
from schema_miner.utils.file_utils import load_json_input, save_json_file


def prompt_based_qudt_grounding(process_schema: dict | Path, save_schema: bool = False) -> dict | None:
    """
    Ground a process schema with QUDT (QuantityKind and Unit) ontology using a direct prompt-based approach.

    :param dict | Path process_schema: Path to the JSON process schema to be grounded.
    :param bool save_schema: Whether to save the grounded schema to disk.
    :returns dict | None: The modified (grounded) schema dictionary, or None if grounding fails.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"QUDT Ontology Grounding for a {ProcessConfig.Process_name} process schema")

    # Retrieve LLM inference class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(EnvConfig.LLM_MODEL)

    # Read the process schema
    logger.info("Reading the schema...")
    schema = load_json_input(process_schema)
    if not schema:
        raise ValueError('Unable to load JSON Schema for Prompt-based Ontology grounding')

    # Read the ontology structure
    logger.debug("Reading the Ontology Structure to be used by the LLM...")
    ontology = SchemaManager.get_schema("QUDT_quantity_schema.json")

    # Read an example
    logger.debug("Reading an example JSON schema with QUDT integration to be used by LLM...")
    qudt_example = SchemaManager.get_schema("QUDT_quantity_schema_example.json")

    # Grounding the Schema with the Ontology
    logger.info("Calling the completion API of the model...")
    var_dict = {
        "process_name": ProcessConfig.Process_name,
        "process_description": ProcessConfig.Process_description,
        "ontology_structure": ontology,
        "qudt_example": qudt_example,
        "process_schema": schema,
    }
    schema = llm_inference(llm_inference_class, EnvConfig.LLM_MODEL, prompt_template, var_dict, CLIConfig.RESULTS_PATH)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(CLIConfig.RESULTS_PATH, f"{EnvConfig.LLM_MODEL}.json", schema)
        if file_saved:
            logger.info(f"JSON schema saved at location: {CLIConfig.RESULTS_PATH}")

    # Return the ontology grounded process schema
    return schema
