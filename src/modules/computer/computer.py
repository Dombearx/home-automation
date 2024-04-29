from src.modules.home_assistant.consts import Service
from src.modules.home_assistant.integration import HomeAssistantIntegration


class Computer:
    @staticmethod
    def turn_computer_on():
        HomeAssistantIntegration.send(Service.TURN_ON_PC)
