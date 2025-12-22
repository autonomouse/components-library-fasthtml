# Dependency Injection Architecture

## Overview

This component library follows **proper dependency injection principles** to ensure components remain pure, testable, and reusable across different FastHTML applications.

## Core Principles

### 1. Components Receive Data as Props

Components don't fetch their own data - they receive it from parent components or routes:

```python
# GOOD: Component receives data
from components_library import search_results

def search_results(
    results: list[dict[str, Any]],  # Injected dependency
    query: str | None = None,
    result_count: int | None = None,
    **kwargs: Any,
) -> Div:
    """Component receives data, doesn't fetch it."""
    return Div(...)

# BAD: Component fetches its own data
def search_results(**kwargs) -> Div:
    engine = create_engine(...)  # Don't do this in components!
    with Session(engine) as session:
        results = session.query(...)  # Business logic in component
    return Div(...)
```

### 2. Business Logic in Routes/Services

Data fetching and business logic live in routes and services, NOT in components:

**Route (contains business logic):**
```python
# your_app/routes/search.py
from components_library import search_results

def search_items(req: Request) -> Any:
    # Business logic: parse request
    query = req.query_params.get("query", "").strip()

    # Business logic: database operations
    engine = create_engine(settings.database_url)
    with Session(engine) as session:
        item_service = ItemService(session)
        items, total_count = item_service.search_items(query=query)

    # Business logic: data transformation
    item_data = [
        {"id": i.id, "name": i.name, ...}
        for i in items
    ]

    # Inject data into component
    return search_results(
        results=item_data,       # Dependency injected
        query=query,             # Dependency injected
        result_count=total_count # Dependency injected
    )
```

**Component (pure/presentational):**
```python
# components_library/components/molecules/search_results.py
def search_results(
    results: list[dict[str, Any]],  # Receives data
    query: str | None = None,
    result_count: int | None = None,
) -> Div:
    """Pure component - just renders what it receives."""
    if not results:
        return _empty_results(query)

    return Div(
        vstack(
            _results_header(count, query),
            vstack(*[_result_item(result) for result in results]),
        )
    )
```

### 3. Behavior Configuration Injected

Components receive their behavior as parameters, not hardcoded:

```python
from components_library import card

def result_card(
    item_id: str | int,
    item_name: str,
    # Behavior injected via parameters
    hx_target: str = "#main-content",
    hx_swap: str = "innerHTML",
    push_url: bool = True,
    **kwargs: Any,
) -> Div:
    """Behavior is configured by caller, not hardcoded."""
    return card(
        item_name,
        hx_get=f"/item/{item_id}",
        hx_target=hx_target,
        hx_swap=hx_swap,
        hx_push_url="true" if push_url else None,
        **kwargs
    )
```

**Usage in different contexts:**
```python
# Production: Full navigation
result_card(item_id=123, item_name="Item")

# Showcase: No navigation (behavior injected)
result_card(item_id=123, item_name="Item", push_url=False)

# Modal: Custom target (behavior injected)
result_card(
    item_id=123,
    item_name="Item",
    hx_target="#modal-content",
    hx_swap="innerHTML"
)
```

### 4. Component Composition

Components compose other components, receiving them as children:

```python
from components_library import card, heading, text, button

def feature_card(
    *content: Any,          # Child components injected
    header: Any = None,     # Header injected
    footer: Any = None,     # Footer injected
    **kwargs: Any,
) -> Div:
    """Receives its content/children as dependencies."""
    return card(
        header=header,
        footer=footer,
        *content,
        **kwargs
    )

# Usage
feature_card(
    text("This is the main content"),
    header=heading("Feature Title", level=3),
    footer=button("Learn More", variant="outline"),
)
```

## Components Are Pure Functions

Components are pure functions that:
1. Take inputs (props/dependencies)
2. Return HTML/FastHTML elements
3. Have no side effects
4. Don't modify global state
5. Don't fetch data

Example component signature:
```python
from components_library import detail_row

def detail_row(
    label: str,              # Input
    value: str,              # Input
    label_width: str | None = None,  # Configuration
    vertical: bool = False,  # Configuration
    **kwargs: Any,           # Additional props
) -> Div:                    # Output
    """Pure function: same inputs → same output."""
    return hstack(...)       # No side effects
```

## Test-Friendly Architecture

Because components use dependency injection, they're easily testable:

