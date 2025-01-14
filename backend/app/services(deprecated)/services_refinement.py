# services_refinement.py for easy access to tools

from typing import List, Dict
from services.data_service import DataService
from services.memory_service import MemoryService
from services.llm_service import LLMService
from services.tool_service import ToolService

class RefinedServices:
    def __init__(self):
        self.data_service = DataService()
        self.memory_service = MemoryService()
        self.llm_service = LLMService()
        self.tool_service = ToolService()

    def embed_and_store(self, content: Dict) -> Dict:
        """
        Handles embedding of content and stores it in memory or database.
        Input schema:
        {
            "text": str,  # Text to embed
            "metadata": Dict  # Additional metadata for the content
        }
        """
        text = content.get("text")
        metadata = content.get("metadata", {})

        if not text:
            return {"status": "error", "message": "No text provided for embedding."}

        # Embed the text (mocked for now)
        embedding = [0.1, 0.2, 0.3]  # Placeholder for embedding logic
        embedded_content = {"embedding": embedding, "metadata": metadata}

        # Store in memory or database
        self.memory_service.store(embedded_content)
        return {"status": "success", "message": "Content embedded and stored."}

    def retrieve_with_embeddings(self, query: str) -> List[Dict]:
        """
        Retrieves data from memory or database using embeddings.
        """
        results = self.memory_service.retrieve_long(query)
        return results

    def schedule_task(self, task: Dict) -> Dict:
        """
        Schedules a task via the tool service.
        Input schema:
        {
            "tool_id": str,  # ID of the tool to execute
            "parameters": Dict  # Parameters for the tool
        }
        """
        tool_id = task.get("tool_id")
        parameters = task.get("parameters", {})

        if not tool_id or tool_id not in self.tool_service.tools:
            return {"status": "error", "message": "Invalid or missing tool_id."}

        try:
            result = self.tool_service.call_tool(tool_id, **parameters)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def generate_response(self, prompt: str) -> Dict:
        """
        Generates a response using the LLM service.
        """
        if not prompt:
            return {"status": "error", "message": "No prompt provided."}

        response = self.llm_service.generate_text(prompt)
        return {"status": "success", "response": response}
