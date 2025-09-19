<p align="center">
<img width="450" src="assets/schema-miner-pro-logo.jpg" alt="schema miner pro logo" />
</p>

<div align="center">

[![PyPI - Version](https://img.shields.io/pypi/v/schema-miner)](https://pypi.org/project/schema-miner/)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/schema-miner)](https://pepy.tech/projects/schema-miner)
[![Maintained Yes](https://img.shields.io/badge/maintained-yes-green)](https://github.com/sciknoworg/schema-miner/blob/main/MAINTENANCE.md)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![MIT License](https://img.shields.io/github/license/sciknoworg/schema-miner)](LICENSE)
[![DOI](https://zenodo.org/badge/900734076.svg)](https://doi.org/10.5281/zenodo.14781824)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](https://schema-miner.readthedocs.io/en/latest/)

</div>

<h3 align="center">SCHEMA-MINER<sup>pro</sup>: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow</h3>

This is an open-source implementation of Schema-Miner<sup>pro</sup>.

## 📋 Schema-miner<sup>pro</sup> Overview

Schema-Miner is a novel framework that leverages Large Language Models (LLMs) and continuous human feedback to automate and enhance the schema mining task. Through an iterative process, the framework uses LLMs to extract and organize properties from unstructured text and refines schemas with expert input. Schema-Miner<sup>pro</sup> extends Schema-Miner with an ontology grounding component powered by agentic AI. It performs multi-step reasoning using lexical heuristics and semantic similarity search, and grounds schema elements in formal ontologies (e.g., QUDT). Comprehensive documentation for Schema-Miner Pro, including detailed guides and examples, is available at [schema-miner.readthedocs.io](https://schema-miner.readthedocs.io/en/latest/).

<p align="center">
  <img src="https://raw.githubusercontent.com/sciknoworg/schema-miner/refs/heads/main/assets/LLM4SchemaMining%20-%20Workflow%20design.svg" height="300">
</p>

<p align="center">
  Figure 1: Overview of the LLMs4SchemaDiscovery workflow.
</p>

## ⚙️ System Requirements

The computational requirements for running this project vary depending on the model being used. If utilizing OpenAI models such as [**GPT-4o**](https://platform.openai.com/docs/models#gpt-4o) and [**GPT-4-turbo**](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), no specialized hardware is needed since inference is performed via API calls. A basic system with a stable internet connection is sufficient for executing API-based workflow.

For users opting to run **open-source models** such as [**Llama 3.1 8B**](https://ai.meta.com/blog/meta-llama-3-1/) or other large-scale transformer-based models, local execution demands significantly higher computational resources. While these models can be executed on a CPU, inference times will be considerably longer. However, for efficient execution, a dedicated GPU with VRAM (specified by the model's documentation) is strongly recommended.

While the hardware configuration can be adjusted based on the model size and performance needs, using a GPU significantly accelerates inference processes, reducing execution time drastically compared to CPU-only setups.

### Experimental Configuration

For our experiments, we used the following hardware setup:

* **Processor:** 16-core CPU
* **Memory:** 32 GB RAM
* **GPU:** Intel Arc Graphics
* **Models Used:**
    * **Cloud-based:** GPT-4o and GPT-4-turbo (via OpenAI API)
    * **Locally run:** Llama 3.1 8B

## 🧪 Installation

Install the package directly from PyPI:

```bash
pip install schema-miner
```

If you are working with the source code directly, install dependencies from [requirements.txt](requirements.txt):


```bash
git clone https://github.com/sciknoworg/schema-miner.git
cd schema-miner
pip install -r requirements.txt
```

## 🚀 Quick Start

For a quick start, see the provided example notebooks highlighting the overall workflows of the schema-miner.

<div align="center">

|  | Notebook |
| --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | [Schema Mining With LLMs and expert Example](tutorials/notebooks/schema_mining_with_LLMs_and_expert_example.ipynb) |
| 2 | [Schema Ontology Grounding Example](tutorials/notebooks/schema_mining_ontology_grounding_example.ipynb) |

</div>

##  🧑‍💻 Schema-miner<sup>pro</sup> Tool Usage

Schema_Miner enables schema discovery and refinement through a 3-stage pipeline (Stage 1 to 3) powered by LLMs, domain expertise, and scientific literature. Schema-Miner<sup>pro</sup> extends this pipeline with an automated ontology-grounding component (Stage 4), performing multi-step reasoning and semantic alignment to formal ontologies, while preserving human-in-the-loop validation.

### 🛠️ Configuration
Before running schema-miner, configure your environment. For example:

```python
from schema_miner.config.envConfig import EnvConfig
EnvConfig.OPENAI_api_key = '<insert-your-openai-key>'
EnvConfig.OPENAI_organization_id = '<insert-your-openi-organization-id>'
```

### 📂 Data Setup
Before running schema-miner, we need to tell schema-miner where to find:

- **Domain specification document(s)** → used for initial schema mining
- **Curated corpus** (high-quality literature) → used for refinement
- **Broader corpus** (larger set of papers) → used for final validation

```python
# Process Specification for Stage 1
process_specification_filepath = '../data/stage-1/Atomic-Layer-Deposition/Experimental-Usecase'
process_specification_filename = 'ALD-Process-Development.pdf'

# Small curated corpus of scientific papers
scientific_paper_stage2_dir = '../data/stage-2/Atomic-Layer-Deposition/research-papers/experimental-usecase'

# Bigger corpus of scientific papers
scientific_paper_stage3_dir = '../data/stage-3/Atomic-Layer-Deposition/research-papers/experimental_usecase'
```

### 🧪 Process Setup
Initialize the process name and description whose schema has to be extracted

```python
from schema_miner.config.processConfig import ProcessConfig
ProcessConfig.Process_name = "Atomic Layer Deposition"
ProcessConfig.Process_description = "An ALD process involves a series of controlled chemical reactions used to deposit thin films on a surface at an atomic level"
```

### 🧩 Stage 1 – Initial Schema Mining

Generate an initial JSON schema from a process specification document using a preferred LLM.

```python
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
results_file_path = Path("./results/stage-1/Atomic-Layer-Deposition/experimental-schema")
schema = extract_schema_stage1(llm_model_name, process_specification, results_file_path, save_schema = True)
```

### 🔄 Stage 2 – Preliminary Schema Refinement

Refine the Stage 1 schema using scientific literature and expert feedback.

```python
from schema_miner.schema_extractor.extract_schema import extract_schema_stage2

# Input Initial Schema, Expert Feedback and Scientific Literature
schema = Path("./results/stage-1/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
expert_review = Path("./data/stage-2/Atomic-Layer-Deposition/domain-expert-reviews/experimental-usecase/method-1/gpt-4o.txt")
scientific_paper = pdf_text_extractor(scientific_paper_stage2_dir, '1 Groner et al.pdf', return_text = True)

# Refine schema
results_file_path = Path("./results/stage-2/Atomic-Layer-Deposition/experimental-schema")
schema = extract_schema_stage2(llm_model_name, schema, expert_review, scientific_paper, results_file_path, save_schema = True)
```

### 🏁 Stage 3 – Final Schema Refinement

Validate and finalize the schema using a larger corpus of research papers and expert review, ensuring generalizability and semantic robustness.

```python
from schema_miner.schema_extractor.extract_schema import extract_schema_stage3

# Input Schema, Expert Feedback and Scientific Literature
schema = Path("./results/stage-2/Atomic-Layer-Deposition/experimental-schema/gpt-4o.json")
expert_review = Path("./data/stage-3/Atomic-Layer-Deposition/domain-expert-reviews/experimental-usecase/Experiment-1/1a/gpt-4o.txt")
scientific_paper = pdf_text_extractor(scientific_paper_stage3_dir, '1-Mattinen et al.pdf', return_text = True)

# Finalize schema
results_file_path = Path("./results/stage-3/Atomic-Layer-Deposition/experimental-schema")
schema = extract_schema_stage3(llm_model_name, schema, expert_review, scientific_paper, results_file_path, save_schema = True)

# View Final Schema
logging.info(f"{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent=2)}")
```

### 🌐 Stage 4 – Ontology Grounding with QUDT

Once a process schema is extracted, it can be semantically grounded using the [QUDT Ontologies](https://www.qudt.org/pages/HomePage.html) (Quantities, Units, Dimensions, and Data Types).

The grounding workflow uses either LLM prompting or an agentic LLM approach to align schema fields with QUDT concepts. Following is an example of an agent based qudt grounding.

```python
from schema_miner.ontology_grounding.agentic_qudt_grounding import agentic_qudt_grounding

# Select LLM for grounding
llm_model_name = 'gpt-4o'

# Ground the schema with QUDT Ontology
process_schema = Path('./results/Ideal Schema/Atomic-Layer-Deposition/experimental-ideal-schema.json')
results_file_path = Path("./results/qudt-grounded/Atomic-Layer-Deposition/experimental-schema")
schema = agentic_qudt_grounding(llm_model_name, process_schema, results_file_path, save_schema = True)

# Display grounded schema
logging.info(f'{ProcessConfig.Process_name} Schema:\n{json.dumps(schema, indent = 2)}')
```

## 📚 Citing this Work

If you use this repository in your research or applications, please cite the appropriate paper(s):

- Schema-Miner (schema discovery/mining only):
  > Sameer Sadruddin, Jennifer D’Souza, Eleni Poupaki, Alex Watkins, Hamed Babaei Giglou, Anisa Rula, Bora Karasulu, Sören Auer, Adrie Mackus, and Erwin Kessels.
  > **LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models.**
  > In *The Semantic Web – ESWC 2025*, Springer, Cham, pp. 244–261.
  > [https://doi.org/10.1007/978-3-031-94578-6_14](https://doi.org/10.1007/978-3-031-94578-6_14)

  ### 📌 BibTeX
  ```bibtex
  @InProceedings{10.1007/978-3-031-94578-6_14,
    author    = {Sadruddin, Sameer and D'Souza, Jennifer and Poupaki, Eleni and Watkins, Alex and Babaei Giglou, Hamed and Rula, Anisa and Karasulu, Bora and Auer, S{\"o}ren and Mackus, Adrie and Kessels, Erwin},
    editor    = {Curry, Edward and Acosta, Maribel and Poveda-Villal{\'o}n, Maria and van Erp, Marieke and Ojo, Adegboyega and Hose, Katja and Shimizu, Cogan and Lisena, Pasquale},
    title     = {LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models},
    booktitle = {The Semantic Web},
    year      = {2025},
    publisher = {Springer Nature Switzerland},
    address   = {Cham},
    pages     = {244--261},
    isbn      = {978-3-031-94578-6},
  }
  ```
- Schema-Miner<sup>pro</sup> (schema mining with QUDT grounding / ontology grounding):
  > Sameer Sadruddin, Jennifer D’Souza, Eleni Poupaki, Alex Watkins, Bora Karasulu, Sören Auer, Adrie Mackus, and Erwin Kessels.
  > **SCHEMA-MINER<sup>pro</sup>: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow.**
  > In *Semantic Web Journal.*
  > [https://www.semantic-web-journal.net/system/files/swj3871.pdf](https://www.semantic-web-journal.net/system/files/swj3871.pdf)

  ### 📌 BibTeX
  ```bibtex
  @InProceedings{10.1007/978-3-031-94578-6_14,
    author    = {Sadruddin, Sameer and D'Souza, Jennifer and Poupaki, Eleni and Watkins, Alex and Karasulu, Bora and Auer, S{\"o}ren and Mackus, Adrie and Kessels, Erwin},
    title     = {SCHEMA-MINERpro: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow},
    journal = {Semantic Web Journal},
    year      = {2025},
  }
  ```

## 👥 Contact & Contributions

We’d love to hear from you!
Whether you're interested in collaborating on `schema miner pro` or have ideas to extend its capabilities, feel free to reach out:

- **Collaboration inquiries:** Contact Jennifer D'Souza at jennifer.dsouza [at] tib.eu

- **Development questions or bug reports:** Please [open an issue](https://github.com/sciknoworg/schema-miner/issues) right here in the repository or get in touch with the lead developer Sameer Sadruddin at sameer.sadruddin [at] tib.eu

Let’s build better schema-mining tools—together!

## 📃 License

This work is licensed under a [MIT License](LICENSE.txt)
