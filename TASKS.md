# Task Breakdown - Todo Console App

**Status**: Active
**Version**: 1.0.0

## Phase 1: Setup & Core Structure

- [ ] **Task 1: Project Initialization**
  - Initialize `uv` project.
  - Create directory structure (`src/models`, `src/services`, `src/ui`, `src/utils`).
  - Create `pyproject.toml` with metadata.
  - Create `README.md` and `CLAUDE.md`.

- [ ] **Task 2: Data Model Implementation**
  - Implement `Task` dataclass in `src/models/task.py`.
  - Add type hints and docstrings.

## Phase 2: Business Logic (Service Layer)

- [ ] **Task 3: Task Manager - Create & Read**
  - Implement `TaskManager` class in `src/services/task_manager.py`.
  - Implement `add_task` logic (ID generation).
  - Implement `get_all_tasks` logic.
  - Add unit tests for these methods (optional but recommended).

- [ ] **Task 4: Task Manager - Update & Delete**
  - Implement `update_task` method (handle partial updates).
  - Implement `delete_task` method.
  - Implement `toggle_complete` method.
  - Add validation logic (check if ID exists).

## Phase 3: User Interface (CLI)

- [ ] **Task 5: CLI - Base & Read Operations**
  - Implement `CLI` class in `src/ui/cli.py`.
  - Create main loop and menu display.
  - Implement "View Tasks" display formatting.
  - Implement "Add Task" input flow.

- [ ] **Task 6: CLI - Update & Delete Operations**
  - Implement "Update Task" flow (input ID, then details).
  - Implement "Delete Task" flow (input ID, confirm scope).
  - Implement "Toggle Complete" flow.
  - Add input validation helper in `src/utils/validators.py`.

## Phase 4: Integration & Polish

- [ ] **Task 7: Main Entry Point & Wiring**
  - Create `src/main.py`.
  - Wire up `CLI` to `TaskManager`.
  - Manual verification of all 5 features.

- [ ] **Task 8: Final Review & Documentation**
  - Verify strict type hinting compliance.
  - Ensure all docstrings are present.
  - Finalize `README.md` with usage instructions.
  - Final git commit.
