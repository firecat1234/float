import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        "api_url": os.getenv("EXTERNAL_API_URL"),
        "api_key": os.getenv("API_KEY"),
        "local_url": os.getenv("LOCAL_LLM_URL"),
        "dynamic_model": os.getenv("DYNAMIC_MODEL"),
        "dynamic_port": os.getenv("DYNAMIC_PORT"),
    }
