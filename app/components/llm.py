"""
This module provides functionality to work with the LLM.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN")
HF_REPO_ID = os.environ.get("HF_REPO_ID", "zai-org/GLM-4.5:novita")


class HuggingFaceRouterWrapper:
    """
    Wrapper for Hugging Face Router API calls.
    """

    def __init__(self, model: str, hf_token: str):
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=hf_token,
        )
        self.model = model

    def invoke(self, prompt: str) -> str:
        """
        Invoke the Hugging Face Router API with the given prompt.
        """
        try:
            logger.info("Calling Hugging Face Router API with model: %s", self.model)
            response = self.client.chat.completions.create(
                model=self.model, messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise CustomException("HF router API call failed", e) from e


def load_llm():
    """
    Load the HuggingFace Router LLM.
    """
    try:
        logger.info("Initializing HuggingFace Router LLM...")
        return HuggingFaceRouterWrapper(model=HF_REPO_ID, hf_token=HF_TOKEN)
    except Exception as e:
        raise CustomException("Failed to initialize HuggingFace router-based LLM", e) from e
