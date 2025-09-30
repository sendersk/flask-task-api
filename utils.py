from typing import Dict, List

VALID_STATUSES = {"todo", "in_progress", "done"}


def validate_task_input(data: Dict) -> List[str]:
    """Validate input data for creating or updating a Task.
    Returns a list of error messages (empty if valid)."""
    errors = []

    # Title validation
    title = data.get("title")
    if title is not None:
        if not isinstance(title, str) or len(title.strip()) < 3:
            errors.append("Title must be at least 3 characters long.")

    # Description validation
    description = data.get("description")
    if description is not None:
        if not isinstance(description, str) or len(description.strip()) == 0:
            errors.append("Description is required.")

    # Status validation
    status = data.get("status")
    if status is not None and status not in VALID_STATUSES:
        errors.append(f"Status must be one of {VALID_STATUSES}.")

    return errors
