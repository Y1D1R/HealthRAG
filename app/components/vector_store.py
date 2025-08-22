"""
This module provides functionality to load and create a vector store.
"""

import os
import logging
from langchain_community.vectorstores import FAISS

from app.components.embeddings import get_embeddings_model
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DB_FAISS_PATH


logging.getLogger("faiss").setLevel(logging.WARNING)

logger = get_logger(__name__)


def load_vector_store():
    """
    FAISS ==> Library for efficient similarity search and clustering of dense vectors.
    Load the vector store from the specified path.

    Returns:
        FAISS or None: The loaded FAISS vector store or None if not found.
    """
    try:
        logger.info("Loading vector store from: %s", DB_FAISS_PATH)
        embeddings_model = get_embeddings_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Vector store found, loading...")
            vector_store = FAISS.load_local(
                DB_FAISS_PATH, embeddings_model, allow_dangerous_deserialization=True
            )
            logger.info("Vector store loaded successfully")
            return vector_store

        logger.warning("Vector store not found at: %s", DB_FAISS_PATH)
        return None

    except Exception as e:
        error_msg = CustomException("Failed to load vector store", e)
        logger.error(str(error_msg))
        raise error_msg from e


def create_vector_store(text_chunks):
    """
    Create and save a new vector store to the specified path.

    Args:
        text_chunks (list): List of documents to embed and store.

    Returns:
        FAISS: The created vector store.
    """
    try:
        if not text_chunks:
            logger.warning("No text chunks provided. Vector store will not be created.")
            raise CustomException("No text chunks provided for vector store creation.")

        logger.info("Generating a new vector store")
        db = FAISS.from_documents(text_chunks, get_embeddings_model())
        db.save_local(DB_FAISS_PATH)
        logger.info("Vector store created and saved successfully at: %s", DB_FAISS_PATH)
        return db

    except Exception as e:
        error_msg = CustomException("Failed to create a new vector store", e)
        logger.error(str(error_msg))
        raise error_msg from e
