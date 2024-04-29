from src.modules.computer.tools import TurnOnComputerTool
from src.modules.light.tools import SwitchLightTool
from src.modules.todoist.tools import AddTodoTasksTool
from src.modules.youtube.tools import YouTubePlayVideoTool, YouTubeSearchTool

# google_search = GoogleSearch()

TOOLS = [
    YouTubeSearchTool(),
    YouTubePlayVideoTool(),
    AddTodoTasksTool(),
    SwitchLightTool(),
    TurnOnComputerTool(),
]

# TOOLS += google_search.get_tools()
