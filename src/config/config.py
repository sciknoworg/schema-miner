import os
from dotenv import load_dotenv

class Config:

    #Loading the environment file
    load_dotenv()

    #OPENAI
    OPENAI_api_key = os.getenv('OPENAI_API_KEY')
    OPENAI_organization_id = os.getenv('OPENAI_ORGANIZATION_ID')

    #SAIA
    SAIA_api_key = os.getenv('SAIA_API_KEY')
    SAIA_base_url = os.getenv('SAIA_BASE_URL')
    SAIA_num_retry = 5

    #OLLAMA
    OLLAMA_base_url = os.getenv('OLLAMA_BASE_URL')
    OLLAMA_context_length = 32768