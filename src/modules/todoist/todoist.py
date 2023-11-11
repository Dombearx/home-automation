from datetime import datetime
from typing import Dict, List

from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Project, Task

from src.modules.todoist.consts import TODOIST_API_TOKEN, Tag


class Todoist:
    def __init__(self):
        self.api = TodoistAPI(TODOIST_API_TOKEN)

    def get_projects(self) -> List[Project]:
        return self.api.get_projects()

    def add_project(self, project_name: str) -> Project:
        return self.api.add_project(name=project_name)

    def get_inbox_project(self) -> Dict:
        projects = self.get_projects()
        return [
            {"project_id": project.id}
            for project in projects
            if project.is_inbox_project
        ][0]

    def get_tasks(self, project_id: str) -> List[Dict]:
        tasks = self.api.get_tasks(project_id=project_id)
        return [
            {"task_name": task.content, "task_id": task.id}
            for task in tasks
            if task.due and self._is_task_late(task.due.date)
        ]

    def _is_task_late(self, task_date):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")
        today_date = datetime.strptime(formatted_date, "%Y-%m-%d")
        task_date = datetime.strptime(task_date, "%Y-%m-%d")

        return task_date <= today_date

    def add_task(self, task_name: str, tag: Tag, due_string: str = "today") -> Task:
        project_id = self.get_inbox_project()["project_id"]
        tasks = self.get_tasks(project_id)
        # TODO rewrite this logic
        for task in tasks:
            if task["task_name"] == tag.value:
                parent_task_id = task["task_id"]
                break
        else:
            # create new parent task
            parent_task_id = self.api.add_task(
                content=tag.value, project_id=project_id, due_string=due_string
            ).id

        return self.api.add_task(
            content=task_name,
            project_id=project_id,
            parent_id=parent_task_id,
        )
