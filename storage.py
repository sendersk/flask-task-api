import json
import os
from typing import Dict, List, Optional
from models import Task

# Path to tasks file
TASKS_FILE = "tasks.json"

# In-memory storage for tasks (id -> Task)
tasks: Dict[int, Task] = {}
_next_id: int = 1 # auto-increment id counter


def _load_from_file():
    """Load tasks from a JSON file into memory."""
    global tasks, _next_id
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            tasks = {int(k): Task(**v) for k, v in data.items()}
            _next_id = max(tasks.keys(), default=0) + 1


def _save_to_file():
    """Save current tasks to a JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump({tid: task.__dict__ for tid, task in tasks.items()}, f, indent=4)


def add_task(title: str, description: str, status: str = "todo") -> Task:
    """Create a new task, save it, and return it."""
    global _next_id
    task = Task(id=_next_id, title=title, description=description, status=status)
    tasks[_next_id] = task
    _next_id += 1
    _save_to_file()
    return task


def get_task(task_id: int) -> Optional[Task]:
    """Retrieve a single task by its id."""
    return tasks.get(task_id)


def get_all_tasks() -> List[Task]:
    """Return a list of all tasks."""
    return list(tasks.values())


def update_task(task_id: int, data: Dict) -> Optional[Task]:
    """Update an existing task with new data."""
    task = tasks.get(task_id)
    if not task:
        return None
    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "status" in data:
        task.status = data["status"] # Task.__post_init__ will validate
    _save_to_file()
    return task


def delete_task(task_id: int) -> bool:
    """Delete a task and save changes."""
    deleted = tasks.pop(task_id, None) is not None
    if deleted:
        _save_to_file()
    return deleted


# Load tasks from file on module import
_load_from_file()
