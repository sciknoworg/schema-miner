<p align="center">
<img width="450" src="https://github.com/sciknoworg/schema-miner/blob/main/assets/schema-miner-pro-logo.jpg?raw=true" alt="schema-miner pro logo" />
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

<h3 align="center">SCHEMA-MINER<sup>pro</sup>: Scientific Schema Mining and Ontology Grounding with LLMs and Human Feedback</h3>

Schema-Miner is an open-source framework for scientific schema mining from process specifications and research literature. It uses Large Language Models (LLMs), expert feedback, and iterative refinement to generate structured JSON schemas from unstructured scientific text. Schema-Miner<sup>pro</sup> extends the workflow with ontology grounding against QUDT, enabling schema fields to be linked to quantity kinds, units, and semantic identifiers.

Project page: [https://sciknoworg.github.io/schema-miner/](https://sciknoworg.github.io/schema-miner/)

Documentation: [https://schema-miner.readthedocs.io/en/latest/](https://schema-miner.readthedocs.io/en/latest/)

Source code: [https://github.com/sciknoworg/schema-miner](https://github.com/sciknoworg/schema-miner)

## Installation

Install from PyPI:

```bash
pip install schema-miner
```

To work from source:

```bash
git clone https://github.com/sciknoworg/schema-miner.git
cd schema-miner
pip install -r requirements.txt
```

Schema-Miner requires Python 3.12 or newer.

## Configuration

Before running the CLI, copy the example environment file and fill in the values for your selected provider and workflow stage:

```bash
cp .env.example .env
```

Core variables:

| Variable | Meaning |
| --- | --- |
| `LLM_PROVIDER` | Active provider: `OPENAI`, `SAIA`, `OLLAMA`, or `HUGGINGFACE`. Use `SAIA` for KISSKI SAIA, OpenRouter, or any OpenAI-compatible endpoint. |
| `LLM_MODEL` | Model name for the selected provider. |
| `PROCESS_NAME` | Scientific process name injected into prompts. |
| `PROCESS_DESCRIPTION` | Short process description injected into prompts. |
| `RESULTS_PATH` | Directory where generated schemas, intermediate schemas, grounded schemas, and logs are written. |

Provider variables:

| Provider | Required variables | Notes |
| --- | --- | --- |
| OpenAI | `OPENAI_API_KEY`; optional `OPENAI_ORGANIZATION_ID` | API-based inference. |
| KISSKI SAIA / GWDG | `LLM_PROVIDER=SAIA`, `SAIA_API_KEY`, `SAIA_BASE_URL=https://chat-ai.academiccloud.de/v1` | OpenAI-compatible academic cloud endpoint. |
| OpenRouter | `LLM_PROVIDER=SAIA`, `SAIA_API_KEY`, `SAIA_BASE_URL=https://openrouter.ai/api/v1` | OpenAI-compatible router endpoint. |
| Ollama | `LLM_PROVIDER=OLLAMA`, optional `OLLAMA_BASE_URL` | Local or remote Ollama server. |
| Hugging Face | `LLM_PROVIDER=HUGGINGFACE`, `HuggingFace_Access_Token`, `HUGGINGFACE_USE_LOCAL` | Local GPU mode when `HUGGINGFACE_USE_LOCAL=True`; serverless Inference API when `False`. |

Stage input paths:

| Variable | Used by | Expected data |
| --- | --- | --- |
| `STAGE1_SPECS_PATH` | Stage 1 | Process specification file in `.txt`, `.md`, or `.pdf` format. |
| `STAGE2_PAPERS_PATH` | Stage 2 | Directory of curated scientific papers in `.txt`, `.md`, or `.pdf` format. |
| `STAGE3_PAPERS_PATH` | Stage 3 | Directory of broader validation/refinement papers in `.txt`, `.md`, or `.pdf` format. |

## CLI Reference

After installation, the package exposes the `schema-miner` command:

```bash
schema-miner [OPTIONS]
```

Options:

| Option | Values | Required when | Description |
| --- | --- | --- | --- |
| `--stage` | `1`, `2`, `3` | Run schema extraction/refinement | `1` runs initial schema mining, `2` preliminary refinement, and `3` final refinement. Mutually exclusive with `--ontology-grounding`. |
| `--ontology-grounding` | `prompt`, `agentic` | Run ontology grounding | Grounds a final schema with QUDT. Mutually exclusive with `--stage`. |
| `--schema` | Path to `.json` | Stages 2 and 3; ontology grounding | Input schema from the previous stage or the final schema to ground. |
| `--expert-feedback` | Inline text or `.txt`/`.md` path | Optional for stages 2 and 3 | Expert guidance incorporated into the next refinement pass. |
| `--papers` | Positive integer or `all` | Optional for stages 2 and 3 | Batch size for paper processing. Omit for one paper per batch; use `all` to process the full directory in one batch. |
| `--version` | None | Optional | Show installed CLI version. |
| `--help` | None | Optional | Show CLI help. |

### Stage 1: Initial Schema Mining

Input variables:

- `LLM_PROVIDER`, `LLM_MODEL`, `PROCESS_NAME`, `PROCESS_DESCRIPTION`, provider credentials, and `RESULTS_PATH`
- `STAGE1_SPECS_PATH`, pointing to a `.txt`, `.md`, or `.pdf` process specification

Run:

```bash
schema-miner --stage 1
```

Output:

- Initial JSON schema saved under `RESULTS_PATH`
- Stage log information written alongside the generated result

### Stage 2: Preliminary Refinement

Input variables and files:

- `STAGE2_PAPERS_PATH`, pointing to the curated Stage 2 literature directory
- `--schema`, pointing to the Stage 1 JSON schema
- Optional `--expert-feedback`, either inline text or a `.txt`/`.md` review file
- Optional `--papers`, controlling paper batch size

Examples:

```bash
# One paper per batch, no initial expert feedback
schema-miner --stage 2 --schema results/stage-1/<model>.json

# Three papers per batch with inline expert feedback
schema-miner --stage 2 --schema results/stage-1/<model>.json --papers 3 \
    --expert-feedback "Please add units for all temperature and pressure fields."

# All curated papers in one batch with feedback from a file
schema-miner --stage 2 --schema results/stage-1/<model>.json --papers all \
    --expert-feedback data/stage-2/reviews/<model>.txt
```

Output:

- Refined schema saved under `RESULTS_PATH`
- Per-paper intermediate schemas saved under `RESULTS_PATH/intermediate-schema/<model>/`
- Interactive feedback prompt between batches when additional batches remain

### Stage 3: Final Refinement

Input variables and files:

- `STAGE3_PAPERS_PATH`, pointing to the broader Stage 3 literature directory
- `--schema`, pointing to the Stage 2 JSON schema
- Optional `--expert-feedback`, either inline text or a `.txt`/`.md` review file
- Optional `--papers`, controlling paper batch size

Examples:

```bash
# One paper per batch
schema-miner --stage 3 --schema results/stage-2/<model>.json

# Five papers per batch with expert feedback
schema-miner --stage 3 --schema results/stage-2/<model>.json --papers 5 \
    --expert-feedback "Ensure all quantities reference standard SI units."

# All broader-corpus papers in one batch
schema-miner --stage 3 --schema results/stage-2/<model>.json --papers all
```

Output:

- Final refined schema saved under `RESULTS_PATH`
- Per-paper intermediate schemas saved under `RESULTS_PATH/intermediate-schema/<model>/`
- Interactive feedback prompt between batches when additional batches remain

### Ontology Grounding

Input variables and files:

- `--ontology-grounding`, set to `prompt` or `agentic`
- `--schema`, pointing to the final JSON schema from Stage 3
- `RESULTS_PATH`, where the grounded schema will be saved

Examples:

```bash
# Prompt-based grounding
schema-miner --ontology-grounding prompt --schema results/stage-3/<model>.json

# Agentic grounding with lexical search, semantic search, and LLM reasoning
schema-miner --ontology-grounding agentic --schema results/stage-3/<model>.json
```

Output:

- QUDT-grounded JSON schema saved under `RESULTS_PATH`

## Tutorial Notebooks

For guided, end-to-end usage, start from the provider-specific notebooks:

| Notebook | Inference | Example model | GPU required |
| --- | --- | --- | --- |
| [Hugging Face - Local GPU](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_huggingface_gpu_tutorial.ipynb) | Local | `mistralai/Ministral-3-8B-Instruct-2512` | Yes |
| [KISSKI SAIA](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_saia_tutorial.ipynb) | Remote API | `qwen3-30b-a3b-instruct-2507` | No |
| [OpenRouter](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_openrouter_tutorial.ipynb) | Remote API | `qwen/qwen3-235b-a22b` | No |

Ontology grounding example:

- [Schema Ontology Grounding Example](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_mining_ontology_grounding_example.ipynb)

## Citing This Work

If you use Schema-Miner in research or applications, please cite:

- **LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models**
  Sameer Sadruddin, Jennifer D'Souza, Eleni Poupaki, Alex Watkins, Hamed Babaei Giglou, Anisa Rula, Bora Karasulu, Soren Auer, Adrie Mackus, and Erwin Kessels.
  In *The Semantic Web - ESWC 2025*, Springer, pp. 244-261.
  [https://doi.org/10.1007/978-3-031-94578-6_14](https://doi.org/10.1007/978-3-031-94578-6_14)

- **SCHEMA-MINERpro: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow**
  Sameer Sadruddin, Eleni Poupaki, Alex Watkins, Bora Karasulu, Adriaan J. M. Mackus, Erwin Kessels, Soren Auer, and Jennifer D'Souza.
  In *Semantic Web*, 2026.
  [https://doi.org/10.1177/22104968261431521](https://doi.org/10.1177/22104968261431521)

## Contact and Contributions

Collaboration inquiries: Jennifer D'Souza, jennifer.dsouza [at] tib.eu.

Development questions or bug reports: open an issue at [https://github.com/sciknoworg/schema-miner/issues](https://github.com/sciknoworg/schema-miner/issues) or contact Sameer Sadruddin, sameer.sadruddin [at] tib.eu.

## License

Schema-Miner is released under the [MIT License](https://github.com/sciknoworg/schema-miner/blob/main/LICENSE.txt).
