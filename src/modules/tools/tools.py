from langchain.agents import tool
from langchain.tools import YouTubeSearchTool

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


TOOLS = [respond_to_user, YouTubeSearchTool(), play_video]
