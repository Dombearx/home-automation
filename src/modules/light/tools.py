from typing import Optional, Type

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from src.modules.light.light import Light, LightState


class SwitchLightSchema(BaseModel):
    new_light_state: LightState = Field(description="should be a new state of light")


class SwitchLightTool(BaseTool):
    name: str = "switch_light"
    description: str = "Allows to turn the light on and off."
    args_schema: Type[SwitchLightSchema] = SwitchLightSchema

    def _run(
        self,
        new_light_state: LightState,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        Light.switch_light(new_light_state)
        return True

    async def _arun(
        self,
        new_light_state: LightState,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
