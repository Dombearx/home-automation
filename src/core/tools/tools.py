from src.modules.computer.tools import TurnOnComputerTool
from src.modules.date.tools import GetDateTool
from src.modules.light.tools import SwitchLightTool
from src.modules.todoist.tools import AddTodoTasksTool
from src.modules.youtube.tools import YouTubePlayVideoTool, YouTubeSearchTool
from src.modules.simple_memory.tools import SaveMemoryTool, ReadMemoryTool

# google_search = GoogleSearch()

TOOLS = [
    YouTubeSearchTool(),
    YouTubePlayVideoTool(),
    AddTodoTasksTool(),
    SwitchLightTool(),
    TurnOnComputerTool(),
    SaveMemoryTool(),
    ReadMemoryTool(),
    GetDateTool(),
]

# TOOLS += google_search.get_tools()
