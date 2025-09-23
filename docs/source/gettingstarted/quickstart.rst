Quickstart
==========

This guide walks you through running schema miner pro: extracting a schema, refining it, and grounding it with QUDT.

Prerequisites
*************

- You have installed `schema-miner` and set up any required API keys (see :doc:`installation`).
- You have data prepared in the directory structure described below.

Step 1: Data Setup
******************

Before extraction, prepare your data directories. For example:

.. code-block:: python

    # Process Specification for Stage 1
    process_specification_filepath = '../data/stage-1/Atomic-Layer-Deposition/Experimental-Usecase'
    process_specification_filename = 'ALD-Process-Development.pdf'

    # Small curated corpus of scientific papers
    scientific_paper_stage2_dir = '../data/stage-2/Atomic-Layer-Deposition/research-papers/experimental-usecase'

    # Bigger corpus of scientific papers
    scientific_paper_stage3_dir = '../data/stage-3/Atomic-Layer-Deposition/research-papers/experimental_usecase'

Step 2: Process Configuration
*****************************

Initialize the process name and description whose schema has to be extracted:

.. code-block:: python

    from schema_miner.config.processConfig import ProcessConfig

    ProcessConfig.Process_name = "Atomic Layer Deposition"
    ProcessConfig.Process_description = "An ALD process involves a series of controlled chemical reactions used to deposit thin films on a surface at an atomic level"

Also make sure your LLM keys/config are set:

.. code-block:: python

    from schema_miner.config.envConfig import EnvConfig

    # OpenAI Keys
    EnvConfig.OPENAI_api_key = '<insert-your-openai-key>'
    EnvConfig.OPENAI_organization_id = '<insert-your-openi-organization-id>'

    # Ollama
    EnvConfig.OLLAMA_base_url = '<Ollama Base URL or empty if Ollama running locally>'

    # HuggingFace
    EnvConfig.HUGGINGFACE_access_token = '<Your huggingface access token>'

Step 3: Stage 1 - Initial Schema Mining
***************************************

An initial JSON schema can be generated based on the domain specification document and the preferred LLM. An example run is shown below:

.. code-block:: python

    import json
    import logging
    from pathlib import Path
    from schema_miner.pdf_text_extractor import pdf_text_extractor
    from schema_miner.schema_extractor.extract_schema import extract_schema_stage1

    # Choose LLM
    llm_model_name = 'gpt-4o'

    # Input process specification
    process_specification = pdf_text_extractor(process_specification_filepath, process_specification_filename, return_text = True)

    # Extract schema
    results_file_path = "./results/stage-1/Atomic-Layer-Deposition/experimental-schema"
    schema = extract_schema_stage1(llm_model_name, process_specification, results_file_path, save_schema = True)

Step 4: Stage 2 - Preliminary Schema Refinement
******************************************************************************

The schema from stage 1 can refined by the LLM iteratively by analyzing a curated set of research papers and incorporating expert feedback. An example run is show below:

.. code-block:: python

    from schema_miner.schema_extractor.extract_schema import extract_schema_stage2

    # Input Initial Schema, Expert Feedback and Scientific Literature
    schema = Path("./results/stage-1/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
    expert_review = Path("./data/stage-2/Atomic-Layer-Deposition/domain-expert-reviews/experimental-usecase/method-1/gpt-4o.txt")
    scientific_paper = pdf_text_extractor(scientific_paper_stage2_dir, '1 Groner et al.pdf', return_text = True)

    # Refine schema
    results_file_path = "./results/stage-2/Atomic-Layer-Deposition/experimental-schema"
    schema = extract_schema_stage2(llm_model_name, schema, expert_review, scientific_paper, results_file_path, save_schema = True)

Step 5: Stage 3 – Final Schema Refinement
*****************************************

The schema from stage 2 can be finalized by the LLM iteratively by a larger set of research papers and expert feedback. An example run is show below:

.. code-block:: python

    from schema_miner.schema_extractor.extract_schema import extract_schema_stage3

    # Input Schema, Expert Feedback and Scientific Literature
    schema = Path("./results/stage-2/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
    expert_review = Path("./data/stage-3/Atomic-Layer-Deposition/domain-expert-reviews/experimental-usecase/Experiment-1/1a/gpt-4o.txt")
    scientific_paper = pdf_text_extractor(scientific_paper_stage3_dir, '1-Mattinen et al.pdf', return_text = True)

    # Finalize schema
    results_file_path = "./results/stage-3/Atomic-Layer-Deposition/experimental-schema"
    schema = extract_schema_stage3(llm_model_name, schema, expert_review, scientific_paper, results_file_path, save_schema = True)

    # View Final Schema
    logging.info(f"{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent=2)}")

Step 6: Ontology Grounding with QUDT
************************************

Once a process schema is extracted, it can be semantically grounded using the `QUDT Ontologies <https://www.qudt.org/pages/HomePage.html>`_ (Quantities, Units, Dimensions, and Data Types).

The grounding workflow uses either LLM prompting or an agentic LLM approach to align schema fields with QUDT concepts. Following is an example of an agent based qudt grounding.

.. code-block:: python

    from schema_miner.ontology_grounding.agentic_qudt_grounding import agentic_qudt_grounding

    # Select LLM for grounding
    llm_model_name = 'gpt-4o'

    # Ground the schema with QUDT Ontology
    process_schema = Path('./results/Ideal Schema/Atomic-Layer-Deposition/experimental-ideal-schema.json')
    results_file_path = "./results/qudt-grounded/Atomic-Layer-Deposition/experimental-schema"
    schema = agentic_qudt_grounding(llm_model_name, process_schema, results_file_path, save_schema = True)

    # Display grounded schema
    logging.info(f'{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent = 2)}')

For a detailed description of each function and module, please refer to the :doc:`Package Reference <../packagereference/schema-extractor>`.
