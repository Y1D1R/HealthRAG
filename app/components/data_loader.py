"""
This module provides functionality to load data and create a vector store.
"""

from app.components.pdf_loader import (
    load_pdfs_from_directory,
    split_documents_into_chunks,
)
from app.components.vector_store import create_vector_store, load_vector_store

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)


def load_data_and_create_vector_store():
    """
    Loads PDF documents, splits them into chunks, and creates a new FAISS vector store.

    Returns:
        The created vector store.
    """

    try:
        logger.info("Starting vector store creation...")

        # Step 1: Load PDF documents
        documents = load_pdfs_from_directory()

        # Step 2: Split documents into chunks
        text_chunks = split_documents_into_chunks(documents)

        # Step 3: Create a new vector store
        vector_store_db = create_vector_store(text_chunks)
        print("Vector store created successfully.", len(vector_store_db))

        logger.info("Vector store created successfully.")
    except Exception as e:
        loading_error = CustomException("Failed to load data and create vector store", e)
        logger.error(str(loading_error))
        raise loading_error from e


if __name__ == "__main__":
    try:
        # Load existing vector store if available
        vector_store = load_vector_store()
        if vector_store is None:
            logger.info("No existing vector store found ==> Creating a new one.")
            load_data_and_create_vector_store()
        else:
            logger.info("Existing vector store loaded successfully.")
    except Exception as e:
        error_msg = CustomException(
            "An unexpected error occurred in main execution of data_loader :", e
        )
        logger.error(str(error_msg))
        raise error_msg from e
