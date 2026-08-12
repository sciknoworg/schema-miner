<p align="center">
<img width="450" src="https://github.com/sciknoworg/schema-miner/blob/main/assets/schema-miner-pro-logo.jpg?raw=true" alt="schema miner pro logo" />
</p>

<div align="center">

[![Project Website](https://img.shields.io/badge/Project%20Website-GitHub%20Pages-2f80ed?logo=githubpages&logoColor=white)](https://sciknoworg.github.io/schema-miner/)
[![PyPI - Version](https://img.shields.io/badge/pypi-v3.2.6-blue)](https://pypi.org/project/schema-miner/)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/schema-miner)](https://pepy.tech/projects/schema-miner)
[![Maintained Yes](https://img.shields.io/badge/maintained-yes-green)](https://github.com/sciknoworg/schema-miner/blob/main/MAINTENANCE.md)
[![MIT License](https://img.shields.io/github/license/sciknoworg/schema-miner)](LICENSE)
[![DOI](https://zenodo.org/badge/900734076.svg)](https://doi.org/10.5281/zenodo.14781824)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](https://schema-miner.readthedocs.io/en/latest/)

</div>

<h3 align="center">Scientific Schema Mining and Ontology Grounding with Large Language Models</h3>

Schema-Miner is an open-source Python package and command-line tool for mining structured scientific schemas from process specifications and research literature. It supports iterative human-in-the-loop schema refinement and optional ontology grounding.

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

Schema-Miner is configured through a `.env` file in the project root. Copy the provided template and fill in your values:

```bash
cp .env.example .env
```

### 🤖 Model Configuration

Select your LLM provider and model, then fill in **only** the credentials block for your chosen provider. The rest can be left empty.

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

#### Supported LLM Providers

Schema-Miner ships a dedicated integration for each provider listed below. Any other service that exposes an **OpenAI-compatible API** can be used through the `SAIA` provider type — just supply your API key and the service's base URL. The current default is `SAIA_BASE_URL = https://chat-ai.academiccloud.de/v1`.

| Provider | `LLM_PROVIDER` value | Example models | Notes |
|---|---|---|---|
| OpenAI | `OPENAI` | `gpt-4o`, `o3-mini` | Requires `OPENAI_API_KEY` |
| GWDG / SAIA | `SAIA` | `gemma-3-27b-it`, `qwen3-30b-a3b-instruct-2507` | Requires `SAIA_API_KEY`; set `SAIA_BASE_URL = https://chat-ai.academiccloud.de/v1` |
| OpenRouter | `OPENROUTER` | `qwen/qwen3-235b-a22b-2507`, `anthropic/claude-sonnet-4.6` | Requires `OPENROUTER_API_KEY`; set `OPENROUTER_BASE_URL = https://openrouter.ai/api/v1` — see [openrouter.ai/docs](https://openrouter.ai/docs/quickstart) |
| Ollama | `OLLAMA` | `llama3.2:3b`, `ministral-3:3b` | Local or remote server; no API key needed |
| HuggingFace | `HUGGINGFACE` | `Qwen/Qwen3-4B-Instruct-2507` | Local GPU mode or serverless Inference API. Requires `HuggingFace_Access_Token` |

> [!NOTE]
> **HuggingFace local mode** (`HUGGINGFACE_USE_LOCAL = True`) downloads and runs the model on your machine. A CUDA-compatible GPU is strongly recommended for models larger than 1B parameters. For CPU-only machines, use the **Inference API** (`HUGGINGFACE_USE_LOCAL = False`) instead.

### 🔬 Process Configuration

In the `.env` file, declare the variables for the scientific process whose schema you want to discover.

```ini
PROCESS_NAME = '<your-process-name>'
PROCESS_DESCRIPTION = '<a brief description of the process in 2 or 3 sentences>'
```

These values are injected into every LLM prompt as scientific context.

### 📂 Data Paths

Point schema-miner to your input documents pertinent to the respective specified stage. Stage 1 i.e. initial schema mining relies on just one document which is often a list of 5 to 15 properties written by a domain expert to get the schema mining started. Stages 2 and 3, on the other hand, are collections of scientific papers that deepen the schema mining process.

```ini
# Stage 1 — path to the process specification document (PDF or plain text)
STAGE1_SPECS_PATH = 'data/stage-1/my-process/specification.pdf'

# Stage 2 — directory containing curated research papers (PDF or plain text)
STAGE2_PAPERS_PATH = 'data/stage-2/my-process/papers/'

# Stage 3 — directory containing the broader paper corpus (PDF or plain text)
STAGE3_PAPERS_PATH = 'data/stage-3/my-process/papers/'
```

### 📤 Output Configuration

Set the directory where the mined schema as the output of that stage will be saved.

```ini
RESULTS_PATH = 'results/my-run/'
```

Schemas are saved at path `RESULTS_PATH/<model>.json`, where `<model>` is `LLM_MODEL`. Stages 2 and 3 additionally save the schema after each paper under `RESULTS_PATH/intermediate-schema/<model>/`.

---

## 🚀 Usage

Schema-Miner can be used in two ways:

1. **[CLI](#️-cli-reference)** — command-line interface for direct execution of the Schema-Miner workflow
2. **[Interactive tutorial notebooks](#-tutorial-notebooks)** — guided, end-to-end demonstrations of the three-stage workflow with different LLM providers and expert-feedback configurations

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
| `--papers` | `N`, `all`, or `<path>` | Optional (stages 2 & 3) | Papers per batch (default: `1`), `all` to process every paper in one batch, or a path to a single paper |
| `--version` | — | — | Display the installed version and exit |
| `--help` | — | — | Show possible options and exit |

---

### 🧩 Stage 1 — Initial Schema Mining

Generates an initial JSON schema using the specified LLM config from a process specification document. Visit an example [process spec. document](https://github.com/sciknoworg/schema-miner/blob/main/data/stage1/process-description.pdf)

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
# Basic — process papers one at a time (default), starting without expert feedback on the Stage 1 schema and prompting for iterative feedback after each paper is processed.
schema-miner --stage 2 --schema data/stage1/schema/qwen3-235b-a22b.json

# With initial expert feedback — process papers one at a time (default), applying the feedback supplied via the CLI to the Stage 1 schema and prompting for further feedback after each paper.
schema-miner --stage 2 --schema data/stage1/schema/qwen3-235b-a22b.json \
  --expert-feedback "Please add units for all temperature and pressure fields."

# With initial expert feedback from a file — process papers one at a time (default), applying the feedback from the specified file to the Stage 1 schema and prompting for further feedback after each paper.
schema-miner --stage 2 --schema data/stage1/schema/qwen3-235b-a22b.json \
  --expert-feedback data/stage1/feedback/qwen3-235b-a22b.txt

# Batchwise feedback — read papers from STAGE2_PAPERS_PATH and process them in batches of 3. Start without expert feedback on the Stage 1 schema; after each batch of 3 papers has been processed, prompt the user for feedback before continuing with the next batch. Unlike the earlier examples, feedback is collected after a batch of papers rather than after every individual paper.
schema-miner --stage 2 --schema data/stage1/schema/qwen3-235b-a22b.json --papers 3

# Single batch, no feedback — read all papers from STAGE2_PAPERS_PATH and process them iteratively, one by one, as a single batch without prompting for expert feedback. The --expert-feedback argument is optional and can therefore be omitted entirely.
schema-miner --stage 2 --schema data/stage1/schema/qwen3-235b-a22b.json --papers all

# Batchwise feedback with initial expert feedback — process papers from STAGE2_PAPERS_PATH in batches of 3. For the first batch, apply the feedback supplied via the CLI to the Stage 1 schema and to each schema iteratively mined after processing a paper in that batch. Papers within each batch are processed one at a time, with the schema updated iteratively after each paper. The feedback available at the start of a batch is reused for every paper in that batch. After each batch is processed, prompt the user for further feedback before continuing with the next batch.
schema-miner --stage 2 --schema data/stage1/schema/qwen3-235b-a22b.json --papers 3 \
  --expert-feedback "Please add units for all temperature and pressure fields."
```

Schema-Miner iteratively processes the papers, updating the schema after each paper and optionally incorporating expert feedback. The intermediate schemas after each iteration and the final refined schema are saved to `RESULTS_PATH`.

> [!NOTE]
> When the `--papers N` argument is supplied, `schema-miner` randomly creates batches of `N` papers. If you prefer to define your own batches for Stage 2 or Stage 3, see the [tutorial notebooks](#-tutorial-notebooks). As will be shown in the tutorials, a simple approach is to set `STAGE2_PAPERS_PATH` to a directory containing your predefined batch of papers for Stage 2 (e.g., [data/stage2/batch1](https://github.com/sciknoworg/schema-miner/tree/main/data/stage2/batch1) or [data/stage2/batch2](https://github.com/sciknoworg/schema-miner/tree/main/data/stage2/batch2)) and use `--papers all`. In this case, all papers in that directory are treated as a single batch, and the feedback supplied at the start of the batch is reused when each paper in that batch is processed.

---

### 🏁 Stage 3 — Final Schema Refinement

Validates and finalises the schema using a larger, non-curated paper corpus and expert review, ensuring generalisability and semantic robustness.

**Prerequisites**: set `STAGE3_PAPERS_PATH` in `.env` and have the final Stage 2 schema available—the schema obtained after all papers in Stage 2 have been processed iteratively.

All CLI usage patterns are the same as for Stage 2. The differences are the input paper collection (`STAGE3_PAPERS_PATH`) and the starting schema, which is the final schema produced by iterative mining in Stage 2. Any initial expert feedback is likewise supplied for this resulting Stage 2 schema and reused as the papers in the first batch are processed iteratively. We therefore show only one usage scenario here. Please refer to the [tutorial notebooks](#-tutorial-notebooks) for complete end-to-end usage demonstrations.

```bash
# Process papers in batches of 5 with initial expert feedback from a file, and prompt the user for further feedback after each batch
schema-miner --stage 3 --schema data/stage2/schema-batch2/qwen3-235b-a22b.json --papers 5 \
    --expert-feedback data/stage2/feedback-batch2/qwen3-235b-a22b.txt
```

Schema-Miner processes the papers iteratively, updating the schema after each paper and optionally incorporating expert feedback. The intermediate schemas after each iteration and the final refined schema are saved to `RESULTS_PATH`.

> [!NOTE]
> In general, the organization of the input data directories is entirely user-defined. The folder structures shown in the usage scenarios above follow those used in our three [demonstration tutorials](#-tutorial-notebooks). Before getting started, we recommend defining a consistent directory structure for papers, schemas, and feedback. For example, if you are mining schemas for multiple scientific processes, each with its own paper collection, you might use the process name as the top-level directory and keep the underlying stage-specific subdirectory structure consistent. This makes it straightforward to automate schema mining programmatically, for example by iterating over processes, stages, and even LLMs in a loop.

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
schema-miner --ontology-grounding prompt --schema data/stage3/schema-batch2/qwen3-235b-a22b.json

# Agentic grounding (recommended)
schema-miner --ontology-grounding agentic --schema data/stage3/schema-batch2/qwen3-235b-a22b.json
```

The grounded schema is saved to `RESULTS_PATH`.

---

## 📓 Tutorial Notebooks

For complete end-to-end demonstrations, choose the tutorial corresponding to your preferred LLM provider:

<div align="center">

|  | Tutorial | Inference | Example Model | GPU Required |
| --- | --- | --- | --- | --- |
| 1 | [Hugging Face — Local GPU](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_huggingface_gpu_tutorial.ipynb) | Local | `mistralai/Ministral-3-8B-Instruct-2512` | Yes |
| 2 | [SAIA](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_saia_tutorial.ipynb) | Remote API | `qwen3-30b-a3b-instruct-2507` | No |
| 3 | [OpenRouter](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_miner_openrouter_tutorial.ipynb) | Remote API | `qwen/qwen3-235b-a22b` | No |

</div>

Each tutorial demonstrates the complete three-stage human-in-the-loop workflow:

1. **Stage 1 — Initial Schema Mining**
2. **Stage 2 — Preliminary Schema Refinement**
3. **Stage 3 — Final Schema Refinement**

Stages 2 and 3 support iterative processing over one or more batches of scientific papers, allowing expert feedback to be incorporated between successive schema-refinement runs.

### Additional Example

- [Schema Ontology Grounding Example](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_mining_ontology_grounding_example.ipynb)

---


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
	@article{sadruddin2026schema,
	  title={Schema-miner pro: Agentic AI for ontology grounding over LLM-discovered scientific schemas in a human-in-the-loop workflow},
	  author={Sadruddin, Sameer and D’Souza, Jennifer and Poupaki, Eleni and Watkins, Alex and Karasulu, Bora and Auer, S{\"o}ren and Mackus, Adrie and Kessels, Erwin},
	  journal={Semantic Web},
	  volume={17},
	  number={3},
	  pages={22104968261431521},
	  year={2026},
	  publisher={SAGE Publications Sage UK: London, England}
	}
  ```

## 👥 Contact & Contributions

We’d love to hear from you!
Whether you're interested in collaborating on `Schema-MinerPro` or have ideas to extend its capabilities, feel free to reach out:

- **Collaboration inquiries:** Contact Jennifer D'Souza at jennifer.dsouza [at] tib.eu

- **Development questions or bug reports:** Please [open an issue](https://github.com/sciknoworg/schema-miner/issues) right here in the repository or get in touch with the lead developer Sameer Sadruddin at sameer.sadruddin [at] tib.eu

Let’s build better schema-mining tools—together!

This work is licensed under the [MIT License](LICENSE.txt).