Installation
============

System Requirements
*******************

The computational requirements for running schema- miner pro vary depending on the model being used. If utilizing OpenAI models such as `GPT-4o <https://platform.openai.com/docs/models#gpt-4o>`_ and `GPT-4-turbo <https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4>`_, no specialized hardware is needed since inference is performed via API calls. A basic system with a stable internet connection is sufficient for executing API-based workflow.

For users opting to run **open-source models** such as `Llama 3.1 8B <https://ai.meta.com/blog/meta-llama-3-1/>`_ or other large-scale transformer-based models, local execution demands significantly higher computational resources. While these models can be executed on a CPU, inference times will be considerably longer. However, for efficient execution, a dedicated GPU with VRAM (specified by the model's documentation) is strongly recommended.

While the hardware configuration can be adjusted based on the model size and performance needs, using a GPU significantly accelerates inference processes, reducing execution time drastically compared to CPU-only setups.

It is best practice to install the project in a virtual environment to avoid dependency conflicts:

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate

Installation with PIP (PyPI)
****************************

Schema miner pro is published on PyPI, you can install it directly:

.. code-block:: bash

    pip install schema-miner

This will install the latest stable release along with its dependencies.

Installation from source
************************

To work with the development version or contribute to the project, clone the GitHub repository and install locally:

.. code-block:: bash

    git clone https://github.com/sciknoworg/schema-miner.git
    cd schema-miner
    pip install -r requirements.txt

Configuration
*************

Schema-miner pro is configured from a project-level ``.env`` file. This file
selects the LLM provider and model, stores provider credentials, defines the
scientific process being mined, and points each workflow stage to its input and
output locations. Start from the repository
`.env.example <https://github.com/sciknoworg/schema-miner/blob/main/.env.example>`_
template.

1. Copy the example configuration file into your project root:

.. code-block:: bash

    cp .env.example .env

2. Open ``.env`` and fill in the provider block and workflow paths relevant to
   your run:

.. code-block:: text

    # -- Active LLM provider --
    # Options: OPENAI, SAIA, OLLAMA, HUGGINGFACE, OPENROUTER
    # Use SAIA for any OpenAI-compatible endpoint.
    LLM_PROVIDER = '<Your LLM provider here>'
    LLM_MODEL = '<Your model here>'

    # -- OpenAI --
    OPENAI_API_KEY = 'Your OpenAI API key'
    OPENAI_ORGANIZATION_ID = 'Your OpenAI Organization ID'  # Optional

    # -- SAIA / OpenAI-compatible endpoint --
    SAIA_API_KEY = 'Your API key'
    SAIA_BASE_URL = 'https://chat-ai.academiccloud.de/v1'

    # -- Ollama --
    OLLAMA_BASE_URL = 'OLLAMA Server Base URL'

    # -- Hugging Face --
    HuggingFace_Access_Token = 'HuggingFace access token'
    HUGGINGFACE_USE_LOCAL = False

    # -- OpenRouter --
    OPENROUTER_API_KEY = 'Your OpenRouter API key'
    OPENROUTER_BASE_URL = 'https://openrouter.ai/api/v1'

    # -- Process configuration --
    PROCESS_NAME = 'Your process name here'
    PROCESS_DESCRIPTION = 'Your process description here'

    # -- Data path configuration --
    STAGE1_SPECS_PATH = 'Path to the process specification document for stage 1'
    STAGE2_PAPERS_PATH = 'Path to the directory containing research papers for stage 2'
    STAGE3_PAPERS_PATH = 'Path to the directory containing research papers for stage 3'

    # -- Output path configuration --
    RESULTS_PATH = 'Path to the directory where results will be saved'

``LLM_PROVIDER`` and ``LLM_MODEL`` select the inference backend. ``PROCESS_NAME``
and ``PROCESS_DESCRIPTION`` define the scientific process being mined and are
reused across all stages. The stage-specific path variables point to the input
files for the workflow, while generated schemas, logs, and intermediate outputs
are written under ``RESULTS_PATH``.

Next steps
**********

Once installed and configured, head over to the :doc:`Quickstart <quickstart>` section to run your first schema extraction workflow.
