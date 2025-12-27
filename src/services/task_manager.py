"""Task Manager Service."""

from typing import List, Dict, Optional
from src.models.task import Task

class TaskManager:
    """
    Manages the lifecycle and storage of tasks.
    
    Attributes:
        _tasks (Dict[int, Task]): In-memory storage mapping ID to Task.
        _next_id (int): Auto-incrementing counter for IDs.
    """

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Creates and stores a new task.
        
        Args:
            title: The task title.
            description: Optional details.
            
        Returns:
            The created Task object.
        """
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks (sorted by ID).
        
        Returns:
            List of Task objects.
        """
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a single task by ID.
        
        Args:
            task_id: The ID to search for.
            
        Returns:
            Task object or None if not found.
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates an existing task's fields.
        
        Args:
            task_id: ID of task to update.
            title: New title (if provided).
            description: New description (if provided).
            
        Returns:
            True if successful, False if ID not found.
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Removes a task permanently.
        
        Args:
            task_id: ID of task to delete.
            
        Returns:
            True if successful, False if ID not found.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_complete(self, task_id: int) -> Optional[bool]:
        """
        Toggles the completion status of a task.
        
        Args:
            task_id: ID of task to toggle.
            
        Returns:
            New status (bool) if successful, None if ID not found.
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        
        task.is_complete = not task.is_complete
        return task.is_complete
