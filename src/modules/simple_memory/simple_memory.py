import os

from loguru import logger
from datetime import datetime

MEMORY_DIR = "~/.local/share/homar"
FILE_NAME = MEMORY_DIR + "/memory"

class SimpleMemory:

    @staticmethod
    def write_to_memory(content):
        content = f"Remembered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {content}"
        if not os.path.exists(MEMORY_DIR):
            os.makedirs(MEMORY_DIR)
        logger.debug(f"Writing to memory: {content}, {FILE_NAME}")
        with open(FILE_NAME, "w") as f:
            f.write(content)

    @staticmethod
    def read_from_memory():
        logger.debug(f"Reading from memory: {FILE_NAME}")
        if not os.path.exists(FILE_NAME):
            return "I don't remember anything."
        with open(FILE_NAME, "r") as f:
            return f.read()

