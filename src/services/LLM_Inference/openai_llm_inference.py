import os

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from services.LLM_Inference.LLM_inference import LLM_Inference

class Openai_LLM_Inference(LLM_Inference):
    """
    Openai_LLM_Inference is a subclass of LLM_Inference which has a task of doing inference from the specific Large Language Model(LLM) 
    giving a specified prompt.
    """

    def __init__(self, model_name: str, temperature: float = 0.3):
        """
        Initialize the object with OpenAI configuration (API Key, Organization ID, Model name etc.)
        """
        super().__init__()

        #API Key of OpenAI
        self.api_key = self.config.OPENAI_api_key
        os.environ['OPENAI_API_KEY'] = self.api_key

        #Organization ID of OpenAI
        self.organization_id = self.config.OPENAI_organization_id
        os.environ['OPENAI_ORGANIZATION'] = self.organization_id

        #Response Format
        self.response_format = self.config.OPENAI_response_format

        #OpenAI LLM Temperature
        self.temperature = temperature

        #The Large Language Model to use for Inference
        self.model_name = model_name
        self.model = ChatOpenAI(model = model_name, temperature = self.temperature, model_kwargs={'response_format': {'type': self.response_format}})

    def __str__(self):
        """
        Returns a human-readable representation of an object
        """
        return f'OPENAI - LLM Inference with Model: {self.model_name}'

    def completion(self, prompt_template, var_dict: dict):
        """
        Call the completion API of the OpenAI model with the formatted prompt. Returns the parsed output from the model.

        :param prompt_template: The prompt template with placeholders for dynamic values.
        :param dict var_dict: The dictionary containing variable name and its corresponding value to format the prompt.
        :returns model_output: The parsed LLM output
        """
        try:
            #Formatting the prompt
            prompt = self.format_prompt_template(prompt_template, var_dict)
            
            #Invoking the model's completion API with the prompt
            model_output = self.model.invoke(prompt.to_messages())

            #Parsing the LLM's output to extract the final output
            model_output = StrOutputParser().invoke(model_output)

            #Returns the LLM's output
            return model_output
        except Exception as e:
            print(f'Exception Occurred while calling the Completion API of model: {self.model_name}')
            print(f'Exception: {e}')
            return None
        