import os
import requests
from subprocess import Popen
from time import sleep

class LLMService:
    def __init__(self, mode="api", config=None):
        """
        Initialize the LLM service.
        Modes:
        - api: Use external API (e.g., OpenAI)
        - local: Use local API (e.g., LM Studio)
        - dynamic: Deploy and use a dynamic server (e.g., Ollama)
        """
        self.mode = mode
        self.config = config or {
            "api_url": os.getenv("EXTERNAL_API_URL", "https://api.openai.com/v1/completions"),
            "api_key": os.getenv("API_KEY"),
            "local_url": os.getenv("LOCAL_LLM_URL", "http://localhost:11433"),
            "dynamic_model": os.getenv("DYNAMIC_MODEL", "llama"),
            "dynamic_port": int(os.getenv("DYNAMIC_PORT", 11434)),
        }
        self.dynamic_process = None

    def generate(self, prompt: str, **kwargs):
        if self.mode == "api":
            return self._generate_via_api(prompt, **kwargs)
        elif self.mode == "local":
            return self._generate_via_local(prompt, **kwargs)
        elif self.mode == "dynamic":
            return self._generate_via_dynamic(prompt, **kwargs)
        else:
            raise ValueError(f"Invalid mode: {self.mode}")

    def _generate_via_api(self, prompt: str, **kwargs):
        headers = {"Authorization": f"Bearer {self.config['api_key']}"}
        payload = {"prompt": prompt, **kwargs}
        response = requests.post(self.config["api_url"], headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"API error: {response.text}")

    def _generate_via_local(self, prompt: str, **kwargs):
        response = requests.post(f"{self.config['local_url']}/generate", json={"prompt": prompt, **kwargs})
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"Local API error: {response.text}")

    def _generate_via_dynamic(self, prompt: str, **kwargs):
        if not self.dynamic_process:
            self._start_dynamic_server()
        response = requests.post(f"http://localhost:{self.config['dynamic_port']}/api/generate", json={"prompt": prompt, **kwargs})
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"Dynamic server error: {response.text}")

    def _start_dynamic_server(self):
        if self.dynamic_process:
            return  # Server already running

        print("Starting dynamic server...")
        self.dynamic_process = Popen(
            ["ollama", "serve", "--model", self.config["dynamic_model"], "--port", str(self.config["dynamic_port"])],
            stdout=open("ollama_stdout.log", "w"),
            stderr=open("ollama_stderr.log", "w"),
        )
        sleep(3)  # Wait for the server to start

    def stop_dynamic_server(self):
        if self.dynamic_process:
            self.dynamic_process.terminate()
            self.dynamic_process = None
            print("Dynamic server stopped.")
