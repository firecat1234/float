# Contains logic for executing tools
import os
import importlib

class ToolService:
    def __init__(self, tool_dir='./tools'):
      self.tool_dir = tool_dir
      self.tools = {}
      self._load_tools()

    def _load_tools(self):
        for dirpath, _, filenames in os.walk(self.tool_dir):
           for filename in filenames:
                if filename.endswith('.py') and filename != '__init__.py':
                  module_path = os.path.join(dirpath, filename)
                  module_path = module_path.replace('\\','/').replace('./', '').replace('/', '.')[:-3]
                  spec = importlib.util.find_spec(module_path)

                  if spec:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # for each function inside of that file, 
                    for name in dir(module):
                        obj = getattr(module, name)
                        if callable(obj) and not name.startswith('_') :
                            tool_id = f"{module_path}.{name}"
                            self.tools[tool_id] = obj # store the function itself in the registry.

        print(f"Loaded Tools: {self.tools.keys()}")
                    
    def call_tool(self, tool_id, *args, **kwargs):
      if tool_id in self.tools:
        return self.tools[tool_id](*args, **kwargs)
      else:
        raise ValueError(f"tool '{tool_id}' not found")