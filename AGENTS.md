# Agent Coding Guidelines

Guidelines for AI agents (Claude, Cursor, etc.) working on this codebase.

---

## Coding Pattern Preferences

- **Scope**: Only make changes that are requested or you are confident are well understood and related to the change being requested.
- **KISS**: Always prefer simple solutions.
- **Keep It Tidy**: Keep the codebase clean and organised. Lint as you go rather than waiting until the end. Run `make fmt` after changes and ensure code is correctly formatted, typed, and linted.
- **Don't Repeat Yourself**: Adhere to DRY principles. Check for existing similar code before adding new functionality.
- **Code Style**: When fixing an issue, do not introduce new patterns or technologies without exhausting existing options first. If you must deviate, update all similar patterns for consistency and remove old implementations.
- **File Length**: Avoid files over 200-300 lines. Refactor at that point.
- **Makefile**: Use `make` commands rather than raw scripts. Check the Makefile for existing commands before running tools directly.
- **Use Dedicated Tooling**: Use ruff, mypy, and other configured tools rather than writing custom scripts. Check the Makefile for available commands (`make lint`, `make fmt`, `make test`).
- **Mocks/Stubs**: Mocking is only for tests. Never add fake data patterns to library code.
- **.env**: Never overwrite .env files without asking first.

---

## Coding Workflow Preferences

- **Relevancy**: Focus on code relevant to the task. Do not touch unrelated code.
- **Downstream Effects**: Consider what other code might be affected by changes. After each stage, run `make lint` and `make test`.
- **Git Conventional Commits**: Provide commit messages in "conventional commits" style. NEVER push commits upstream - provide the message and wait for a human to commit.
- **Linting & Formatting**: Fix linter issues rather than adding ignores. Only ignore rules with explicit permission and good reason.
- **Testing**: Write thorough tests for all major functionality in the `tests/` directory:
  - **Unit Tests** (`tests/unit/`): Test individual functions in isolation.
  - **Integration Tests** (`tests/integration/`): Validate component interactions.

---

## Python Preferences

- **Package Management**: Always use UV. Use `uv run python3` instead of `python3`. Use native UV commands (`uv add`, `uv sync`) not pip through UV.
- **Linting & Formatting**: Use ruff for linting/formatting (line length 100 for this project), mypy for type-checking. Run these tools often.
- **No Wildcard Imports**: Never use `from module import *`. Import each item explicitly.
- **Pyproject**: Always use pyproject.toml over ini files.
- **Type Safety**: Always add type hints (`str | None`, `list[int]`). Avoid `Any` unless strictly necessary. Use modern syntax: `list` not `List`, `X | None` not `Optional[X]`.
- **Code Style**: Follow PEP 8. Think about style as you go, not after finishing.
- **Python Version**: Use Python 3.11+.
- **Filesystem Handling**: Use Pathlib for file paths.
- **Testing**: Use pytest for tests.
- **Dependencies**: Use UV exclusively - no pip references in the codebase.

---

## Component Library Specific

- **Atomic Design**: This library follows Atomic Design methodology:
  - **Atoms** (`components/atoms/`): Basic elements (button, input, badge, card)
  - **Molecules** (`components/molecules/`): Combinations of atoms (search_bar, breadcrumbs)
  - **Organisms** (`components/organisms/`): Larger components (header, data_table)
  - **Templates** (`components/templates/`): Page structures (base_page, auth_page_layout)

- **Design Tokens**: Use the design system tokens (`Colors`, `Spacing`, `Typography`, etc.) rather than hardcoding values.

- **Dependency Injection**: Components receive data as props - they never fetch their own data. Business logic belongs in the consuming application, not in components.

- **HTMX Integration**: All interactive components should support `hx_*` attributes via `**kwargs`.

- **Pure Functions**: Components are pure functions - same inputs produce same outputs, no side effects.

- **Showcase Testing**: After adding/modifying components, verify they render correctly in the showcase (`make showcase`).

---

## FastHTML Specific

- **Documentation**: Refer to `docs/fasthtml_llms.txt` for FastHTML patterns and conventions.
- **No Wildcard Imports**: Import explicitly from `fasthtml.common`, never use `*`.
- **Inline Styles**: This library uses inline styles for Cloud Run compatibility (stateless containers, no static file serving).

---

## Documentation Preferences

- **README**: Include instructions for installation, usage, and running the showcase.
- **Docstrings**: All public functions should have docstrings with Args, Returns, and Example sections.
- **Type Annotations**: All functions must have complete type annotations.

---

## Refactoring Guidelines

When asked to refactor:

1. Review the codebase for "high-coupling, low-cohesion" areas
2. Ensure comprehensive test coverage exists
3. Run static analysis (`make lint`)
4. Follow SOLID principles and improve modularity
5. Use design patterns where applicable
6. Remove redundant/duplicate code (DRY)
7. Refactor in small, manageable steps
8. Maintain single sources of truth for configuration
9. Follow existing patterns; if deviating, update all similar code
10. Run all linters, formatters, and tests before completing

---

## The Twelve-Factor App Principles

Where applicable, follow these principles:

- **Explicit Dependencies**: Use UV and pyproject.toml; no system-wide dependencies
- **Config via Env Vars**: Secrets/config in environment variables, not code
- **Stateless Processes**: Components are pure functions with no side effects
- **Dev = Prod**: Keep environments identical
- **Log to Stdout**: Let external tools handle log aggregation
