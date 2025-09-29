from typing import Dict, List, Optional
from models import Task

# In-memory storage for tasks (id -> Task)
tasks: Dict[int, Task] = {}
_next_id: int = 1 # auto-increment id counter


def add_task(title: str, description: str, status: str = "todo") -> Task:
    """Create a new task and add it to the in-memory storage."""
    global _next_id
    task = Task(id=_next_id, title=title, description=description, status=status)
    tasks[_next_id] = task
    _next_id += 1
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

    return task


def delete_task(task_id: int) -> bool:
    """Delete a task by id. Returns True if deleted, False otherwise."""
    return tasks.pop(task_id, None) is not None