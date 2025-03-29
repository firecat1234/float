from fastapi import APIRouter, HTTPException, Request
from app.services import LLMService, ModelContext
from app.models import ChatRequest, ChatResponse
from app.schemas import MemoryUpdateRequest
from typing import Dict, Any, Optional, List

router = APIRouter()
llm_service = LLMService()

@router.post("/context/")
async def create_context(system_prompt: str = "", messages: Optional[List[Dict[str, str]]] = None, tools: Optional[List[Dict[str, Any]]] = None, metadata: Optional[Dict[str, Any]] = None):
    """
    Create a new model context.
    """
    context = ModelContext(system_prompt=system_prompt, messages=messages, tools=tools, metadata=metadata)
    llm_service.set_context(context)
    return {"status": "success", "context": context.to_dict()}

@router.post("/context/{context_id}/message")
async def add_message(context_id: str, role: str, content: str, metadata: Optional[Dict[str, Any]] = None):
    """
    Add a message to the context.
    """
    context = llm_service.get_context()
    context.add_message(role, content, metadata)
    return {"status": "success", "context": context.to_dict()}

@router.post("/context/{context_id}/tool")
async def add_tool(context_id: str, name: str, description: str, parameters: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None):
    """
    Add a tool to the context.
    """
    context = llm_service.get_context()
    context.add_tool(name, description, parameters, metadata)
    return {"status": "success", "context": context.to_dict()}

@router.post("/context/{context_id}/metadata")
async def set_metadata(context_id: str, key: str, value: Any):
    """
    Set metadata in the context.
    """
    context = llm_service.get_context()
    context.set_metadata(key, value)
    return {"status": "success", "context": context.to_dict()}

@router.get("/context/{context_id}")
async def get_context(context_id: str):
    """
    Get the current context.
    """
    context = llm_service.get_context()
    return {"status": "success", "context": context.to_dict()}

@router.delete("/context/{context_id}")
async def clear_context(context_id: str):
    """
    Clear the current context.
    """
    context = llm_service.get_context()
    context.clear()
    return {"status": "success", "message": "Context cleared"}

@router.post("/llm/generate")
async def generate(prompt: str, mode: str = "api", context: Optional[ModelContext] = None):
    """
    Generate text using the selected mode and context.
    Modes: api, local, dynamic
    """
    try:
        llm_service.mode = mode
        if context:
            llm_service.set_context(context)
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
    Endpoint for handling chat messages with context support.
    """
    try:
        # Create or get context
        context = llm_service.get_context()
        
        # Add user message to context
        context.add_message("user", chat_request.message)
        
        # Generate response
        response = llm_service.generate(chat_request.message)
        
        # Add assistant response to context
        context.add_message("assistant", response.get("text", ""))
        
        return ChatResponse(
            message=response.get("text", ""),
            thought=response.get("thought", ""),
            tools_used=response.get("tools_used", []),
            metadata=response.get("metadata", {})
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/memory/update/")
async def update_memory(request: Request, update_request: MemoryUpdateRequest):
    """
    Updates memory with the given key-value pair.
    """
    # Use the Request object to access the app state
    result = request.app.state.memory_manager.update_memory(update_request.dict())
    return {"status": "success", "updated": result}

@router.get("/tools/")
async def get_tools(request: Request):
    """
    Returns the list of available tools.
    """
    return {"tools": request.app.state.memory_manager.list_tools()}