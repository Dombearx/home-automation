from src.modules.light.tools import SwitchLightTool
from src.modules.todoist.tools import AddTodoTasksTool
from src.modules.user_communication.tools import RespondToUserTool
from src.modules.youtube.tools import YouTubePlayVideoTool, YouTubeSearchTool

# google_search = GoogleSearch()

TOOLS = [
    RespondToUserTool(),
    YouTubeSearchTool(),
    YouTubePlayVideoTool(),
    AddTodoTasksTool(),
    SwitchLightTool(),
]

# TOOLS += google_search.get_tools()
