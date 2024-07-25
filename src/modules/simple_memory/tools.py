from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from src.modules.simple_memory.simple_memory import SimpleMemory

class SaveMemorySchema(BaseModel):
    content: str = Field(description="should be a content to remember, should be as specific as possible.")

class ReadMemorySchema(BaseModel):
    should_read: bool = Field(description="should be True")

class SaveMemoryTool(BaseTool):
    name: str = "save_to_memory"
    description: str = "Allows to remember something. You can remember only one thing at a time."
    args_schema: Type[SaveMemorySchema] = SaveMemorySchema

    def _run(
        self,
        content: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        SimpleMemory.write_to_memory(content)
        return True

    async def _arun(
        self,
        content: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("save_to_memory does not support async")

class ReadMemoryTool(BaseTool):
    name: str = "read_from_memory"
    description: str = "Allows to recall remembered content."
    args_schema: Type[ReadMemorySchema] = ReadMemorySchema

    def _run(
        self,
        should_read: bool,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        return SimpleMemory.read_from_memory()

    async def _arun(
        self,
        should_read: bool,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("read_from_memory does not support async")

