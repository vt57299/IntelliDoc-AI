from dotenv import load_dotenv
import os

load_dotenv() 

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    CHUNK_SIZE = 500
    OVERLAP = 100
    VECTOR_DB_PATH = "data/vectorstore"
    METADATA_FILE = "data/metadata.json"

settings = Settings()
