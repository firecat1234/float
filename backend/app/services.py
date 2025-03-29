import os
import requests
from subprocess import Popen
from time import sleep
from typing import Dict, List, Optional, Any

class ModelContext:
    def __init__(self, system_prompt: str = "", messages: List[Dict[str, str]] = None, tools: List[Dict[str, Any]] = None, metadata: Dict[str, Any] = None):
        self.system_prompt = system_prompt
        self.messages = messages or []
        self.tools = tools or []
        self.metadata = metadata or {}

    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        self.messages.append({
            "role": role,
            "content": content,
            "metadata": metadata or {}
        })

    def add_tool(self, name: str, description: str, parameters: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None):
        self.tools.append({
            "name": name,
            "description": description,
            "parameters": parameters,
            "metadata": metadata or {}
        })

    def set_metadata(self, key: str, value: Any):
        self.metadata[key] = value

    def get_metadata(self, key: str) -> Optional[Any]:
        return self.metadata.get(key)

    def clear(self):
        self.messages = []
        self.tools = []
        self.metadata = {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "system_prompt": self.system_prompt,
            "messages": self.messages,
            "tools": self.tools,
            "metadata": self.metadata
        }

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
        self.context = ModelContext()

    def set_context(self, context: ModelContext):
        """Set the current model context."""
        self.context = context

    def get_context(self) -> ModelContext:
        """Get the current model context."""
        return self.context

    def generate(self, prompt: str, context: Optional[ModelContext] = None, **kwargs):
        """
        Generate text using the selected mode and context.
        Args:
            prompt: The input prompt
            context: Optional ModelContext to use for generation
            **kwargs: Additional generation parameters
        """
        if context:
            self.context = context

        if self.mode == "api":
            return self._generate_via_api(prompt, **kwargs)
        elif self.mode == "local":
            return self._generate_via_local(prompt, **kwargs)
        elif self.mode == "dynamic":
            return self._generate_via_dynamic(prompt, **kwargs)
        else:
            raise ValueError(f"Invalid mode: {self.mode}")

    def _prepare_payload(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Prepare the payload for API requests with context."""
        context_dict = self.context.to_dict()
        return {
            "prompt": prompt,
            "system_prompt": context_dict["system_prompt"],
            "messages": context_dict["messages"],
            "tools": context_dict["tools"],
            "metadata": context_dict["metadata"],
            **kwargs
        }

    def _generate_via_api(self, prompt: str, **kwargs):
        headers = {"Authorization": f"Bearer {self.config['api_key']}"}
        payload = self._prepare_payload(prompt, **kwargs)
        response = requests.post(self.config["api_url"], headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"API error: {response.text}")

    def _generate_via_local(self, prompt: str, **kwargs):
        payload = self._prepare_payload(prompt, **kwargs)
        response = requests.post(f"{self.config['local_url']}/generate", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"Local API error: {response.text}")

    def _generate_via_dynamic(self, prompt: str, **kwargs):
        if not self.dynamic_process:
            self._start_dynamic_server()
        payload = self._prepare_payload(prompt, **kwargs)
        response = requests.post(f"http://localhost:{self.config['dynamic_port']}/api/generate", json=payload)
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
