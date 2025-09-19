from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

from schema_miner.services.LLM_Inference.LLM_inference import LLM_Inference


class OLLAMA_LLM_Inference(LLM_Inference):
    """
    OLLAMA_LLM_Inference is a subclass of LLM_Inference which has a task of doing inference on specified Open source
    Large Language Model(LLM) running locally using the Ollama with a specified prompt.
    """

    def __init__(self, model_name: str, temperature: float = 0.3):
        """
        Initialize the object with Ollama configuration (Model name etc.)
        """
        super().__init__(model_name=model_name, temperature=temperature)

        # Base URL for OLLAMA Server
        self.base_url = self.config.OLLAMA_base_url

        # Context length for the model
        self.context_length = self.config.OLLAMA_context_length

        # Response Format
        self.response_format = self.config.OLLAMA_response_format

        # The Large Language Model to use for Inference
        self.model = OllamaLLM(
            base_url=None,
            model=self.model_name,
            num_ctx=self.context_length,
            temperature=self.temperature,
            format=self.response_format,
        )

    def __str__(self):
        """
        Returns a human-readable representation of an object
        """
        return f"OLLAMA - LLM Inference with Model: {self.model_name}"

    def completion(self, prompt_template, var_dict):
        """
        Requests the completion endpoint of the Ollama with the specified prompt/message. Returns the parsed output from the model.

        :param prompt_template: The prompt template with placeholders for dynamic values.
        :param dict var_dict: The dictionary containing variable name and its corresponding value to format the prompt.
        :returns model_output: The parsed LLM output
        """

        try:
            # Formatting the prompt
            prompt = super().format_prompt_template(prompt_template, var_dict)

            # Invoking the model's completion API with the prompt
            model_output = self.model.invoke(prompt.to_messages())

            # Parsing the LLM's output to extract the final output
            model_output = StrOutputParser().invoke(model_output)

            # Returns the LLM's output
            return model_output
        except Exception as e:
            self.logger.debug(
                f"Exception Occurred while calling the Completion API of model: {self.model_name}"
            )
            self.logger.debug(f"Exception: {e}")
            return None
