from fastapi import FastAPI
from .routes import router  # Import the router
from .config import load_config  # Import your configuration function

app = FastAPI()

# Load configurations.
config = load_config()
app.state.config = config  # Attach the loaded configuration to the application

app.include_router(router) # Include routes defined in routes.py

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # start the API server

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust based on security requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .services import MemoryManager, RAGHandler

memory_manager = MemoryManager(config)
rag_handler = RAGHandler(config)

app.state.memory_manager = memory_manager
app.state.rag_handler = rag_handler


#add a route to initialize and monitor this functionality
