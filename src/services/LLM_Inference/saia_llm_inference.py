from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from services.LLM_Inference.LLM_inference import LLM_Inference

class SAIA_LLM_Inference(LLM_Inference):
    """
    SAIA_LLM_Inference is a subclass of LLM_Inference which has a task of doing inference from the specific Open source 
    Large Language Model(LLM) giving a specified prompt.
    """

    def __init__(self, model_name: str):
        """
        Initialize the object with SAIA configuration (Base URL, API Key, Model name etc.)
        """
        super().__init__()
        
        #Base URL of the Scalable AI Accelerator (SAIA) platform
        self.base_url = self.config.SAIA_base_url

        #API Key of the SAIA Chat AI
        self.api_key = self.config.SAIA_api_key
        
        #Number of retry if model returns any error
        self.num_retry = self.config.SAIA_num_retry

        #Response Format
        self.response_format = self.config.SAIA_response_format

        #The Large Language Model to use for Inference
        self.model_name = model_name
        self.model = ChatOpenAI(base_url = self.base_url, api_key = self.api_key, model = model_name, temperature = 0.3, model_kwargs={'response_format': {'type': self.response_format}})

    def __str__(self):
        """
        Returns a human-readable representation of an object
        """
        return f'SAIA - LLM Inference with Model: {self.model_name}'

    def completion(self, prompt_template, var_dict: dict):
        """
        Requests the completion endpoint of the SAIA service with the specified prompt/message. Returns the parsed output from the model.

        :param prompt_template: The prompt template with placeholders for dynamic values.
        :param dict var_dict: The dictionary containing variable name and its corresponding value to format the prompt.
        :returns model_output: The parsed LLM output
        """

        #Initializing model output
        model_output = None

        #Resetting number of retry count
        self.num_retry = self.config.SAIA_num_retry
        
        #Iterating until we get a response from the model or the number of retry is exhausted
        while not model_output:
            try:
                #Formatting the prompt
                prompt = super().format_prompt_template(prompt_template, var_dict)
                
                #Invoking the model's completion API with the prompt
                model_output = self.model.invoke(prompt.to_messages())

                #Parsing the LLM's output to extract the final output
                model_output = StrOutputParser().invoke(model_output)
            except Exception as e:
                print(f'Exception Occurred while calling the Completion API of model: {self.model_name}')
                print(f'Exception: {e}')
                
                #Checking if number of retry's are left, otherwise returning from the method
                if self.num_retry > 0:
                    self.num_retry -= 1
                    print(f'Retrying again with the same prompt, current retry count: {self.num_retry}')
                else:
                    print('Number of retry is finished, returning from the model')
                    break

        #Returns the LLM's output
        return model_output