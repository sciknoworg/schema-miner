import json
import logging
from pathlib import Path

from schema_miner.config.processConfig import ProcessConfig
from schema_miner.config.envConfig import EnvConfig
from schema_miner.ontology_grounding.prompt_qudt_grounding import prompt_based_qudt_grounding

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logger.info("LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models")

    # Ground the schema with QUDT Ontology
    logger.info(f"Performing LLM ({EnvConfig.LLM_MODEL}) Inference to extract schema...")
    process_schema = Path("../results/stage-3/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
    schema = prompt_based_qudt_grounding(process_schema, save_schema=True)

    # Display the final Process Schema
    logging.info(f"{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent = 2)}")
