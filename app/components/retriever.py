from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.vector_store import load_vector_store
from app.components.llm import load_llm

from app.config.config import HF_REPO_ID,HF_TOKEN

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

logger = get_logger(__name__)

CUSTOM_PROMPT = """ 
You are a professional medical assistant. You must reply concisely and directly to the user's question using only the context.

⚠️ Do NOT explain your thought process.  
⚠️ Do NOT analyze the question or the context.  
⚠️ Do NOT repeat the question.  
⚠️ Do NOT mention what you can or cannot do.  
⚠️ DO NOT say things like "the user is asking..." or "the context says..."

Respond in **2 to 3 complete sentences** ONLY, and provide the answer **based purely on the context**.

Context:
{context}

Question:
{user_input}

Answer:
"""

def set_custom_prompt():
    """
    Sets a custom prompt for the RetrievalQA chain.
    """
    return PromptTemplate( template=CUSTOM_PROMPT, input_variables=["context", "question"])
    
def create_retrieval_qa_chain():
    """
    Prepares the retriever and LLM for manual prompting.
    Returns:
        tuple: (vector_store, llm)
    """
    try:
        logger.info("Loading vector store...")
        vector_store_db = load_vector_store()
        if vector_store_db is None:
            raise CustomException("Vector store not loaded properly (missing or empty).")

        logger.info("Loading LLM...")
        llm = load_llm()
        if llm is None:
            raise CustomException("LLM not loaded properly.")

        logger.info("Retriever and LLM loaded successfully.")
        return vector_store_db, llm

    except Exception as e:
        error_msg = CustomException("Failed to prepare retriever and LLM", e)
        logger.error(str(error_msg))
        raise error_msg