from dataclasses import dataclass, field
from typing import Dict, Any


VALID_STATUSES = {"todo", "in_progress", "done"}

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = field(default="todo")

    def __post_init__(self):
        # Validate status
        if self.status not in VALID_STATUSES:
            raise ValueError(f"Invalid status '{self.status}'. Allowed: {VALID_STATUSES}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert Task object into dictionary (JSON-ready)."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }