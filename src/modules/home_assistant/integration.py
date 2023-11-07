import json

import requests
from loguru import logger

from src.modules.home_assistant.consts import (HA_ACCESS_TOKEN, HA_ACCESS_URL,
                                               Service, get_service_webhook_id)


class HomeAssistantIntegration:
    @staticmethod
    def send(service: Service, payload: dict):
        headers = {
            "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
        webhook_id = get_service_webhook_id(service)

        service_url = f"{HA_ACCESS_URL}/api/webhook/{webhook_id}"
        response = requests.post(service_url, headers=headers, data=json.dumps(payload))

        logger.debug(f"{response.status_code = }")
        logger.debug(response.text)
