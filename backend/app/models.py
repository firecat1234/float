from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None  # Add session tracking
    use_rag: Optional[bool] = True
    patience: Optional[int] = 1

class ChatResponse(BaseModel):
    message: str
    thought: Optional[str] = None
    tools_used: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class ErrorResponse(BaseModel):
    error: str
    details: Optional[Dict[str, Any]]

