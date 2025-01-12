from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .routes import router  # Import the router
from .config import load_config  # Import your configuration function
from .services import MemoryManager, RAGHandler

# Initialize FastAPI
app = FastAPI()

# Health Check
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}

# Root Route
@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}

# Load configurations
try:
    config = load_config()
    app.state.config = config  # Attach the loaded configuration to the application
except Exception as e:
    print(f"Error loading configuration: {e}")
    raise

# Add Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust based on security requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging Middleware (Optional)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    print(f"Request: {request.method} {request.url} - Status: {response.status_code}")
    return response

# Initialize services
memory_manager = MemoryManager(config)
rag_handler = RAGHandler(config)

app.state.memory_manager = memory_manager
app.state.rag_handler = rag_handler

# Include routes
app.include_router(router)

# Exception Handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred.", "detail": str(exc)},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": "Validation error", "errors": exc.errors()},
    )

# Run the application for development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
