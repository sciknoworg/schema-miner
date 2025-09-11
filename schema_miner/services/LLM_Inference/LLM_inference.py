import logging

from langchain_core.prompts import ChatPromptTemplate

from schema_miner.config.envConfig import EnvConfig

class LLM_Inference:
    """
    LLM_Inference is a super class for doing LLM inference using different Large Language Models(LLMs).
    """

    def __init__(self):
        """
        Initialize the object and reads the configuration file
        """

        #Reading the Config File
        self.config = EnvConfig

        # Initialize the logger
        self.logger = logging.getLogger(__name__)

    def format_prompt_template(self, prompt_template, var_dict: dict):
        """
        Takes the prompt template and variable dictionary to format the final prompt to be given to the LLM

        :param prompt_template: The prompt template with placeholders for dynamic values.
        :param dict var_dict: The dictionary containing variable name and its corresponding value to format the prompt.
        :returns prompt: The formatted prompt
        """
        #Creating the chat prompt template using Langchain
        chat_prompt_template = ChatPromptTemplate.from_messages([
            ('system', prompt_template.system_prompt),
            ('user', prompt_template.user_prompt),
        ])

        #Replacing the placeholders in the prompt with its value
        prompt = chat_prompt_template.invoke(var_dict)

        #Returning the formatted prompt
        return prompt

    def completion(self, prompt_template, var_dict):
        pass