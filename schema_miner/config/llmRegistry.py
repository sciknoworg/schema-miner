from schema_miner.services.LLM_Inference.LLM_inference import LLM_Inference
from schema_miner.services.LLM_Inference.openai_llm_inference import Openai_LLM_Inference
from schema_miner.services.LLM_Inference.ollama_llm_inference import OLLAMA_LLM_Inference
from schema_miner.services.LLM_Inference.saia_llm_inference import SAIA_LLM_Inference
from schema_miner.services.LLM_Inference.huggingface_llm_inference import HuggingFace_LLM_Inference

class LLMRegistry:
    #Dictionary containing the class mapping for different LLM types
    llm_type_mappings = {
        'gpt-4o': Openai_LLM_Inference,
        'gpt-4-turbo': Openai_LLM_Inference,
        'gpt-5': Openai_LLM_Inference,
        'meta-llama-3.1-8b-instruct': SAIA_LLM_Inference,
        'meta-llama-3.1-70b-instruct': SAIA_LLM_Inference,
        'Qwen/Qwen2.5-0.5B-Instruct': HuggingFace_LLM_Inference
    }

    default_llm_inference_fallback = OLLAMA_LLM_Inference

    @classmethod
    def get_llm_Inference_cls(cls, llm_model_name: str) -> LLM_Inference:
        """
        Retrieve the LLM inference class corresponding to the given model name.
        
        :param str llm_model_name: The name of the Large Language Model(LLM)
        :return LLM_Inference: The inference class associated with the provided LLM name.
        """
        return cls.llm_type_mappings.get(llm_model_name, cls.default_llm_inference_fallback)