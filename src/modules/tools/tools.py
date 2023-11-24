from typing import List

from langchain.agents import tool
from langchain.tools import YouTubeSearchTool
from todoist_api_python.models import Task

from src.modules.light.light import Light, LightState
from src.modules.todoist.consts import Tag
from src.modules.todoist.todoist import Todoist
from src.modules.user_communication.communication import UserCommunication
from src.modules.youtube.youtube import YoutubeConnector


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


todoist = Todoist()


@tool
def add_todo_task(task_name: str, tag: Tag, due_string: str = "today") -> Task:
    """Adds task to list. Due_string is human-like string. Returns data about added task."""
    return todoist.add_task(task_name, tag, due_string)


@tool
def add_todo_tasks(tasks_names: List[str], tag: Tag, due_string: str = "today") -> bool:
    """Adds many tasks at once with the same tag. Due_string is human-like string."""
    todoist.add_tasks(tasks_names, tag, due_string)
    return True


# google_search = GoogleSearch()


@tool
def switch_light(new_light_state: LightState):
    """Allows to play youtube video with given url."""
    Light.switch_light(new_light_state)
    return True


TOOLS = [
    respond_to_user,
    YouTubeSearchTool(),
    play_video,
    add_todo_task,
    add_todo_tasks,
    switch_light,
]
#
# TOOLS += google_search.get_tools()
