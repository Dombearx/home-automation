from typing import List

from langchain.agents import tool
from langchain.tools import YouTubeSearchTool

from src.modules.shopping_list.shopping_list import ShoppingList
from src.modules.user_communication.communication import UserCommunication
from src.modules.youtube.youtube import YoutubeConnector


# @tool
# def search_and_play_video(text_to_search: str):
#     """Allows to play youtube video."""
#     YoutubeConnector.search_and_play_video(text_to_search)
#     return True


@tool
def respond_to_user(response: str):
    """Allows to respond to user. Should only contain text that is easy to say"""
    UserCommunication.respond(response)
    return True


@tool
def play_video(url: str):
    """Allows to play youtube video with given url."""
    YoutubeConnector.play_video(url)
    return True


@tool
def add_to_shopping_list(items: List[str]):
    """Allows to add items to a shopping list"""
    ShoppingList.add_to_shopping_list(items)
    return True


TOOLS = [respond_to_user, YouTubeSearchTool(), play_video, add_to_shopping_list]
