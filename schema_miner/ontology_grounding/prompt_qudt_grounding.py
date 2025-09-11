import logging
from pathlib import Path
from schema_miner.config.llmRegistry import LLMRegistry
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.prompts.ontology_grounding import prompt_template
from schema_miner.utils.file_utils import load_json_input, save_json_file
from schema_miner.services.schema_manager.schema_manager import SchemaManager
from schema_miner.services.LLM_Inference.inference_runner import llm_inference

def prompt_based_qudt_grounding(llm_model_name: str, process_schema: dict | Path, result_file_path: str, save_schema: bool = False) -> dict | None:
    """
    Ground a process schema with QUDT (QuantityKind and Unit) ontology using a direct prompt-based approach.

    :param str llm_model_name: Name of the LLM model to use (e.g., "gpt-4o").
    :param dict | Path process_schema: Path to the JSON process schema to be grounded.
    :param str result_file_path: Directory path where the grounded schema will be saved if `save_schema` is True.
    :param bool save_schema: Whether to save the grounded schema to disk.
    :returns dict | None: The modified (grounded) schema dictionary, or None if grounding fails.
    """
    logger = logging.getLogger(__name__)
    logger.info(f'\nQUDT Ontology Grounding for a {ProcessConfig.Process_name} process schema')

    # Retrieve LLM inference class
    llm_inference_class = LLMRegistry.get_llm_Inference_cls(llm_model_name)

    # Read the process schema
    logger.info(f'\nReading the process schema')
    schema = load_json_input(process_schema)

    #Read the ontology structure
    logger.info(f'\nReading the Ontology Structure to be used by the LLM')
    ontology = SchemaManager.get_schema('QUDT_quantity_schema.json')

    # Read an example
    logger.info(f'\nReading an example JSON schema with QUDT integration to be used by LLM')
    qudt_example = SchemaManager.get_schema('QUDT_quantity_schema_example.json')

    #Grounding the Schema with the Ontology
    logger.info('\nCalling the completion API of the model')
    var_dict = {'process_name': ProcessConfig.Process_name, 'process_description': ProcessConfig.Process_description, 'ontology_structure': ontology, 'qudt_example': qudt_example, 'process_schema': schema}
    schema = llm_inference(llm_inference_class, llm_model_name, prompt_template, var_dict, result_file_path)

    # Optionally save extracted schema on disk
    if save_schema:
        file_saved = save_json_file(result_file_path, f'{llm_model_name}.json', schema)
        if file_saved: logger.info(f'JSON schema saved at location: {result_file_path}')

    # Return the ontology grounded process schema
    return schema