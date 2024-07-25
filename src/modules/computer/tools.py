from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from src.modules.computer.computer import Computer


class TurnComputerSchema(BaseModel):
    turn_on_computer: bool = Field(description="should be True")


class TurnOnComputerTool(BaseTool):
    name: str = "turn_on_computer"
    description: str = "Allows to turn the computer on."
    args_schema: Type[TurnComputerSchema] = TurnComputerSchema

    def _run(
        self,
        turn_on_computer: bool,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        Computer.turn_computer_on()
        return True

    async def _arun(
        self,
        turn_on_computer: bool,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
