import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        "api_url": os.getenv("EXTERNAL_API_URL", "https://api.openai.com/v1/completions"),
        "api_key": os.getenv("API_KEY", ""),
        "local_url": os.getenv("LOCAL_LLM_URL", "http://localhost:11433"), #maybe 1234 unless its proxied
        "dynamic_model": os.getenv("DYNAMIC_MODEL", "mistral"),
        "dynamic_port": int(os.getenv("DYNAMIC_PORT", "11434")),
    }
