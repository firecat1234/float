# contains async celery tasks

from celery import Celery
from .app.services.tool_service import ToolService
from services.etl_tools import ETLTools
from services.refined_services import RefinedServices
import time
import logging

celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

tool_service = ToolService() # used to call tools
etl_tools = ETLTools()
services = RefinedServices()

@celery_app.task
def execute_tool(tool_id, *args, **kwargs):
    # executes the called tool in async context.
    try:
        result = tool_service.call_tool(tool_id, *args, **kwargs)
        return result
    except ValueError as e:
        return f"Tool {tool_id} not found: {e}"
    except Exception as e:
        logging.error(f"Error during tool execution: {e}")
        return f"Error during tool execution: {e}"

@celery_app.task
def long_running_task():
    # placeholder for any long running tasks.
    time.sleep(10) # wait 10 seconds.
    return 'long task complete.'

@celery_app.task
def execute_etl_pipeline(source: Dict, transform_config: Dict, load_target: Dict) -> Dict:
    """
    Executes the full ETL pipeline asynchronously.
    - Extracts data from the source.
    - Transforms the data according to the transform configuration.
    - Loads the transformed data to the specified target.
    Input schema:
    {
        "source": Dict,  # Configuration for the extract step
        "transform_config": Dict,  # Configuration for the transform step
        "load_target": Dict  # Configuration for the load step
    }
    """
    # Extract
    extract_result = etl_tools.extract(source)
    if extract_result["status"] != "success":
        return {"status": "error", "step": "extract", "message": extract_result.get("message")}

    # Transform
    transform_result = etl_tools.transform({
        "type": source["type"],
        "raw_data": extract_result.get("html" if source["type"] == "web" else "data")
    }, transform_config)
    if transform_result["status"] != "success":
        return {"status": "error", "step": "transform", "message": transform_result.get("message")}

    # Load
    load_result = etl_tools.load({"type": load_target["type"], "content": transform_result})
    if load_result["status"] != "success":
        return {"status": "error", "step": "load", "message": load_result.get("message")}

    return {"status": "success"}

@celery_app.task
def generate_embedding_task(content: Dict) -> Dict:
    """
    Generates embeddings for given content and stores it asynchronously.
    Input schema:
    {
        "text": str,  # Text to embed
        "metadata": Dict  # Metadata to store alongside embeddings
    }
    """
    return services.embed_and_store(content)
