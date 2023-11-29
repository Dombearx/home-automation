from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from src.modules.user_communication.communication import UserCommunication


class RespondToUserSchema(BaseModel):
    response: str = Field(description="should be a response that user will see")


class RespondToUserTool(BaseTool):
    name: str = "respond_to_user"
    description: str = (
        "Allows to send response to user, without it the user will not see the reponse."
    )
    args_schema: Type[RespondToUserSchema] = RespondToUserSchema

    def _run(
        self,
        response: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        UserCommunication.respond(response)
        return True

    async def _arun(
        self,
        response: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
