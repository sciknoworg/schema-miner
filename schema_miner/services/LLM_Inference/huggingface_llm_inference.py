import os

from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser

from schema_miner.services.LLM_Inference.LLM_inference import LLM_Inference

class HuggingFace_LLM_Inference(LLM_Inference):
    """
    HuggingFace_LLM_Inference is a subclass of LLM_Inference which has a task of doing inference from the specific Large Language Model(LLM) giving a specified prompt.
    """

    def __init__(self, model_name: str):
        """
        Initialize the object with HuggingFace configuration (Model name etc.)
        """
        super().__init__()

        #HuggingFace Access Token
        self.access_token = self.config.HUGGINGFACE_access_token
        os.environ['HUGGINGFACEHUB_API_TOKEN'] = self.access_token

        #The Large Language Model to use for Inference
        self.model_name = model_name
        self.model = HuggingFaceEndpoint(
            repo_id = self.model_name,
            task = "text-generation",
            max_new_tokens = 1024,
            temperature = 0.3,
            truncate = True
        )

    def __str__(self):
        """
        Returns a human-readable representation of an object
        """
        return f'HuggingFace - LLM Inference with Model: {self.model_name}'
    
    def completion(self, prompt_template, var_dict):
        """
        Requests the completion endpoint of the HuggingFace with the specified prompt/message. Returns the parsed output from the model.

        :param prompt_template: The prompt template with placeholders for dynamic values.
        :param dict var_dict: The dictionary containing variable name and its corresponding value to format the prompt.
        :returns model_output: The parsed LLM output
        """
        try:
            #Formatting the prompt
            prompt = super().format_prompt_template(prompt_template, var_dict)
            
            #Invoking the model's completion API with the prompt
            model_output = self.model.invoke(prompt.to_messages())

            #Parsing the LLM's output to extract the final output
            model_output = StrOutputParser().invoke(model_output)

            #Returns the LLM's output
            return model_output
        except Exception as e:
            self.logger.debug(f'Exception Occurred while calling the Completion API of model: {self.model_name}')
            self.logger.debug(f'Exception: {e}')
            return None