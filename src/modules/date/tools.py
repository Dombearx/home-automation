from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from src.modules.date.date import Date

class GetDateSchema(BaseModel):
    get_date: bool = Field(description="should be true to get the current date.")

class GetDateTool(BaseTool):
    name: str = "get_current_date"
    description: str = "Get the current date."
    args_schema: Type[GetDateSchema] = GetDateSchema

    def _run(
        self,
        get_date: bool,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        return Date.get_current_date()

    async def _arun(
        self,
        get_date: bool,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("get_current_date does not support async")
