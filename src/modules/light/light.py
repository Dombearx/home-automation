from enum import Enum

from src.modules.home_assistant.consts import Service
from src.modules.home_assistant.integration import HomeAssistantIntegration


class LightState(Enum):
    ON = "1"
    OFF = "0"


class Light:
    @staticmethod
    def switch_light(new_light_state: LightState):
        service_data = {"value": new_light_state.value, "event": "ABC"}

        HomeAssistantIntegration.send(Service.LIGHT_SWITCH, payload=service_data)
