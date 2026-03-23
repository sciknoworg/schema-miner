<p align="center">
<img width="450" src="https://github.com/sciknoworg/schema-miner/blob/main/assets/schema-miner-pro-logo.jpg?raw=true" alt="schema miner pro logo" />
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

Schema-Miner is a novel framework that leverages Large Language Models (LLMs) and continuous human feedback to automate and enhance the schema mining task. Through an iterative process, the framework uses LLMs to extract and organize properties from unstructured text and refines schemas with expert input [ESWC Proceedings](https://link.springer.com/chapter/10.1007/978-3-031-94578-6_14). Schema-Miner<sup>pro</sup> extends Schema-Miner with an ontology grounding component powered by agentic AI. It performs multi-step reasoning using lexical heuristics and semantic similarity search, and grounds schema elements in formal ontologies (e.g., [QUDT](https://www.qudt.org/pages/HomePage.html)). Comprehensive documentation for Schema-Miner Pro, including detailed guides and examples, is available at [schema-miner.readthedocs.io](https://schema-miner.readthedocs.io/en/latest/).

> [!NOTE]
> **Schema-Miner** implements a three-stage pipeline for schema discovery and refinement without ontology grounding (see Figure 1). **Schema-Miner Pro** extends this pipeline by grounding the discovered schemas to formal ontologies.

<p align="center">
  <img src="https://raw.githubusercontent.com/sciknoworg/schema-miner/refs/heads/main/assets/LLM4SchemaMining%20-%20Workflow%20design.svg" height="300">
</p>

<p align="center">
  Figure 1: Overview of the LLMs4SchemaDiscovery workflow implemented in the SCHEMA-MINER tool. Stage 1 generates an initial process schema using domain specifications, while Stage 2, refines this schema using a small, curated scientific corpus. In Stage 3, schema is further enriched using a larger, non-curated corpus. The final stage involves grounding the properties in formal ontologies.
</p>

## 🧪 Installation

Install the package directly from PyPI using ``pip``:

```bash
pip install schema-miner
```

If you are working with the source code directly, install dependencies from [requirements.txt](requirements.txt):

```bash
git clone https://github.com/sciknoworg/schema-miner.git
cd schema-miner
pip install -r requirements.txt
```

> [!IMPORTANT]
> Before running schema-miner for the first time, configure your environment by copying `.env.example` to `.env` and filling in your values. See the [Configuration](#️-configuration) section below.

## ⚙️ Configuration

Schema-Miner is configured entirely through a `.env` file in the project root. Copy the provided template and fill in your values:

```bash
cp .env.example .env
```

### 🤖 Model Configuration

Select your LLM provider and model, then fill in **only** the credentials block for that provider:

```ini
# Active provider — options: OPENAI | SAIA | OLLAMA | HUGGINGFACE
# Use SAIA for any OpenAI-compatible endpoint (GWDG/SAIA, OpenRouter, etc.)
LLM_PROVIDER = '<Your LLM provider here>'
LLM_MODEL = '<Your model here>'                          # e.g. mistral-large-3-675b-instruct-2512, gemma-3-27b-it

# OpenAI
OPENAI_API_KEY = '<your-openai-api-key>'
OPENAI_ORGANIZATION_ID = '<your-openai-organization-id>' # Optional, only needed if you have multiple organizations in OpenAI

# SAIA / Any OpenAI-compatible endpoint
# Schema-Miner supports any service exposing an OpenAI-compatible API.
# Provide your API key and the base URL for your preferred provider.
SAIA_API_KEY = '<your-api-key>'                         # SAIA key  OR  OpenRouter key 
SAIA_BASE_URL = 'https://chat-ai.academiccloud.de/v1'   # GWDG/SAIA (Germany) | or use https://openrouter.ai/api/v1 for OpenRouter

# Ollama  (leave blank if running locally on the same machine)
OLLAMA_BASE_URL = '<OLLAMA Server Base URL>'

# HuggingFace
HuggingFace_Access_Token = '<your-huggingface-access-token>'
HUGGINGFACE_USE_LOCAL = False                            # True = load model locally (GPU recommended) | False = use Inference API
```

#### Supported LLM Providers

Schema-Miner supports **any service that exposes an OpenAI-compatible API** via the `SAIA` provider type — just supply your API key and the service's base URL.

| Provider | `LLM_PROVIDER` value | Example models | Notes |
|---|---|---|---|
| OpenAI | `OPENAI` | `gpt-4o`, `o3-mini` | Requires `OPENAI_API_KEY` |
| GWDG / SAIA | `SAIA` | `gemma-3-27b-it`, `qwen3-30b-a3b-instruct-2507` | OpenAI-compatible; set `SAIA_BASE_URL = https://chat-ai.academiccloud.de/v1` |
| OpenRouter | `SAIA` | `qwen/qwen3-235b-a22b-2507`, `anthropic/claude-sonnet-4.6` | OpenAI-compatible; set `SAIA_BASE_URL = https://openrouter.ai/api/v1` — see [openrouter.ai/docs](https://openrouter.ai/docs/quickstart) |
| Ollama | `OLLAMA` | `llama3.2:3b`, `ministral-3:3b` | Local or remote server; no API key needed |
| HuggingFace | `HUGGINGFACE` | `Qwen/Qwen3-4B-Instruct-2507` | Local GPU mode or serverless Inference API. Requires `HuggingFace_Access_Token` | 

> [!NOTE]
> **HuggingFace local mode** (`HUGGINGFACE_USE_LOCAL = True`) downloads and runs the model on your machine. A CUDA-compatible GPU is strongly recommended for models larger than 1B parameters. For CPU-only machines, use the **Inference API** (`HUGGINGFACE_USE_LOCAL = False`) instead.

### 🔬 Process Configuration

Define the scientific process whose schema you want to discover:

```ini
PROCESS_NAME = '<your-process-name>'
PROCESS_DESCRIPTION = '<a brief description of the process>'
```

These values are injected into every LLM prompt as scientific context.

### 📂 Data Paths

Point schema-miner to your input documents. Only set the path for the stage you intend to run:

```ini
# Stage 1 — path to the process specification document (PDF or plain text)
STAGE1_SPECS_PATH = 'data/stage-1/my-process/specification.pdf'

# Stage 2 — directory containing curated research papers (PDF or plain text)
STAGE2_PAPERS_PATH = 'data/stage-2/my-process/papers/'

# Stage 3 — directory containing the broader paper corpus (PDF or plain text)
STAGE3_PAPERS_PATH = 'data/stage-3/my-process/papers/'
```

### 📤 Output Configuration

Set the directory where extracted schemas will be saved:

```ini
RESULTS_PATH = 'results/my-run/'
```

---

## 🚀 Usage

Schema-Miner Pro supports two usage modes:

1. **Python SDK** — programmatic access via function calls, ideal for notebooks and custom workflows
2. **CLI** — command-line interface for direct stage execution without writing any Python

---

## 📓 Python SDK

For a quick start with the Python SDK, see the provided example notebooks:

<div align="center">

|  | Notebook |
| --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | [Schema Mining With LLMs and expert Example](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_mining_with_LLMs_and_expert_example.ipynb) |
| 2 | [Schema Ontology Grounding Example](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_mining_ontology_grounding_example.ipynb) |

</div>

---

## 🖥️ CLI Reference

Schema-Miner exposes a `schema-miner` command after installation. All configuration is read from the `.env` file — no Python code required.

```
schema-miner [OPTIONS]
```

### Options

| Option | Values | Required when | Description |
|---|---|---|---|
| `--stage` | `1`, `2`, `3` | Mutually exclusive with `--ontology-grounding` | Run a schema extraction stage |
| `--ontology-grounding` | `prompt`, `agentic` | Mutually exclusive with `--stage` | Run ontology grounding |
| `--schema` | `<path>` | Stages 2, 3, and ontology grounding | Path to the input JSON schema file |
| `--expert-feedback` | `<text or path>` | Optional (stages 2 & 3) | Inline review text, or path to a `.txt` / `.md` file |
| `--papers` | `N` or `all` | Optional (stages 2 & 3) | Number of papers to process per batch (default: `1`) |
| `--version` | — | — | Display the installed version and exit |
| `--help` | — | — | Show possible options and exit |

---

### 🧩 Stage 1 — Initial Schema Mining

Generates an initial JSON schema from a process specification document using the configured LLM.

**Prerequisite**: set `STAGE1_SPECS_PATH` in `.env` (PDF or plain text file).

```bash
schema-miner --stage 1
```

Schema-Miner reads the specification document, queries the LLM, and saves the resulting JSON schema to `RESULTS_PATH`.

---

### 🔄 Stage 2 — Preliminary Schema Refinement

Refines the Stage 1 schema using domain-expert feedback and a curated corpus of scientific papers.

**Prerequisites**: set `STAGE2_PAPERS_PATH` in `.env`; have a Stage 1 schema file available.

```bash
# Basic — process papers one by one (default) without initial expert feedback and prompt user for feedback after each paper
schema-miner --stage 2 --schema results/stage-1/mistral-large-3-675b-instruct-2512.json

# With inline expert feedback for the first batch, and prompt user for feedback after each subsequent paper
schema-miner --stage 2 --schema results/stage-1/mistral-large-3-675b-instruct-2512.json \
    --expert-feedback "Please add units for all temperature and pressure fields."

# With expert feedback for the first batch, and prompt user for feedback after each subsequent paper
schema-miner --stage 2 --schema results/stage-1/mistral-large-3-675b-instruct-2512.json \
    --expert-feedback data/stage-2/reviews/mistral-large-3-675b-instruct-2512.txt

# Process papers in batches of 3, and NO expert feedback is provided for the first batch but user is prompted to provided feedback after each batch
schema-miner --stage 2 --schema results/stage-1/mistral-large-3-675b-instruct-2512.json --papers 3

# Process all papers in a single batch with NO expert feedback
schema-miner --stage 2 --schema results/stage-1/mistral-large-3-675b-instruct-2512.json --papers all

# Process papers in batches of 3 with inline expert feedback for the first batch, and prompt user for feedback after each subsequent batch
schema-miner --stage 2 --schema results/stage-1/mistral-large-3-675b-instruct-2512.json --papers 3 \
    --expert-feedback "Please add units for all temperature and pressure fields."
```

Schema-Miner iteratively processes the papers, updating the schema after each paper and optionally incorporating expert feedback. The intermediate schemas after each iteration and the final refined schema are saved to `RESULTS_PATH`.

---

### 🏁 Stage 3 — Final Schema Refinement

Validates and finalises the schema using a larger, non-curated paper corpus and expert review, ensuring generalisability and semantic robustness.

**Prerequisites**: set `STAGE3_PAPERS_PATH` in `.env`; have a Stage 2 schema file available.

```bash
# Basic — process papers one by one (default) without initial expert feedback and prompt user for feedback after each paper
schema-miner --stage 3 --schema results/stage-2/mistral-large-3-675b-instruct-2512.json

# With inline expert feedback for the first batch, and prompt user for feedback after each subsequent paper
schema-miner --stage 3 --schema results/stage-2/mistral-large-3-675b-instruct-2512.json \
    --expert-feedback "Ensure all quantities reference standard SI units."

# With expert feedback  for the first batch, and prompt user for feedback after each subsequent paper
schema-miner --stage 3 --schema results/stage-2/mistral-large-3-675b-instruct-2512.json \
    --expert-feedback data/stage-3/reviews/mistral-large-3-675b-instruct-2512.txt

# Process papers in batches of 5, and NO expert feedback is provided for the first batch but user is prompted to provided feedback after each batch
schema-miner --stage 3 --schema results/stage-2/mistral-large-3-675b-instruct-2512.json --papers 5

# Process all papers in a single batch with NO expert feedback
schema-miner --stage 3 --schema results/stage-2/mistral-large-3-675b-instruct-2512.json --papers all

# Process papers in batches of 5 with inline expert feedback for the first batch, and prompt user for feedback after each subsequent batch
schema-miner --stage 3 --schema results/stage-2/mistral-large-3-675b-instruct-2512.json --papers 5 \
    --expert-feedback "Ensure all quantities reference standard SI units."
```

Schema-Miner processes the papers iteratively, updating the schema after each paper and optionally incorporating expert feedback. The intermediate schemas after each iteration and the final refined schema are saved to `RESULTS_PATH`.

---

### 🌐 Ontology Grounding with QUDT

Semantically grounds the discovered schema against the [QUDT](https://www.qudt.org/pages/HomePage.html) (Quantities, Units, Dimensions, and Data Types) ontology.

Two grounding methods are available:

| Method | `--ontology-grounding` value | Description |
|---|---|---|
| Prompt-based | `prompt` | Single LLM call per schema field; fast and lightweight |
| Agentic | `agentic` | Multi-step reasoning with lexical heuristics and semantic similarity search; higher accuracy |

```bash
# Prompt-based grounding
schema-miner --ontology-grounding prompt --schema results/stage-3/mistral-large-3-675b-instruct-2512.json

# Agentic grounding (recommended)
schema-miner --ontology-grounding agentic --schema results/stage-3/mistral-large-3-675b-instruct-2512.json
```

The grounded schema is saved to `RESULTS_PATH`.

## 📚 Citing this Work

If you use this repository in your research or applications, please cite the following paper(s):

- **LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models**:
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
- **SCHEMA-MINER<sup>pro</sup>: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow**
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
Whether you're interested in collaborating on `Schema-MinerPro` or have ideas to extend its capabilities, feel free to reach out:

- **Collaboration inquiries:** Contact Jennifer D'Souza at jennifer.dsouza [at] tib.eu

- **Development questions or bug reports:** Please [open an issue](https://github.com/sciknoworg/schema-miner/issues) right here in the repository or get in touch with the lead developer Sameer Sadruddin at sameer.sadruddin [at] tib.eu

Let’s build better schema-mining tools—together!

## 📃 License

This work is licensed under a [MIT License](LICENSE.txt)
