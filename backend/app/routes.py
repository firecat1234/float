from fastapi import APIRouter, HTTPException
import app.services as services

router = APIRouter()
llm_service = LLMService()

@router.post("/llm/generate")
async def generate(prompt: str, mode: str = "api"):
    """
    Generate text using the selected mode.
    Modes: api, local, dynamic
    """
    try:
        llm_service.mode = mode
        response = llm_service.generate(prompt)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/llm/start-dynamic")
async def start_dynamic_server():
    """
    Start the dynamic LLM server.
    """
    try:
        llm_service._start_dynamic_server()
        return {"status": "success", "message": "Dynamic server started."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/llm/stop-dynamic")
async def stop_dynamic_server():
    """
    Stop the dynamic LLM server.
    """
    try:
        llm_service.stop_dynamic_server()
        return {"status": "success", "message": "Dynamic server stopped."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat/", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    """
    Endpoint for handling chat messages.
    """
    response = ChatResponse(
        message="This is a placeholder response",
        thought="Thinking..."
    )
    return response

@router.post("/memory/update/")
async def update_memory(update_request: MemoryUpdateRequest):
    """
    Updates memory with the given key-value pair.
    """
    result = app.state.memory_manager.update_memory(
        {"key": update_request.key, "value": update_request.value}
    )
    return {"status": "success", "updated": result}

@router.get("/tools/")
async def get_tools():
    """
    Returns the list of available tools.
    """
    return {"tools": app.state.memory_manager.list_tools()}
