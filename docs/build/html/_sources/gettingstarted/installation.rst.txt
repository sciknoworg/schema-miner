Installation
============

System Requirements
*******************

The computational requirements for running this project vary depending on the model being used. If utilizing OpenAI models such as `GPT-4o <https://platform.openai.com/docs/models#gpt-4o>`_ and `GPT-4-turbo <https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4>`_, no specialized hardware is needed since inference is performed via API calls. A basic system with a stable internet connection is sufficient for executing API-based workflow.

For users opting to run **open-source models** such as `Llama 3.1 8B <https://ai.meta.com/blog/meta-llama-3-1/>`_ or other large-scale transformer-based models, local execution demands significantly higher computational resources. While these models can be executed on a CPU, inference times will be considerably longer. However, for efficient execution, a dedicated GPU with VRAM (specified by the model's documentation) is strongly recommended.

While the hardware configuration can be adjusted based on the model size and performance needs, using a GPU significantly accelerates inference processes, reducing execution time drastically compared to CPU-only setups.

Installation with PIP
*********************

Install all the necessary Python packages listed in the `requirements.txt <https://github.com/sciknoworg/schema-miner/blob/main/requirements.txt>`_ file.

.. code-block:: bash
    
    pip install -r requirements.txt