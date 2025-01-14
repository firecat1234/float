# Contains logic for executing tools
import os
import importlib
from pydantic import BaseModel

#

def _load_tools(self):
for dirpath, _, filenames in os.walk(self.tool_dir):
    for filename in filenames:
        if filename.endswith('.py') and filename != '__init__.py':
            # Load tools dynamically
            tool_module = self._import_module(dirpath, filename)
            self._register_tools_from_module(tool_module)

def _register_tools_from_module(self, module):
    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj) and not name.startswith('_'):
            self.tools[name] = obj
            print(f"Registered tool: {name}")

def call_tool(self, tool_id, context, *args, **kwargs):
    if tool_id not in self.tools:
        raise ValueError(f"Tool '{tool_id}' not found.")
    print(f"Calling tool: {tool_id} with context: {context}")
    return self.tools[tool_id](*args, **kwargs)

#tool tests

def test_tool_registration(tool_service):
    tool_service._load_tools()
    assert "multiply_numbers" in tool_service.tools

def test_tool_execution(tool_service):
    result = tool_service.call_tool("multiply_numbers", {"a": 3, "b": 4})
    assert result["result"] == 12

def test_invalid_tool(tool_service):
    try:
        tool_service.call_tool("nonexistent_tool", {})
    except ValueError as e:
        assert str(e) == "Tool 'nonexistent_tool' not found."


class MultiplyNumbersInput(BaseModel):
    a: int
    b: int

class MultiplyNumbersOutput(BaseModel):
    result: int
