from langchain_huggingface import HuggingFaceEmbeddings
from app.config.config import HF_EMBEDDINGS_MODEL

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)


def get_embeddings_model():
    """
    Get the embeddings model from HuggingFace.
    """
    try:
        logger.info(f"Initializing embedding model: {HF_EMBEDDINGS_MODEL}")
        model = HuggingFaceEmbeddings(model_name=HF_EMBEDDINGS_MODEL)
        logger.info(f"Embedding model loaded successfully")
        return model
    
    except Exception as e:
        error_msg= CustomException(f"Failed to load embedding model", e)
        logger.error(str(error_msg))  
        raise error_msg  
