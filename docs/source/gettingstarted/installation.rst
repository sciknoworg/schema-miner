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

Configuration of API keys
*************************

Schema-miner pro uses large language models (LLMs) that require API access (e.g., OpenAI). API keys and other secrets are managed either via a .env file at the project root or with the EnvConfig Class.

Configuration Using ``.env``
----------------------------

1. Copy the example configuration file:

.. code-block:: bash

    cp .env.example .env

2. Open .env in a text editor and add your keys:

.. code-block:: bash

    OPENAI_API_KEY = 'Your OpenAI API key'
    OPENAI_ORGANIZATION_ID = 'Your OpenAI Organization ID'

3. Schema-miner automatically loads these values at runtime using the provided configuration utilities.

Configuration Using ``EnvConfig``
---------------------------------

.. code-block:: python

    from schema_miner.config.envConfig import EnvConfig

    # OpenAI Keys
    EnvConfig.OPENAI_api_key = '<insert-your-openai-key>'
    EnvConfig.OPENAI_organization_id = '<insert-your-openi-organization-id>'

    # Ollama
    EnvConfig.OLLAMA_base_url = '<Ollama Base URL or empty if Ollama running locally>'

    # HuggingFace
    EnvConfig.HUGGINGFACE_access_token = '<Your huggingface access token>'

Next steps
**********

Once installed and configured, head over to the :doc:`Quickstart <quickstart>` section to run your first schema extraction workflow.
