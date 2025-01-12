# tests/test_services.py
import pytest
from services.data_service import DataService
from services.llm_service import LLMService
from services.memory_service import MemoryService
from services.security_service import SecurityService
from services.task_service import TaskService
from services.tool_service import ToolService

@pytest.fixture
def data_service():
    return DataService()

@pytest.fixture
def llm_service():
    return LLMService()

@pytest.fixture
def memory_service():
    return MemoryService()

@pytest.fixture
def security_service():
    return SecurityService(key="testkey")

@pytest.fixture
def task_service():
    return TaskService()

@pytest.fixture
def tool_service():
    return ToolService(tool_dir="./tools")

def test_store_memory(data_service):
    data_service.store_memory({"id": "1", "data": "test memory"})
    result = data_service.retrieve_memory("test query")
    assert result  # Verify the result isn't empty

def test_generate_text(llm_service):
    response = llm_service.generate_text("Generate a test response.")
    assert "Response from" in response

def test_memory_service(memory_service):
    memory_service.store("short-term memory")
    assert "short-term memory" in memory_service.retrieve_short()
    memory_service.clear()
    assert not memory_service.retrieve_short()

def test_security_service(security_service):
    encrypted = security_service.encrypt("plaintext")
    assert "encrypted" in encrypted
    decrypted = security_service.decrypt(encrypted)
    assert decrypted == "plaintext"

def test_task_service(task_service):
    task_service.add_task("Test Task")
    assert "Test Task" in task_service.list_tasks()

def test_tool_service(tool_service):
    tool_service._load_tools()
    tool_id = next(iter(tool_service.tools))
    assert tool_id  # Ensure at least one tool is loaded
    result = tool_service.call_tool(tool_id, context={}, args=[])
    assert result  # Ensure the tool executes
