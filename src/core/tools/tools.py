from langchain.agents import tool
from langchain.tools import YouTubeSearchTool

from src.modules.google.google_search import GoogleSearch
from src.modules.light.tools import SwitchLightTool
from src.modules.todoist.tools import AddTodoTasksTool
from src.modules.user_communication.communication import UserCommunication
from src.modules.youtube.youtube import YoutubeConnector


@tool
def respond_to_user(response: str):
    """Allows to respond to user. Should only contain text that is easy to say"""
    UserCommunication.respond(response)
    return True


@tool
def play_video(url: str):
    """Allows to play YouTube video with given url."""
    YoutubeConnector.play_video(url)
    return True


# google_search = GoogleSearch()


TOOLS = [
    respond_to_user,
    YouTubeSearchTool(),
    play_video,
    AddTodoTasksTool(),
    SwitchLightTool(),
]

# TOOLS += google_search.get_tools()
