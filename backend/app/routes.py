from fastapi import APIRouter
from .models import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat/", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    """
    Endpoint for handling chat messages.
    """
    # Placeholder, implement logic to interact with the agent/model
    response = ChatResponse(message="This is a placeholder response", thought="Thinking...") 
    return response

@router.get("/tools/")
async def get_tools():
    """
    Returns the list of available tools.
    """
    return {"tools": app.state.memory_manager.list_tools()}

#validate inputs - use fastapi's validation system to check the schema during runtime

@router.post("/memory/update/")
async def update_memory(update_request: MemoryUpdateRequest):
    result = app.state.memory_manager.update_memory(update_request)
    return {"status": "success", "updated": result}
