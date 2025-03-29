from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Union


class Message(BaseModel):
    role: str
    content: str
    metadata: Optional[Dict[str, Any]] = None

class Tool(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None

class ModelContext(BaseModel):
    system_prompt: str = ""
    messages: List[Message] = []
    tools: List[Tool] = []
    metadata: Dict[str, Any] = {}

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None  # Add session tracking
    use_rag: Optional[bool] = True
    patience: Optional[int] = 1
    context: Optional[ModelContext] = None

class ChatResponse(BaseModel):
    message: str
    thought: Optional[str] = None
    tools_used: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    context: Optional[ModelContext] = None

class ErrorResponse(BaseModel):
    error: str
    details: Optional[Dict[str, Any]]

