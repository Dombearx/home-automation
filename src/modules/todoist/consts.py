import os
from enum import Enum

TODOIST_API_TOKEN = os.environ.get("TODOIST_API_TOKEN")


class Tag(Enum):
    SHOPPING = "SHOPPING"
    OTHER = "OTHER"
