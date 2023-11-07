import os
from enum import Enum


class Service(Enum):
    SHOPPING_LIST = "SHOPPING_LIST_WEBHOOK_ID"


HA_ACCESS_TOKEN = os.environ.get("HA_ACCESS_TOKEN")
HA_ACCESS_URL = os.environ.get("HA_ACCESS_URL")


def get_service_webhook_id(service: Service):
    return os.environ.get(service.value)
