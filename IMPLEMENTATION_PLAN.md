# Technical Implementation Plan - Todo Console App

**Version**: 1.0.0
**Date**: 2025-12-27
**Status**: Approved

## 1. Technology Stack
- **Language**: Python 3.13+
- **Environment Management**: `uv` (modern Python package manager)
- **External Dependencies**: None (Standard Library only proposed to keep it lightweight, but `rich` could be used for CLI formatting if desired. For "Basic Level", standard library is sufficient and safer).
- **Testing framework**: `unittest` (Standard library) or `pytest`.

## 2. Architecture Overview
The application will follow a clean, layered architecture to support maintainability and future testing.

### 2.1 Directory Structure
```
hackathon-2/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application Entry Point
│   ├── models/              # Data structures
│   │   ├── __init__.py
│   │   └── task.py          # Task dataclass
│   ├── services/            # Business Logic
│   │   ├── __init__.py
│   │   └── task_manager.py  # CRUD operations
│   ├── ui/                  # User Interface
│   │   ├── __init__.py
│   │   └── cli.py           # Menu handling and Input/Output
│   └── utils/               # Helpers
│       ├── __init__.py
│       └── validators.py    # Input validation functions
├── tests/                   # Automated tests
├── specs_history/           # Specification documents
├── pyproject.toml           # Configuration
├── README.md
├── CONSTITUTION.md
└── CLAUDE.md
```

### 2.2 Components

#### **A. Models (`src/models/task.py`)**
- `Task` class using `@dataclass`.
- Fields: `id: int`, `title: str`, `description: str`, `is_complete: bool`, `created_at: datetime`.
- Method: `__str__` or `display()` for formatted output.

#### **B. Services (`src/services/task_manager.py`)**
- `TaskManager` class.
- **State**: Holds `tasks` (List or Dict) and `next_id` counter.
- **Methods**:
  - `add_task(title, description)` -> Task
  - `get_all_tasks()` -> List[Task]
  - `get_task_by_id(id)` -> Optional[Task]
  - `update_task(id, title, description)` -> bool
  - `delete_task(id)` -> bool
  - `toggle_complete(id)` -> bool

#### **C. UI (`src/ui/cli.py`)**
- `CLI` class.
- **Responsibility**: Prints menu, captures user input, calls `TaskManager` methods, prints results.
- **Methods**:
  - `run()`: Main loop.
  - `print_menu()`: Helper.
  - `handle_add()`: Prompts user -> calls manager.add -> prints confirm.
  - `handle_view()`: Calls manager.get_all -> loops and prints.
  - ...etc for other actions.

#### **D. Utils (`src/utils/validators.py`)**
- Functions to sanitize inputs (e.g., ensure non-empty title, ensure ID is an integer).

#### **E. Main (`src/main.py`)**
- Bootstraps the application:
  ```python
  if __name__ == "__main__":
      app = CLI()
      app.run()
  ```

## 3. Implementation Guidelines
- **Dataclasses**: Use Python 3.7+ dataclasses for clean model definitions.
- **Type Hints**: Mandatory for all signatures.
- **Docstrings**: Required.
- **Error Handling**: `cli.py` should wrap calls in `try/except` blocks to catch logical errors from `task_manager.py` (though `task_manager` should ideally return status/results rather than raising exceptions for expected flows).

## 4. Risks & Mitigations
- **Data Loss**: Data is in-memory only. *Mitigation*: Explicitly stated in constraints; acceptable for Phase I.
- **Input Errors**: User enters "abc" for ID. *Mitigation*: Validator utility to check types before passing to logic.
