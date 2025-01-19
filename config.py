import os
from pathlib import Path
import logging
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Base paths
    BASE_DIR = Path(__file__).parent
    DOCUMENTS_DIR = BASE_DIR / "documents"
    DATA_DIR = BASE_DIR / "data"
    
    # Vector store settings
    VECTOR_DIMENSION = 384
    INDEX_FILE = DATA_DIR / "faiss_index.bin"
    DOCUMENT_MAPPINGS_FILE = DATA_DIR / "document_mappings.json"
    
    # Groq settings
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # Document processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # Retrieval settings
    TOP_K_DOCUMENTS = 5
    
    @staticmethod
    def setup_logging():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )