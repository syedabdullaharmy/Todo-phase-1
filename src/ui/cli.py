"""Command Line Interface for Todo App."""

import sys
from typing import Optional
from src.services.task_manager import TaskManager
from src.utils.validators import validate_non_empty, parse_int

class CLI:
    """
    Handles user interaction via standard input/output.
    """

    def __init__(self) -> None:
        self.manager = TaskManager()

    def print_menu(self) -> None:
        """Displays main menu options."""
        print("\n=== TODO APP ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Completion")
        print("6. Exit")

    def run(self) -> None:
        """Main application loop."""
        while True:
            self.print_menu()
            choice = input("Choice: ").strip()

            if choice == "1":
                self.handle_add()
            elif choice == "2":
                self.handle_view()
            elif choice == "3":
                self.handle_update()
            elif choice == "4":
                self.handle_delete()
            elif choice == "5":
                self.handle_toggle()
            elif choice == "6":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice, please try again.")

    def _get_id_input(self, prompt: str = "Enter Task ID: ") -> Optional[int]:
        """Helper to get a valid integer ID from user."""
        raw = input(prompt)
        try:
            return parse_int(raw)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def handle_add(self) -> None:
        """Flow for adding a new task."""
        print("\n--- Add Task ---")
        try:
            title_input = input("Title: ")
            title = validate_non_empty(title_input, "Title")
            desc = input("Description (optional): ").strip()
            
            task = self.manager.add_task(title, desc)
            print(f"Success: Task added with ID {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view(self) -> None:
        """Flow for listing tasks."""
        print("\n--- Your Tasks ---")
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return

        for t in tasks:
            print(str(t))
            if t.description:
                print(f"    {t.description}")

    def handle_update(self) -> None:
        """Flow for updating a task."""
        task_id = self._get_id_input()
        if task_id is None:
            return

        task = self.manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task {task_id} not found.")
            return

        print(f"Updating: {task.title}")
        new_title = input("New Title (Enter to keep): ").strip() or None
        new_desc = input("New Description (Enter to keep): ").strip() or None

        if self.manager.update_task(task_id, new_title, new_desc):
            print("Success: Task updated.")
        else:
            print("Error: Update failed.")

    def handle_delete(self) -> None:
        """Flow for deleting a task."""
        task_id = self._get_id_input()
        if task_id is None:
            return

        if self.manager.delete_task(task_id):
            print(f"Success: Task {task_id} deleted.")
        else:
            print(f"Error: Task {task_id} not found.")

    def handle_toggle(self) -> None:
        """Flow for marking complete/incomplete."""
        task_id = self._get_id_input()
        if task_id is None:
            return

        status = self.manager.toggle_complete(task_id)
        if status is None:
            print(f"Error: Task {task_id} not found.")
        else:
            state_str = "Complete" if status else "Incomplete"
            print(f"Success: Task {task_id} marked as {state_str}.")
