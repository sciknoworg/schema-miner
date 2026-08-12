<p align="center">
<img width="420" src="https://github.com/sciknoworg/schema-miner/blob/main/assets/schema-miner-pro-logo.jpg?raw=true" alt="schema-miner pro logo" />
</p>

<div align="center">

[![PyPI - Version](https://img.shields.io/pypi/v/schema-miner)](https://pypi.org/project/schema-miner/)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/schema-miner)](https://pepy.tech/projects/schema-miner)
[![Maintained Yes](https://img.shields.io/badge/maintained-yes-green)](https://github.com/sciknoworg/schema-miner/blob/main/MAINTENANCE.md)
[![MIT License](https://img.shields.io/github/license/sciknoworg/schema-miner)](LICENSE)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](https://schema-miner.readthedocs.io/en/latest/)

</div>

<h3 align="center">SCHEMA-MINER<sup>pro</sup>: Scientific Schema Mining and Ontology Grounding with LLMs</h3>

Schema-Miner is a command-line and Python package for mining scientific JSON schemas from process specifications and research literature. It supports a human-in-the-loop workflow for schema refinement and an ontology-grounding step that enriches schema fields with QUDT quantity and unit metadata.

Use this PyPI page for installation and CLI orientation. For the full workflow, figures, notebooks, and project background, see:

- Project page: [https://sciknoworg.github.io/schema-miner/](https://sciknoworg.github.io/schema-miner/)
- Documentation: [https://schema-miner.readthedocs.io/en/latest/](https://schema-miner.readthedocs.io/en/latest/)
- Source code: [https://github.com/sciknoworg/schema-miner](https://github.com/sciknoworg/schema-miner)

## Installation

```bash
pip install schema-miner
```

Schema-Miner requires Python 3.12 or newer.

To install from source:

```bash
git clone https://github.com/sciknoworg/schema-miner.git
cd schema-miner
pip install -r requirements.txt
```

## Minimal Configuration

Copy the example environment file and edit it:

```bash
cp .env.example .env
```

Required workflow settings:

```ini
# Active provider — options: OPENAI | SAIA | OPENROUTER | OLLAMA | HUGGINGFACE
# Use SAIA for any other endpoint exposing an OpenAI-compatible API
LLM_PROVIDER = '<Your LLM provider here>'
LLM_MODEL = '<Your model here>'                          # e.g. mistral-large-3-675b-instruct-2512, gemma-3-27b-it

# OpenAI
OPENAI_API_KEY = '<your-openai-api-key>'
OPENAI_ORGANIZATION_ID = '<your-openai-organization-id>' # Optional, only needed if you have multiple organizations in OpenAI

# SAIA / Any OpenAI-compatible endpoint
# Schema-Miner supports any service exposing an OpenAI-compatible API.
# Provide your API key and the base URL for your preferred provider.
SAIA_API_KEY = '<your-api-key>'
SAIA_BASE_URL = 'https://chat-ai.academiccloud.de/v1'   # GWDG/SAIA (Germany)

# OpenRouter
OPENROUTER_API_KEY = '<your-openrouter-api-key>'
OPENROUTER_BASE_URL = 'https://openrouter.ai/api/v1'

# Ollama  (leave blank if running locally on the same machine)
OLLAMA_BASE_URL = '<OLLAMA Server Base URL>'

# HuggingFace
HuggingFace_Access_Token = '<your-huggingface-access-token>'
HUGGINGFACE_USE_LOCAL = False                            # True = load model locally (GPU recommended) | False = use Inference API
```

## CLI Quick Start

Run one workflow step at a time:

```bash
# Stage 1: generate an initial schema from the process specification
schema-miner --stage 1

# Stage 2: refine with a curated paper corpus and optional expert feedback
schema-miner --stage 2 --schema results/stage-1/<model>.json --papers 3

# Stage 3: finalize with a broader paper corpus
schema-miner --stage 3 --schema results/stage-2/<model>.json --papers all

# Ontology grounding: enrich the final schema with QUDT metadata
schema-miner --ontology-grounding agentic --schema results/stage-3/<model>.json
```

Common options:

| Option | Meaning |
| --- | --- |
| `--stage 1` | Initial schema mining from `STAGE1_SPECS_PATH`. |
| `--stage 2` | Preliminary refinement using `STAGE2_PAPERS_PATH`; requires `--schema`. |
| `--stage 3` | Final refinement using `STAGE3_PAPERS_PATH`; requires `--schema`. |
| `--schema <path>` | Input JSON schema for stages 2, 3, or ontology grounding. |
| `--expert-feedback <text-or-file>` | Optional feedback for stages 2 and 3. |
| `--papers <N or all>` | Paper batch size for stages 2 and 3. |
| `--ontology-grounding prompt` | Prompt-based QUDT grounding. |
| `--ontology-grounding agentic` | Agentic QUDT grounding with lexical and semantic lookup. |

Generated schemas, intermediate outputs, grounded schemas, and logs are written under `RESULTS_PATH`.

## CLI Usage Scenarios

### Check the Installed CLI

```bash
schema-miner --help
schema-miner --version
```

### Stage 1: Initial Schema Mining

Use this when you have a process specification and want the first JSON schema.

Required `.env` values:

- `PROCESS_NAME`
- `PROCESS_DESCRIPTION`
- `STAGE1_SPECS_PATH`
- `RESULTS_PATH`
- LLM provider and credentials

Run:

```bash
schema-miner --stage 1
```

The command reads `STAGE1_SPECS_PATH` and writes the initial schema to `RESULTS_PATH`.

### Stage 2: Preliminary Refinement

Use this when you have a Stage 1 schema and a small curated paper corpus.

Required inputs:

- `STAGE2_PAPERS_PATH` in `.env`
- `--schema` pointing to the Stage 1 JSON schema

Process one paper per batch:

```bash
schema-miner --stage 2 --schema data/stage1/schema/<model>.json
```

Process with inline expert feedback for the first batch:

```bash
schema-miner --stage 2 --schema data/stage1/schema/<model>.json \
    --expert-feedback "Add units for temperature and pressure fields."
```

Process with expert feedback from a file:

```bash
schema-miner --stage 2 --schema data/stage1/schema/<model>.json \
    --expert-feedback data/stage1/feedback/<model>.txt
```

Process papers in fixed-size batches:

```bash
schema-miner --stage 2 --schema data/stage1/schema/<model>.json --papers 3
```

Process all curated papers in one batch:

```bash
schema-miner --stage 2 --schema data/stage1/schema/<model>.json --papers all
```

Process papers in fixed-size batches with initial inline expert feedback:

```bash
schema-miner --stage 2 --schema data/stage1/schema/<model>.json --papers 3 \
    --expert-feedback "Add units for temperature and pressure fields."
```

### Stage 3: Final Refinement

Use this when you have the final Stage 2 schema and a broader validation/refinement corpus.

Required inputs:

- `STAGE3_PAPERS_PATH` in `.env`
- `--schema` pointing to the final Stage 2 JSON schema

All CLI usage patterns are the same as for Stage 2. One example is shown below.

Run papers in batches of 5 with initial expert feedback from a file:

```bash
schema-miner --stage 3 --schema results/stage-2/<model>.json --papers 5 \
    --expert-feedback data/stage-2/feedback/<model>.txt
```

### Stage 4: Ontology Grounding

Use this when you have a final schema and want QUDT quantity/unit grounding.

Prompt-based grounding:

```bash
schema-miner --ontology-grounding prompt --schema results/stage-3/<model>.json
```

Agentic grounding:

```bash
schema-miner --ontology-grounding agentic --schema results/stage-3/<model>.json
```

## Tutorial Notebooks

| Notebook | Inference mode |
| --- | --- |
| [Hugging Face local GPU](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_huggingface_gpu_tutorial.ipynb) | Local model |
| [KISSKI SAIA](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_saia_tutorial.ipynb) | Remote OpenAI-compatible API |
| [OpenRouter](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_openrouter_tutorial.ipynb) | Remote OpenAI-compatible API |

## Contact

Collaboration inquiries: Jennifer D'Souza, jennifer.dsouza [at] tib.eu.

Development questions or bug reports: [open an issue](https://github.com/sciknoworg/schema-miner/issues) or contact Sameer Sadruddin, sameer.sadruddin [at] tib.eu.

## License

Schema-Miner is released under the [MIT License](https://github.com/sciknoworg/schema-miner/blob/main/LICENSE.txt).
