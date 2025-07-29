import os

# Hugging Face access token
HF_TOKEN = os.environ.get("HF_TOKEN")

# LLM model repo ID
HF_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

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