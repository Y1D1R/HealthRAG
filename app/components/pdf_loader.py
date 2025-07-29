import os
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdfs_from_directory():
    """
    Load all PDF files from a specified directory and split them into chunks.
    
    """
    try:
        if not os.path.exists(DATA_DIR):
            raise CustomException(f"Data directory '{DATA_DIR}' does not exist.")
        
        logger.info(f"Loading PDF documents from directory: {DATA_DIR}")
        loader = DirectoryLoader(DATA_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        
        if not documents:
            raise CustomException(f"No PDF documents found in the specified DATA directory: {DATA_DIR}")
        else:
            logger.info(f"Found {len(documents)} PDF documents in the DATA directory: {DATA_DIR}")

        return documents
    
    except Exception as e:
        error_msg = CustomException("Failed to load PDF documents", e)
        logger.error(str(error_msg))
        return []
        
        
        
def split_documents_into_chunks(documents):
    """
    Split documents into smaller chunks for processing.
    
    Args:
        documents (list): A list of documents to be split.
    
    Returns:
        list: A list of document chunks.
    """
    try:
        if not documents:
            raise CustomException("No documents provided to split into chunks.")
        
        logger.info(f"Received {len(documents)} documents to split into chunks.")
        
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
        
        chunks = text_splitter.split_documents(documents)
        
        logger.info(f"{len(documents)} Documents splitted into {len(chunks)} Chunks.")
        return chunks
    
    except Exception as e:
        error_msg = CustomException("Failed to split documents into chunks", e)
        logger.error(str(error_msg))
        return []