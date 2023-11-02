from langchain.agents import tool

from src.modules.user_communication.communication import UserCommunication
from src.modules.youtube.youtube import YoutubeConnector


@tool
def get_word_length(word: str) -> int:
    """Returns length of the word."""
    return len(word)


@tool
def search_and_play_video(text_to_search: str):
    """Allows to play youtube video."""
    YoutubeConnector.search_and_play_video(text_to_search)


@tool
def respond_to_user(response: str):
    """Allows to respond to user."""
    UserCommunication.respond(response)


TOOLS = [get_word_length, search_and_play_video, respond_to_user]
