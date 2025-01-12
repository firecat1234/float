from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional

class ToolSchema(BaseModel):
    """
    Defines the structure of tool configurations for the agent.
    """
    tool_id: str = Field(description="The unique identifier for the tool. This is how you call it.")
    description: str = Field(description="A description of what the tool does.")
    input_schema: Dict[str, Any] = Field(description="The expected input data structure.")
    permissions: Optional[List[str]] = Field(default=[], description="A list of permissions required to execute tool. User validation will halt the flow if these are not available.")

class Message(BaseModel):
  """
  Defines the structure of a message in the chat.
  """
  sender: str = Field(description="who sent this message.")
  content: str = Field(description="text of the message.")
  timestamp: float = Field(description="Time the message was sent.")
  metadata: Optional[Dict[str, str]] = Field(default={}, description="any extra info.")