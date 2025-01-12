# contains async celery tasks

from celery import Celery
from .app.services.tool_service import ToolService
import time
import logging


celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

tool_service = ToolService() # used to call tools

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