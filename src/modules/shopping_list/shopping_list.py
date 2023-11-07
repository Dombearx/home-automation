from typing import List

from src.modules.home_assistant.consts import Service
from src.modules.home_assistant.integration import HomeAssistantIntegration


class ShoppingList:

    @staticmethod
    def add_to_shopping_list(items: List[str]):
        service_data = {
            "shopping_items": items
        }

        HomeAssistantIntegration.send(Service.SHOPPING_LIST, payload=service_data)

