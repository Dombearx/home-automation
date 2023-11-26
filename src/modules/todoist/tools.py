from typing import List, Optional, Type

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from src.modules.todoist.consts import Tag
from src.modules.todoist.todoist import Todoist


class AddTodoTasksSchema(BaseModel):
    tasks_names: List[str] = Field(
        description="should be a list of one or more tasks to add"
    )
    tag: Tag = Field(description="should be a tag assigned to given tasks")
    due_string: str = Field(
        description="should be a due date formatted as human-like string"
    )


class AddTodoTasksTool(BaseTool):
    name: str = "add_todo_tasks"
    description: str = (
        "Adds one or more tasks with given tag. " "Due_string is human-like string."
    )
    args_schema: Type[AddTodoTasksSchema] = AddTodoTasksSchema

    def _run(
        self,
        tasks_names: List[str],
        tag: Tag,
        due_string: str = "today",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool."""
        todoist = Todoist()
        todoist.add_tasks(tasks_names, tag, due_string)
        return True

    async def _arun(
        self,
        tasks_names: List[str],
        tag: Tag,
        due_string: str = "today",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
