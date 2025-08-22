"""
This module provides configuration settings for the application.
"""

import os
from dotenv import load_dotenv

load_dotenv()
# Hugging Face access token
HF_TOKEN = os.environ.get("HF_TOKEN")

# LLM model repo ID
HF_REPO_ID = "zai-org/GLM-4.5:novita"
print(f"Using Hugging Face repo ID: {HF_REPO_ID}")

# Embeddings model
HF_EMBEDDINGS_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# FAISS vector DB location
DB_FAISS_PATH = "vectorstore/db_faiss"

# Directory for input documents
DATA_DIR = "data/"

# Number of characters per document chunk
CHUNK_SIZE = 600

# Number of overlapping characters between chunks
CHUNK_OVERLAP = 100
