from typing import Type

from schema_miner.config.envConfig import EnvConfig

from schema_miner.services.LLM_Inference.huggingface_llm_inference import HuggingFace_LLM_Inference
from schema_miner.services.LLM_Inference.LLM_inference import LLM_Inference
from schema_miner.services.LLM_Inference.ollama_llm_inference import OLLAMA_LLM_Inference
from schema_miner.services.LLM_Inference.openai_llm_inference import Openai_LLM_Inference
from schema_miner.services.LLM_Inference.saia_llm_inference import SAIA_LLM_Inference


class LLMRegistry:
    # Dictionary containing the class mapping for different LLM types
    llm_provider_mappings = {
        "openai": Openai_LLM_Inference,
        "saia": SAIA_LLM_Inference,
        "huggingface": HuggingFace_LLM_Inference,
        "ollama": OLLAMA_LLM_Inference,
    }

    default_llm_inference_fallback = OLLAMA_LLM_Inference

    @classmethod
    def get_llm_Inference_cls(cls) -> Type[LLM_Inference]:
        """
        Retrieve the LLM inference class based on the LLM model name and LLM provider specified in the environment configuration.
        
        :return LLM_Inference: The inference class associated with the LLM model and provider specified in the environment configuration.
        """
        return cls.llm_provider_mappings.get(EnvConfig.LLM_PROVIDER.lower(), cls.default_llm_inference_fallback)