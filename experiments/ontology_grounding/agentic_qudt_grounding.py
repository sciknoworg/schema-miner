import json
import logging
from pathlib import Path
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.ontology_grounding.agentic_qudt_grounding import agentic_qudt_grounding

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logger.info(f'\nLLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models')

    # Add process name and process description whose schema have to be extracted 
    ProcessConfig.Process_name = "Atomic Layer Deposition"
    ProcessConfig.Process_description = "An ALD process involves a series of controlled chemical reactions used to deposit thin films on a surface at an atomic level"

    # Large Language Model (LLM) to be used for Schema Extraction
    llm_model_name = 'gpt-4o'

    # Ground the schema with QUDT Ontology
    logger.info(f'\nPerforming LLM ({llm_model_name}) Inference to extract schema...')
    process_schema = Path('./results/Ideal Schema/Atomic-Layer-Deposition/experimental-ideal-schema.json')
    results_file_path = Path("./results/test/qudt-grounded/Atomic-Layer-Deposition/experimental-schema")
    schema = agentic_qudt_grounding(llm_model_name, process_schema, results_file_path, save_schema = True)

    # Display the final Process Schema
    logging.info(f'{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent = 2)}')