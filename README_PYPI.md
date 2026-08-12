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
LLM_PROVIDER = "SAIA"      # OPENAI, SAIA, OLLAMA, or HUGGINGFACE
LLM_MODEL = "qwen3-30b-a3b-instruct-2507"

PROCESS_NAME = "Atomic Layer Deposition"
PROCESS_DESCRIPTION = "Layer-by-layer thin film growth process."

STAGE1_SPECS_PATH = "data/stage1/process-description.pdf"
STAGE2_PAPERS_PATH = "data/stage2/"
STAGE3_PAPERS_PATH = "data/stage3/"
RESULTS_PATH = "results/my-run/"
```

Provider credentials:

| Provider | Set in `.env` |
| --- | --- |
| OpenAI | `LLM_PROVIDER=OPENAI`, `OPENAI_API_KEY` |
| KISSKI SAIA / GWDG | `LLM_PROVIDER=SAIA`, `SAIA_API_KEY`, `SAIA_BASE_URL=https://chat-ai.academiccloud.de/v1` |
| OpenRouter | `LLM_PROVIDER=SAIA`, `SAIA_API_KEY`, `SAIA_BASE_URL=https://openrouter.ai/api/v1` |
| Ollama | `LLM_PROVIDER=OLLAMA`, optional `OLLAMA_BASE_URL` |
| Hugging Face | `LLM_PROVIDER=HUGGINGFACE`, `HuggingFace_Access_Token`, `HUGGINGFACE_USE_LOCAL` |

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
| `--papers <N|all>` | Paper batch size for stages 2 and 3. |
| `--ontology-grounding prompt` | Prompt-based QUDT grounding. |
| `--ontology-grounding agentic` | Agentic QUDT grounding with lexical and semantic lookup. |

Generated schemas, intermediate outputs, grounded schemas, and logs are written under `RESULTS_PATH`.

## CLI Usage Scenarios

### Check the Installed CLI

```bash
schema-miner --help
schema-miner --version
```

### Scenario 1: Initial Schema Mining

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

### Scenario 2: Preliminary Refinement

Use this when you have a Stage 1 schema and a small curated paper corpus.

Required inputs:

- `STAGE2_PAPERS_PATH` in `.env`
- `--schema` pointing to the Stage 1 JSON schema

Run one paper per batch:

```bash
schema-miner --stage 2 --schema results/stage-1/<model>.json
```

Run with inline expert feedback for the first batch:

```bash
schema-miner --stage 2 --schema results/stage-1/<model>.json \
    --expert-feedback "Add units for temperature and pressure fields."
```

Run with expert feedback from a file:

```bash
schema-miner --stage 2 --schema results/stage-1/<model>.json \
    --expert-feedback data/stage-2/reviews/<model>.txt
```

Run papers in fixed-size batches:

```bash
schema-miner --stage 2 --schema results/stage-1/<model>.json --papers 3
```

Run all curated papers in one batch:

```bash
schema-miner --stage 2 --schema results/stage-1/<model>.json --papers all
```

### Scenario 3: Final Refinement

Use this when you have a Stage 2 schema and a broader validation/refinement corpus.

Required inputs:

- `STAGE3_PAPERS_PATH` in `.env`
- `--schema` pointing to the Stage 2 JSON schema

Run one paper per batch:

```bash
schema-miner --stage 3 --schema results/stage-2/<model>.json
```

Run with inline expert feedback:

```bash
schema-miner --stage 3 --schema results/stage-2/<model>.json \
    --expert-feedback "Ensure measurable properties use standard SI units."
```

Run with expert feedback from a file:

```bash
schema-miner --stage 3 --schema results/stage-2/<model>.json \
    --expert-feedback data/stage-3/reviews/<model>.txt
```

Run papers in fixed-size batches:

```bash
schema-miner --stage 3 --schema results/stage-2/<model>.json --papers 5
```

Run all broader-corpus papers in one batch:

```bash
schema-miner --stage 3 --schema results/stage-2/<model>.json --papers all
```

### Scenario 4: Ontology Grounding

Use this when you have a final schema and want QUDT quantity/unit grounding.

Prompt-based grounding:

```bash
schema-miner --ontology-grounding prompt --schema results/stage-3/<model>.json
```

Agentic grounding:

```bash
schema-miner --ontology-grounding agentic --schema results/stage-3/<model>.json
```

### Scenario 5: Provider-Specific Runs

The CLI command stays the same across providers; only `.env` changes.

KISSKI SAIA:

```ini
LLM_PROVIDER = "SAIA"
LLM_MODEL = "qwen3-30b-a3b-instruct-2507"
SAIA_API_KEY = "<your-saia-key>"
SAIA_BASE_URL = "https://chat-ai.academiccloud.de/v1"
```

OpenRouter:

```ini
LLM_PROVIDER = "SAIA"
LLM_MODEL = "qwen/qwen3-235b-a22b"
SAIA_API_KEY = "<your-openrouter-key>"
SAIA_BASE_URL = "https://openrouter.ai/api/v1"
```

Hugging Face local GPU:

```ini
LLM_PROVIDER = "HUGGINGFACE"
LLM_MODEL = "mistralai/Ministral-3-8B-Instruct-2512"
HuggingFace_Access_Token = "<your-huggingface-token>"
HUGGINGFACE_USE_LOCAL = True
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
