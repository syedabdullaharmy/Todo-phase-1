# Todo Console Application Specification

**Version**: 1.0.0
**Date**: 2025-12-27
**Type**: Phase I - Console App

## 1. Project Overview
A command-line interface (CLI) application for managing personal tasks. This project serves as the foundational "Phase I" of a larger system, focusing on core logic, clean architecture, and rigorous development practices without the complexity of a web frontend or database persistence.

## 2. User User Stories

### 2.1 Managing Tasks
- **As a user**, I want to **add a new task** with a title and optional description so that I can track what I need to do.
- **As a user**, I want to **view all my tasks** in a list so that I can see my workload at a glance.
- **As a user**, I want to **update a task's details** (title or description) if they change.
- **As a user**, I want to **delete a task** when it is no longer relevant.
- **As a user**, I want to **mark a task as complete** so I can track my progress.

### 2.2 Application Experience
- **As a user**, I want a **clean menu system** that guides me through options.
- **As a user**, I want clear **error messages** if I enter invalid information (e.g., deleting a non-existent ID).
- **As a user**, I want the application to **confirm my actions** (e.g., "Task added successfully").

## 3. Functional Requirements

### 3.1 Feature: Add Task
- **Input**: Title (required, non-empty), Description (optional).
- **Behavior**: Creates a new task object with a unique ID, "Incomplete" status, and creation timestamp.
- **Output**: Confirmation message with the new Task ID.

### 3.2 Feature: View Tasks
- **Input**: None (Select from menu).
- **Behavior**: Retrieves all tasks from memory.
- **Output**: A formatted list showing:
  - ID
  - Status (e.g., `[ ]` or `[x]`, or `✓`/`✗`)
  - Title
  - Description (optional or truncated)
- **Empty State**: Displays "No tasks found" if the list is empty.

### 3.3 Feature: Update Task
- **Input**: Task ID.
- **Behavior**:
  1. Validates ID exists.
  2. Prompts for new Title (press Enter to keep current).
  3. Prompts for new Description (press Enter to keep current).
  4. Updates the task object.
- **Output**: Confirmation message of the update.

### 3.4 Feature: Delete Task
- **Input**: Task ID.
- **Behavior**:
  1. Validates ID exists.
  2. Removes the task permanently from memory.
- **Output**: Confirmation message.

### 3.5 Feature: Mark Complete/Incomplete
- **Input**: Task ID.
- **Behavior**: Toggles the boolean status of the task.
- **Output**: Confirmation showing new status (e.g., "Task marked as Complete").

## 4. Non-Functional Requirements
- **Performance**: Operations should be instantaneous (<100ms).
- **Reliability**: Input validation must prevent all unhandled exceptions.
- **Usability**: CLI output should be spaced and formatted for readability.

## 5. Data Model (Conceptual)
**Task Entity**:
- `id`: Integer (Auto-incrementing)
- `title`: String
- `description`: String (Optional)
- `is_complete`: Boolean (Default: False)
- `created_at`: Datetime

## 6. User Interface (CLI Mockup)

```
=== TODO APP ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. Exit
Choice: 
```

**List View Example**:
```
[1] [x] Buy Groceries
    Description: Milk, Eggs, Bread
[2] [ ] Finish Report
    Description: Due Friday
```