```python
from components_library import search_results

# Easy to test - just pass in mock data
def test_search_results_displays_items():
    mock_results = [
        {"id": 1, "name": "Item A"},
        {"id": 2, "name": "Item B"},
    ]

    result = search_results(
        results=mock_results,  # Inject test data
        query="test"
    )

    html = str(result)
    assert "Item A" in html
    assert "Item B" in html
```

## Styling: Intentional Inline Approach

### Why Inline Styles?

This library uses inline styles for Cloud Run compatibility:

> - No third-party CSS/JS libraries as static files
> - All styling must be inline or in `<style>` tags
> - All JavaScript must be inline or in `<script>` tags
> - Cloud Run compatibility required (stateless containers)

**This is NOT a violation of separation of concerns** - it's a deployment requirement.

### Styling Organization

**Design Tokens (Centralized):**
```python
from components_library import Colors, Spacing

# Use tokens for consistent styling
primary_color = Colors.brand.primary_600  # "#2563eb"
gap = Spacing.md  # "1rem"
```

**Theme Styles (Global):**
```python
from components_library import base_styles, component_styles

# Include once in your base template
def my_page(*content):
    return Html(
        Head(
            base_styles(),      # Global foundation styles
            component_styles(), # Component-specific CSS
        ),
        Body(*content)
    )
```

**Component Styles (Local):**
```python
from components_library import text, Colors

# Components use inline styles referencing design tokens
text(
    "Hello",
    style=f"color: {Colors.brand.primary_600}; font-size: 1rem;"
)
```

## Dependency Injection Benefits

### 1. Testability
Components can be tested in isolation with mock data

### 2. Reusability
Same component works in multiple contexts (pages, modals, showcases)

### 3. Maintainability
Changes to business logic don't require component changes

### 4. Flexibility
Components adapt to different use cases via configuration

### 5. Separation of Concerns
- **Components**: Presentation only
- **Routes**: HTTP handling, data fetching
- **Services**: Business logic, database operations
- **Design System**: Styling and theming

## Example: Complete Flow

```python
# your_app/routes/users.py
from components_library import data_table, base_page

def list_users(req: Request):
    """Route handles data fetching."""
    # Business logic
    with Session(engine) as session:
        users = session.query(User).all()

    # Transform data
    user_data = [
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ]

    # Inject data into component
    return base_page(
        data_table(
            data=user_data,  # Injected
            columns=[
                {"key": "name", "label": "Name"},
                {"key": "email", "label": "Email"},
            ],
        ),
        title="Users"
    )
```

## Shared Utilities

The library provides shared utilities that follow the same DI principles - they receive configuration rather than reading from global state.

### API Client

The library includes an API client for backend services:

```python
# Library provides the tool (no config dependencies)
from components_library.api.rest import ApiClient
from components_library.api import ApiResponse, ApiSuccess, ApiFailure

# Application provides configuration
client = ApiClient(
    base_url=settings.api_base_url,  # Injected from app config
    timeout=settings.api_timeout,
)

# Use in services
async def fetch_items(client: ApiClient, query: str) -> list[dict]:
    response = await client.get("/items", params={"q": query})
    if isinstance(response, ApiSuccess):
        return response.data
    raise Exception(response.error.message)
```

**Key principles:**
- `ApiClient` requires explicit `base_url` (no hidden defaults)
- Version-specific clients (`v2`, future `v3`) share the same interface via `ApiClientProtocol`
- Applications create configured instances and inject them

### Session Utilities

Stateless session management functions for Starlette-based apps:

```python
from components_library import (
    SessionToken,
    get_session_tokens,
    add_session_token,
    remove_session_token,
)

# In a route handler
@rt("/api/tokens/add")
def add_token(req: Request, name: str, token_type: str):
    token = SessionToken(id=str(uuid4()), name=name, type=token_type)
    tokens = add_session_token(req, token)
    return token_list_partial(tokens)
```

**Key principles:**
- Pure functions with no global state
- Session key is configurable (defaults to `"search_tokens"`)
- `SessionToken` is a Pydantic model for validation

## Summary

This library uses dependency injection throughout:

1. **Data Injection**: Components receive data as parameters
2. **Behavior Injection**: Configuration is passed as parameters
3. **Composition**: Components accept children as dependencies
4. **Pure Components**: No side effects, no data fetching
5. **Business Logic Separation**: Routes/services handle logic, components handle presentation
6. **Shared Utilities**: API clients and session helpers receive configuration, not global state

The architecture ensures components remain:
- **Untouched by business logic**
- **Flexible and reusable**
- **Testable in isolation**
- **Configurable for different contexts**
