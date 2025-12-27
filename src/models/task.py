"""Task data model."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    """
    Represents a single task in the todo list.
    
    Attributes:
        id (int): Unique identifier for the task.
        title (str): The summary or name of the task.
        description (str): Detailed explanation of the task.
        is_complete (bool): Status of the task (True if done).
        created_at (datetime): Timestamp of creation.
    """
    id: int
    title: str
    description: str = ""
    is_complete: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def __str__(self) -> str:
        """Formatted string representation for CLI display."""
        status = "[x]" if self.is_complete else "[ ]"
        return f"[{self.id}] {status} {self.title}"
