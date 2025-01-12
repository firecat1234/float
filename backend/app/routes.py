from fastapi import APIRouter, Depends
from .models import ChatRequest, ChatResponse
from .schemas import MemoryUpdateRequest

router = APIRouter()

@router.post("/chat/", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    """
    Endpoint for handling chat messages.
    """
    # Placeholder, implement logic to interact with the agent/model
    response = ChatResponse(
        message="This is a placeholder response", 
        thought="Thinking..."
    )
    return response

@router.post("/memory/update/")
async def update_memory(update_request: MemoryUpdateRequest, app=Depends()):
    """
    Updates memory with the given key-value pair.
    """
    result = app.state.memory_manager.update_memory(
        {"key": update_request.key, "value": update_request.value}
    )
    return {"status": "success", "updated": result}

@router.get("/tools/")
async def get_tools(app=Depends()):
    """
    Returns the list of available tools.
    """
    tools = app.state.memory_manager.list_tools()
    return {"tools": tools}
