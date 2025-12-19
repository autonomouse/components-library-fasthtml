# Agentic Coding Guide for FastHTML Development

This guide helps developers build FastHTML applications using AI coding assistants (Claude Code, Cursor, GitHub Copilot, etc.) with the components-library-python package.

## Table of Contents

1. [Introduction](#introduction)
2. [Which Coding Assistant](#which-coding-assistant)
3. [Getting Started](#getting-started)
4. [Warnings](#warnings)
5. [The Basics](#the-basics)
6. [How To Prompt](#how-to-prompt)
7. [Git Branching and Commit Messages](#git-branching-and-commit-messages)
8. [Working With APIs](#working-with-apis)
9. [Troubleshooting](#troubleshooting)

---

## Introduction

### Prerequisites

- Python 3.11+
- Basic understanding of web development concepts
- An AI coding assistant (Claude Code, Cursor, etc.)

### Terminology

- **FastHTML** - A Python library for building server-rendered hypermedia applications using HTMX
- **HTMX** - A library that allows you to access modern browser features directly from HTML
- **FT Components** - FastHTML's way of writing HTML in Python (FastTags)
- **Atomic Design** - A methodology for creating design systems with a hierarchical component structure
- **Agentic Coding** - Using AI tools to assist with writing code

---

## Which Coding Assistant?

There are many agentic coding tools available. We recommend using Claude Code or Cursor to get started.

### CLI-based

| Tool        | Description                                                                    | Link                                       | Cost       |
| ----------- | ------------------------------------------------------------------------------ | ------------------------------------------ | ---------- |
| Claude Code | Terminal-based AI coding agent by Anthropic with repo-wide context.            | [anthropic.com](https://www.anthropic.com) | Expensive  |
| Aider       | Open-source terminal pair-programmer that edits and commits code from prompts. | [aider.chat](https://aider.chat)           | Free       |

### Standalone

| Tool   | Description                                                          | Link                             | Cost            |
| ------ | -------------------------------------------------------------------- | -------------------------------- | --------------- |
| Cursor | AI-first code editor forked from VS Code with deep agentic features. | [cursor.com](https://cursor.com) | Free/Subsidised |

### VS Code Plug-Ins

| Tool     | Description                                                     | Link                                                                                         | Cost |
| -------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---- |
| Roo Code | AI agent that can browse, edit, and debug across your codebase. | [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=RooAI.roo-code)         | Free |
| Cline    | Conversational coding tasks and autonomous refactoring.         | [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) | Free |

---

## Getting Started

1. **Install the Library**

```bash
uv add components-library
```

2. **Create a Basic FastHTML App**

```python
from fasthtml.common import fast_app, serve
from components_library import (
    base_page, heading, text, button, card,
    base_styles, component_styles, htmx_script
)

app, rt = fast_app()

@rt("/")
def get():
    return base_page(
        card(
            heading("Welcome", level=1),
            text("This is a FastHTML app using components-library"),
            button("Click me", variant="solid", color_palette="brand"),
        ),
        title="Labs App"
    )

serve()
```

3. **Run the App**

```bash
python app.py
# Or with uvicorn for development
uvicorn app:app --reload --port 8000
```

---

## Warnings

Agentic coding assistants can...

### Delete Production Data

An over-eager assistant may run destructive commands if not sandboxed.

**Mitigations:**
- Never ask it to operate directly on a database - use services/routes for data operations
- Use environment variables for sensitive configuration
- Watch what the model is doing and don't be afraid to stop it

### Hard-Code Secrets

If you tell it your API key or secrets, it will probably hard-code them somewhere.

**Mitigations:**
- Always use `.env` files for secrets (add to `.gitignore`)
- Search the codebase for secrets before committing: `grep -r "your_secret" .`
- Submit code for review

### Rack Up High Costs Quickly

Using a coding assistant can get expensive with token-based pricing.

**Mitigations:**
- Turn off autonomous loops unless actively supervising
- Use multiple agents to take advantage of free tiers
- If you can do something simple by hand, just do it

---

## The Basics

### The Component Library

This library follows atomic design principles. For detailed information on component architecture, design tokens, and HTMX integration, see:

- [Feature Development Guide](./feature-development-guide.md) - Comprehensive component development standards
- [Component Flexibility & HTMX](./component_flexibility.md) - HTMX configuration patterns
- [Dependency Injection Architecture](./dependency_injection_architecture.md) - Data flow and separation of concerns

### Shared Utilities

Beyond UI components, the library provides reusable utilities:

- **API Client** (`components_library.api.v2`) - Versioned HTTP client for backend APIs
- **Session Utilities** (`components_library.utils.session`) - Starlette session management helpers

See [Feature Development Guide](./feature-development-guide.md#shared-utilities) for usage examples.

### Minimize JavaScript

**Prefer native HTML/CSS and HTMX over custom JavaScript.**

When implementing features, consider in order:
1. **HTML first** - semantic elements (`<details>`, `<dialog>`, `<form>`)
2. **CSS second** - modern CSS (`:has()`, transitions, animations)
3. **HTMX third** - server interactions via attributes
4. **JavaScript last** - only when no alternative exists

See [Feature Development Guide](./feature-development-guide.md#minimize-javascript) for detailed examples.

---

## How To Prompt

### A Prompt To Get You Started

```
I would like to create a FastHTML page using the components-library-python package.

The page needs to:
1. Display a list of items from an API
2. Allow filtering by category
3. Support pagination

Please follow the patterns in @feature-development-guide.md and use
the existing components from the library. Use HTMX for all dynamic
interactions without full page reloads.
```

### Use the Guides Included

Reference documentation files in your prompts:

```
Use the @feature-development-guide.md to help you.
Use @dependency_injection_architecture.md for data flow patterns.
Use @component_flexibility.md for HTMX configuration.
```

### Build Up Layer by Layer

Break down goals into smaller tasks:

1. First, create the basic page structure
2. Add the data display components
3. Implement filtering
4. Add pagination
5. Polish the UI

### Be Specific

Use component names from the library:

```
I would like to use the `data_table` organism component to display
the items with sortable columns. Use the `filter_panel` molecule
for category filtering.
```

### Give It Code

If you have existing code, share it:

```
Here's my current route that returns the data. Please create a
component to display this:

@rt("/api/items")
def get_items():
    items = db.get_items()
    return [{"id": i.id, "name": i.name} for i in items]
```

### Use the Linting Tools

```bash
# Format code
make fmt

# Run linting and type checking
make check

# Run tests
make test
```

---

## Git Branching and Commit Messages

### Branching Strategy

Always work in a feature branch:

```bash
git checkout -b feat/<feature_name>
# Example: git checkout -b feat/user-dashboard
```

**Branch naming conventions:**
- `feat/<feature_name>` - For new features
- `fix/<issue_description>` - For bug fixes
- `docs/<topic>` - For documentation updates
- `refactor/<component_name>` - For code improvements

### Commit Message Generation

Ask your AI assistant:

```
Using `git diff` please create a git commit message in conventional commits format
```

**Example commit messages:**
- `feat(components): add data table with sorting`
- `fix(button): handle disabled state correctly`
- `docs(readme): update installation instructions`

### Before Pushing

Always run quality checks:

```bash
make fmt      # Format code
make check    # Run linting
make test     # Run tests
```

---

## Working With APIs

### Shared API Client

The library provides a versioned API client for backend calls:

```python
from components_library.api.v2 import ApiClient
from components_library.api import ApiSuccess, ApiFailure

# Create client with your app's configuration
client = ApiClient(
    base_url=settings.api_base_url,
    timeout=30,
)

# Make requests
response = await client.get("/items", params={"q": query}, access_token=token)

if isinstance(response, ApiSuccess):
    items = response.data
else:
    error = response.error.message
```

**Key points:**
- `ApiClient` requires explicit configuration (dependency injection)
- Versioned structure (`api/v2/`) for future compatibility with `api/v3/`
- Returns typed `ApiSuccess` or `ApiFailure` responses

### Route Pattern

Keep business logic in routes, presentation in components:

```python
from components_library import search_results

@rt("/search")
def search(req: Request):
    # Business logic in route
    query = req.query_params.get("q", "")

    with Session(engine) as session:
        results = search_service.search(session, query)

    # Transform data
    result_data = [
        {"id": r.id, "name": r.name, "score": r.score}
        for r in results
    ]

    # Inject into component
    return search_results(
        results=result_data,
        query=query,
        result_count=len(result_data),
    )
```

### HTMX Patterns

Use partial updates instead of full page reloads:

```python
# Route returns just the updated content
@rt("/api/items")
def get_items(page: int = 1):
    items = paginate_items(page)
    return vstack(
        *[item_card(item) for item in items],
        gap=2,
    )

# Component triggers the update
button(
    "Load More",
    hx_get=f"/api/items?page={next_page}",
    hx_target="#items-list",
    hx_swap="beforeend",
)
```

---

## Troubleshooting

**The page is blank or showing errors**
- Check that you've included `base_styles()` and `component_styles()` in your page head
- Verify imports are correct

**HTMX interactions aren't working**
- Ensure `htmx_script()` is included in the page head
- Check that `hx_target` selectors match element IDs

**Styles look wrong**
- Use design tokens from the library instead of hardcoded values
- Check that you're using the correct variant/size props

**Components not found**
- Verify the library is installed: `pip show components-library`
- Check import paths match the library structure

---

## Related Documentation

- [Feature Development Guide](./feature-development-guide.md)
- [Dependency Injection Architecture](./dependency_injection_architecture.md)
- [Component Flexibility & HTMX](./component_flexibility.md)
- [FastHTML Documentation](./fasthtml_llms.txt)
