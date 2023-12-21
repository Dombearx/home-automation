import asyncio
import datetime
import os
import requests
import discord
from loguru import logger

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def send_to_endpoint(human_order: str, endpoint_name: str) -> str:
    """Send human_order to localhost:8000/receive_message endpoint"""
    response = requests.post(
        f"http://localhost:8000/{endpoint_name}", data={"human_order": human_order}
    )
    return response.json()["response"]


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    endpoint_name = "receive_command"
    if message.author == client.user:
        return
    if client.user in message.mentions:
        human_order = message.content.replace(f"<@{client.user.id}> ", "")
        logger.debug(f"Processing: {human_order}")

        async with message.channel.typing():
            response = send_to_endpoint(human_order, endpoint_name=endpoint_name)
            await message.channel.send(response)


if __name__ == "__main__":
    client.run(os.environ["DISCORD_TOKEN"])
