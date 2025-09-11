import json
import logging
from pathlib import Path
from schema_miner.config.processConfig import ProcessConfig
from schema_miner.pdf_text_extractor import pdf_text_extractor
from schema_miner.schema_extractor.extract_schema import extract_schema_stage1, extract_schema_stage2, extract_schema_stage3

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":

    # Add process name and process description whose schema have to be extracted 
    ProcessConfig.Process_name = "Atomic Layer Deposition"
    ProcessConfig.Process_description = "An ALD process involves a series of controlled chemical reactions used to deposit thin films on a surface at an atomic level"

    # Large Language Model (LLM) to be used for Schema Extraction
    llm_model_name = 'gpt-4o'

    # LLMs4SchemaDiscovery - Stage 1 - Initial Schema Mining
    results_file_path = Path("./results/test/stage-1/Atomic-Layer-Deposition/experimental-schema")
    process_specification_filepath = './data/stage-1/Atomic-Layer-Deposition/Experimental-Usecase'
    process_specification_filename = 'ALD-Process-Development.pdf'
    process_specification = pdf_text_extractor(process_specification_filepath, process_specification_filename, return_text = True)
    schema = extract_schema_stage1(llm_model_name, process_specification, results_file_path, save_schema = True)

    # LLMs4SchemaDiscovery - Stage 2 - Preliminary Schema Refinement
    schema = Path("./results/test/stage-1/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
    expert_review = Path("./data/stage-2/Atomic-Layer-Deposition/domain-expert-reviews/experimental-usecase/method-1/gpt-4o.txt")
    results_file_path = Path("./results/test/stage-2/Atomic-Layer-Deposition/experimental-schema")
    scientific_paper = pdf_text_extractor('./data/stage-2/Atomic-Layer-Deposition/research-papers/experimental-usecase', '1 Groner et al.pdf', return_text = True)
    schema = extract_schema_stage2(llm_model_name, schema, expert_review, scientific_paper, results_file_path, save_schema = True)
    
    # LLMs4SchemaDiscovery - Stage 3 - Finalize Schema Refinement
    schema = Path("./results/test/stage-2/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
    expert_review = Path("./data/stage-3/Atomic-Layer-Deposition/domain-expert-reviews/experimental-usecase/Experiment-1/1a/gpt-4o.txt")
    results_file_path = Path("./results/test/stage-3/Atomic-Layer-Deposition/experimental-schema")
    scientific_paper = pdf_text_extractor('./data/stage-3/Atomic-Layer-Deposition/research-papers/experimental_usecase', '1-Mattinen et al.pdf', return_text = True)
    schema = extract_schema_stage3(llm_model_name, schema, expert_review, scientific_paper, results_file_path, save_schema = True)

    # Print the final Process Schema
    logging.info(f'{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent = 2)}')