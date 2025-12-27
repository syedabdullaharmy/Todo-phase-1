# Project Constitution - Todo Console App

## Project Purpose
Build a robust, clean, and maintainable command-line todo application that serves as the foundation (Phase I) for a future full-stack AI-powered system. The primary goal is to demonstrate flawless spec-driven development practices.

## Core Principles

### 1. Development Methodology
- **Strict Spec-Driven Process**: No code is written without a corresponding specification and task.
- **Agentic Workflow**: Follow the cycle: Spec → Plan → Tasks → Implement.
- **No Magic Code**: All logic must be explicit, understandable, and documented.
- **Iterative Improvement**: Review and refine at each step.

### 2. Code Quality Standards
- **Clean Code**: Adhere strictly to PEP 8 and Python best practices.
- **Type Safety**: Use robust type hinting (`typing` module) for all functions and classes.
- **Documentation**: Mandatory docstrings (Google style) for modules, classes, and methods.
- **Modularity**: Separation of concerns (Models vs Services vs UI).
- **Error Handling**: Graceful handling of invalid inputs; the app should never crash from user error.

### 3. User Experience
- **Intuitive Interface**: Clear menu-driven CLI with helpful prompts.
- **Feedback**: Immediate visual confirmation of actions (success/error messages).
- **Simplicity**: Minimal friction for adding and managing tasks.
- **Consistency**: Standardized command patterns and output formatting.

### 4. Technical Constraints
- **Python 3.13+**: Leverage modern Python features.
- **In-Memory Storage**: For Phase I, data persistence is not required (simulated storage).
- **No External Database**: Minimize dependencies; use standard library where possible.
- **UV Package Manager**: Use `uv` for environment and dependency management.

### 5. Testing & Validation
- **Manual Verification**: All features must be verifiable through the CLI.
- **Edge Cases**: Explicitly test empty inputs, invalid IDs, and boundary conditions.
- **Unit Tests**: Code structure should support easy unit testing (even if manual testing is primary for Phase I).

## Success Criteria
- [ ] All 5 basic features (Add, View, Update, Delete, Mark Complete) functional.
- [ ] Zero crashes during normal operation.
- [ ] Clean, lint-free code with 100% type hint coverage.
- [ ] Complete documentation (README, CLAUDE.md, Specs).

---
**Version**: 1.0.0
**Status**: Active
