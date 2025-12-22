# Feature Development Guide

## Overview

This guide provides comprehensive instructions for developing features using the components-library-fasthtml package in FastHTML applications. Follow this guide to ensure consistency, maintainability, and quality across all components.

## Core Development Principles

**Develop components following atomic design principles with strict separation of concerns, defensive coding practices, and comprehensive testing. Use dependency injection to keep components pure and testable.**

## Table of Contents

1. [Architecture Requirements](#architecture-requirements)
2. [Component Development Standards](#component-development-standards)
3. [Atomic Design Principles](#atomic-design-principles)
4. [Component Audit Process](#component-audit-process)
5. [Service Layer Architecture](#service-layer-architecture)
6. [Theming and Styling](#theming-and-styling)
7. [Testing Requirements](#testing-requirements)
8. [Code Quality and Linting](#code-quality-and-linting)
9. [Minimize JavaScript](#minimize-javascript)
10. [HTMX Integration](#htmx-integration)
11. [Accessibility Guidelines](#accessibility-guidelines)
12. [Common Patterns and Examples](#common-patterns-and-examples)

## Architecture Requirements

### Clear Separation Between UI Components and Business Logic

**Enforce clear separation between UI components and business logic by isolating API interactions and data operations in routes and services.**

```python
# BAD: Business logic mixed with component
def user_profile() -> Div:
    # API logic directly in component
    engine = create_engine(settings.database_url)
    with Session(engine) as session:
        user = session.query(User).first()
        # Business logic in component
        display_name = f"{user.first_name} {user.last_name}"
        is_active = user.last_login > datetime.now() - timedelta(days=30)

    return card(
        heading(display_name),
        text("Active" if is_active else "Inactive"),
    )

# GOOD: Clear separation using dependency injection
def user_profile(
    user_name: str,
    is_active: bool,
    avatar_url: str | None = None,
) -> Div:
    """Pure component - receives data, doesn't fetch it."""
    return card(
        avatar(src=avatar_url, name=user_name) if avatar_url else None,
        heading(user_name, level=3),
        badge("Active" if is_active else "Inactive",
              color_palette="green" if is_active else "gray"),
    )

# Route handles business logic
@rt("/user/{user_id}")
def get_user(user_id: int):
    with Session(engine) as session:
        user = user_service.get_user(session, user_id)
        # Transform data
        return user_profile(
            user_name=f"{user.first_name} {user.last_name}",
            is_active=user.last_login > datetime.now() - timedelta(days=30),
            avatar_url=user.avatar_url,
        )
```

### Modular, Reusable Component Design

**Design components as modular, reusable functions that accept configuration via parameters.**

```python
# Component with configurable behavior
def result_card(
    item_id: str | int,
    title: str,
    description: str | None = None,
    # HTMX behavior injected via parameters
    hx_target: str = "#main-content",
    hx_swap: str = "innerHTML",
    push_url: bool = True,
    **kwargs: Any,
) -> Div:
    """Behavior is configured by caller, not hardcoded."""
    htmx_attrs = {
        "hx_get": f"/item/{item_id}",
        "hx_target": hx_target,
        "hx_swap": hx_swap,
    }
    if push_url:
        htmx_attrs["hx_push_url"] = "true"

    return card(
        heading(title, level=3),
        text(description) if description else None,
        style="cursor: pointer;",
        **htmx_attrs,
        **kwargs,
    )
```

## Component Development Standards

### Defensive Coding and Type Safety

**Code defensively with comprehensive type hints and sensible defaults.**

```python
from typing import Literal, Any
from fasthtml.common import Div, Button as FtButton

def button(
    *children: Any,
    variant: Literal["solid", "outline", "ghost"] = "solid",
    size: Literal["xs", "sm", "md", "lg"] = "md",
    color_palette: Literal["brand", "gray", "red", "green", "blue"] = "brand",
    loading: bool = False,
    disabled: bool = False,
    type: Literal["button", "submit", "reset"] = "button",
    **kwargs: Any,
) -> FtButton:
    """
    Button component with comprehensive prop validation.

    Args:
        children: Button content
        variant: Visual style variant
        size: Button size
        color_palette: Color scheme
        loading: Show loading state
        disabled: Disable button
        type: HTML button type
        **kwargs: Additional HTML attributes including HTMX

    Returns:
        FastHTML Button element
    """
    # Defensive: Handle edge cases
    is_disabled = disabled or loading

    # Build class string
    classes = merge_classes(
        "btn",
        f"btn-{variant}",
        f"btn-{size}",
        f"btn-{color_palette}",
        "btn-loading" if loading else None,
        kwargs.pop("cls", None),
    )

    return FtButton(
        *children,
        type=type,
        disabled=is_disabled,
        cls=classes,
        **kwargs,
    )
```

### Component Documentation

**Document all components with clear docstrings and usage examples.**

```python
def search_bar(
    placeholder: str = "Search...",
    hx_get: str | None = None,
    hx_target: str = "#search-results",
    hx_trigger: str = "input changed delay:300ms",
    hx_indicator: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Search bar with HTMX live search support.

    Args:
        placeholder: Input placeholder text
        hx_get: HTMX endpoint for search
        hx_target: Target element for results
        hx_trigger: HTMX trigger configuration
        hx_indicator: Loading indicator selector
        **kwargs: Additional attributes

    Returns:
        Div containing search input and optional button

    Example:
        search_bar(
            hx_get="/api/search",
            hx_target="#results",
            hx_indicator="#loading",
        )
    """
    ...
```

## Atomic Design Principles

Our component architecture follows Brad Frost's Atomic Design methodology:

### 1. Atoms (Basic Building Blocks)

**Location:** `components/atoms/`

Atoms are the fundamental building blocks - the smallest possible components.

**Examples:**
- `button` - Interactive buttons
- `text` - Typography elements
- `input` - Form inputs
- `icon` - SVG icons
- `badge` - Status indicators
- `card` - Container component

**Key Principles:**
- Highly reusable across the entire application
- No business logic
- Minimal dependencies
- Configurable via props

```python
# Atom example
def badge(
    *children: Any,
    variant: Literal["solid", "subtle", "outline"] = "subtle",
    color_palette: str = "gray",
    size: Literal["sm", "md", "lg"] = "md",
    **kwargs: Any,
) -> Span:
    """Basic badge atom component."""
    ...
```

### 2. Molecules (Simple Combinations)

**Location:** `components/molecules/`

Molecules combine atoms into functional groups.

**Examples:**
- `search_bar` - Input + button + icon
- `filter_panel` - Multiple filter controls
- `breadcrumbs` - Navigation path display
- `user_nav` - User menu with avatar

```python
# Molecule example - combines atoms
def search_bar(
    placeholder: str = "Search...",
    show_button: bool = True,
    **kwargs: Any,
) -> Div:
    """Search bar molecule composed of atoms."""
    return hstack(
        input(type="search", placeholder=placeholder, **kwargs),
        button(icon("search"), variant="ghost") if show_button else None,
        gap=2,
    )
```

### 3. Organisms (Complex Units)

**Location:** `components/organisms/`

Organisms are complex, self-contained sections built from molecules and atoms.

**Examples:**
- `data_table` - Table with sorting, pagination
- `header` - Page header with nav and user menu
- `notifications` - Notification dropdown system

```python
# Organism example
def header(
    logo_text: str = "App",
    logo_href: str = "/",
    breadcrumb_items: list[dict] | None = None,
    user_avatar: str | None = None,
    user_name: str | None = None,
    notification_count: int = 0,
    **kwargs: Any,
) -> HtmlHeader:
    """Page header organism with logo, breadcrumbs, user actions."""
    return HtmlHeader(
        hstack(
            logo(logo_text, href=logo_href),
            breadcrumbs(breadcrumb_items) if breadcrumb_items else None,
            Div(style="flex-grow: 1;"),
            user_actions(user_avatar, user_name, notification_count),
            justify="space-between",
        ),
        **kwargs,
    )
```

### 4. Templates (Page Layouts)

**Location:** `components/templates/`

Templates define page-level layouts.

**Examples:**
- `base_page` - Standard page with head elements
- `auth_page_layout` - Centered auth forms
- `centered_content` - Centered content wrapper

```python
# Template example
def base_page(
    *content: Any,
    title: str = "Labs App",
    description: str | None = None,
    include_htmx: bool = True,
    **kwargs: Any,
) -> Html:
    """Base page template with common head elements."""
    return Html(
        Head(
            Title(title),
            Meta(name="description", content=description) if description else None,
            base_styles(),
            component_styles(),
            htmx_script() if include_htmx else None,
        ),
        Body(
            *content,
            **kwargs,
        ),
    )
```

## Component Audit Process

### Pre-Development Checklist

Before creating a new component:

1. **Search for existing components:**
```bash
# Search in atoms
ls components_library/components/atoms/

# Search in molecules
ls components_library/components/molecules/

# Search in organisms
ls components_library/components/organisms/

# Search for similar functionality
grep -r "search" components_library/components/
```

2. **Check if existing component can be extended:**
   - Can you compose existing atoms into a new molecule?
   - Can you add parameters to an existing component?

3. **Document your audit:**
```python
"""
COMPONENT AUDIT RESULTS

Requirement: Need a card for displaying user info with actions

Existing Components Found:
- card (atom): Basic card structure - CAN REUSE
- avatar (atom): User profile image - CAN REUSE
- button (atom): Actions - CAN REUSE
- hstack/vstack (atoms): Layout - CAN REUSE

Decision: Create new user_card molecule using existing atoms
"""
```

## Service Layer Architecture

### Route-Level Business Logic

Keep all data operations in routes:

```python
# routes/users.py
@rt("/users")
def list_users(page: int = 1, per_page: int = 20):
    """Route handles data fetching and transformation."""
    with Session(engine) as session:
        users, total = user_service.list_users(session, page, per_page)

        user_data = [
            {
                "id": u.id,
                "name": f"{u.first_name} {u.last_name}",
                "email": u.email,
                "is_active": u.is_active,
            }
            for u in users
        ]

        return base_page(
            data_table(
                data=user_data,
                columns=[
                    {"key": "name", "label": "Name"},
                    {"key": "email", "label": "Email"},
                    {"key": "is_active", "label": "Status"},
                ],
                total_count=total,
                current_page=page,
            ),
            title="Users",
        )
```

### Service Layer (Optional)

For complex business logic, use a service layer:

```python
# services/user_service.py
class UserService:
    def __init__(self, session: Session):
        self.session = session

    def list_users(self, page: int, per_page: int) -> tuple[list[User], int]:
        offset = (page - 1) * per_page
        query = select(User).offset(offset).limit(per_page)
        users = self.session.execute(query).scalars().all()
        total = self.session.execute(select(func.count(User.id))).scalar()
        return list(users), total
```

## Theming and Styling

### Design Tokens

Use design tokens for consistent styling:

```python
from components_library import Colors, Spacing, Typography, Shadows

# Colors
primary = Colors.brand.primary_600
error = Colors.error.error_500
success = Colors.success.success_500

# Spacing
gap = Spacing.md      # "1rem"
padding = Spacing.lg  # "1.5rem"

# Typography
font_size = Typography.sizes.md
font_weight = Typography.weights.semibold

# Effects
shadow = Shadows.md
```

### Inline Styles

Components use inline styles for Cloud Run compatibility:

```python
def card(*content, **kwargs):
    style = generate_style_string(
        background_color=Colors.neutral.white,
        border_radius=BorderRadius.lg,
        box_shadow=Shadows.sm,
        padding=Spacing.md,
    )
    return Div(*content, style=style, **kwargs)
```

### Global Styles

Include base styles in your page template:

```python
from components_library import base_styles, component_styles

def my_page(*content):
    return Html(
        Head(
            base_styles(),      # Foundation CSS
            component_styles(), # Component-specific CSS
        ),
        Body(*content),
    )
```

## Testing Requirements

### Unit Tests

Test components in isolation:

```python
# tests/test_button.py
from components_library import button

def test_button_renders_text():
    result = button("Click me")
    html = str(result)
    assert "Click me" in html

def test_button_disabled_state():
    result = button("Click me", disabled=True)
    html = str(result)
    assert "disabled" in html

def test_button_loading_state():
    result = button("Click me", loading=True)
    html = str(result)
    assert "disabled" in html
    assert "loading" in html

def test_button_variants():
    for variant in ["solid", "outline", "ghost"]:
        result = button("Click me", variant=variant)
        html = str(result)
        assert f"btn-{variant}" in html
```

### Integration Tests

Test components with real data:

```python
def test_data_table_with_data():
    data = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ]
    columns = [
        {"key": "id", "label": "ID"},
        {"key": "name", "label": "Name"},
    ]

    result = data_table(data=data, columns=columns)
    html = str(result)

    assert "Item 1" in html
    assert "Item 2" in html
    assert "ID" in html
    assert "Name" in html
```

## Code Quality and Linting

### Makefile Commands

```bash
# Format code
make fmt

# Run linting and type checking
make check

# Run tests
make test

# Run all checks before committing
make fmt && make check && make test
```

### Type Checking

Use type hints for all functions:

```python
from typing import Literal, Any
from fasthtml.common import Div

def my_component(
    title: str,
    items: list[dict[str, Any]],
    variant: Literal["default", "compact"] = "default",
    **kwargs: Any,
) -> Div:
    ...
```

## Minimize JavaScript

**Prefer native HTML/CSS and HTMX over custom JavaScript.**

### Why Minimize JavaScript?

- **Simplicity**: Less code to maintain and debug
- **Performance**: Native browser features are optimized
- **Accessibility**: Semantic HTML works with assistive technologies
- **Cloud Run**: Stateless containers work best without client-side state

### Hierarchy of Solutions

When implementing interactive features, consider solutions in this order:

1. **HTML first**: Use semantic elements (`<details>`, `<dialog>`, `<form>`, `<datalist>`)
2. **CSS second**: Use modern CSS (`:has()`, `@container`, transitions, animations)
3. **HTMX third**: Use HTMX attributes for server interactions
4. **JavaScript last**: Only when no alternative exists

### Native HTML Examples

```python
# Collapsible content - no JS needed
Details(
    Summary("Show more"),
    Div("Hidden content revealed on click"),
)

# Modal dialog - native HTML
Dialog(
    heading("Confirm Action", level=2),
    P("Are you sure?"),
    Form(
        button("Cancel", formmethod="dialog"),
        button("Confirm", type="submit"),
        method="dialog",
    ),
    id="confirm-dialog",
)

# Autocomplete - native HTML
Input(
    type="text",
    list="suggestions",
    placeholder="Start typing...",
)
Datalist(
    Option(value="Option 1"),
    Option(value="Option 2"),
    id="suggestions",
)
```

### CSS-Only Interactions

```python
# Hover effects via CSS
card(
    heading("Hover me"),
    text("Content appears on hover"),
    cls="hover-reveal",  # CSS handles the interaction
)

# In component_styles():
# .hover-reveal .content { opacity: 0; transition: opacity 0.2s; }
# .hover-reveal:hover .content { opacity: 1; }
```

### When JavaScript Is Acceptable

- Complex animations not achievable with CSS transitions
- Third-party library integrations (charts, maps, rich text editors)
- Features with no HTML/CSS/HTMX equivalent
- Client-side calculations that don't require server state

**Important**: All JavaScript must be inline in `<script>` tags for Cloud Run compatibility.

---

## HTMX Integration

### Basic HTMX Attributes

```python
# Direct attributes
button(
    "Load More",
    hx_get="/api/items",
    hx_target="#results",
    hx_swap="beforeend",
)

# Using helper function
from components_library import htmx_attrs

attrs = htmx_attrs(
    get="/api/search",
    target="#results",
    trigger="input changed delay:300ms",
)
input(type="search", **attrs)
```

### Common Patterns

```python
# Live search
search_bar(
    hx_get="/api/search",
    hx_target="#search-results",
    hx_trigger="input changed delay:300ms",
    hx_indicator="#loading",
)

# Modal trigger
button(
    "Edit",
    **modal_trigger(
        modal_id="edit-modal",
        content_url="/api/edit-form/123",
    ),
)

# Confirm delete
button(
    "Delete",
    **confirm_delete(
        delete_url="/api/item/123",
        confirm_message="Are you sure?",
        target="#item-123",
    ),
)
```

## Accessibility Guidelines

### Semantic HTML

Use appropriate HTML elements:

```python
# Good: Semantic elements
def page_header(title: str, subtitle: str | None = None) -> HtmlHeader:
    return HtmlHeader(
        H1(title),
        P(subtitle) if subtitle else None,
    )

# Bad: Generic divs
def page_header(title: str, subtitle: str | None = None) -> Div:
    return Div(
        Div(title, style="font-size: 2rem;"),
        Div(subtitle) if subtitle else None,
    )
```

### ARIA Attributes

Include ARIA attributes where needed:

```python
def modal(
    *content,
    id: str,
    title: str,
    **kwargs,
) -> Div:
    return Div(
        *content,
        id=id,
        role="dialog",
        aria_modal="true",
        aria_labelledby=f"{id}-title",
        **kwargs,
    )
```

## Common Patterns and Examples

### Page with Search and Results

```python
def search_page():
    return base_page(
        heading("Search", level=1),

        search_bar(
            hx_get="/api/search",
            hx_target="#results",
            hx_trigger="input changed delay:300ms",
        ),

        Div(id="results"),

        title="Search",
    )

@rt("/api/search")
def search(q: str = ""):
    results = search_service.search(q)
    return search_results(
        results=[{"id": r.id, "name": r.name} for r in results],
        query=q,
    )
```

### Data Table with Pagination

```python
@rt("/items")
def items_page(page: int = 1):
    items, total = item_service.list_items(page, per_page=20)

    return base_page(
        data_table(
            data=[{"id": i.id, "name": i.name} for i in items],
            columns=[
                {"key": "id", "label": "ID"},
                {"key": "name", "label": "Name"},
            ],
        ),
        pagination(
            current_page=page,
            total_pages=(total + 19) // 20,
            hx_target="#main-content",
        ),
        title="Items",
    )
```

### Form with Validation

```python
def contact_form():
    return card(
        Form(
            field(
                input(type="text", name="name", required=True),
                label="Name",
                required=True,
            ),
            field(
                input(type="email", name="email", required=True),
                label="Email",
                required=True,
            ),
            field(
                textarea(name="message", required=True),
                label="Message",
                required=True,
            ),
            button("Send", type="submit", variant="solid"),
            hx_post="/api/contact",
            hx_target="#result",
        ),
        Div(id="result"),
    )
```

## Shared Utilities

Beyond UI components, the library provides reusable utilities for common application needs.

### API Client

An HTTP client for backend API calls. The library provides the client class; your application provides configuration:

```python
# In your app's services layer
from components_library.api.rest import ApiClient
from components_library.api import ApiSuccess, ApiFailure

# Create configured instance
client = ApiClient(
    base_url=settings.api_base_url,
    timeout=settings.api_timeout,
)

# Use in service functions
async def get_items(query: str, access_token: str) -> list[dict]:
    response = await client.get(
        "/items",
        params={"q": query},
        access_token=access_token,
    )
    if isinstance(response, ApiSuccess):
        return response.data
    raise Exception(response.error.message)
```

**Protocol**: All API clients implement the same `ApiClientProtocol` interface, enabling consistent usage patterns.

### Session Utilities

Stateless helpers for managing session data in Starlette-based apps:

```python
from components_library import (
    SessionToken,
    get_session_tokens,
    add_session_token,
    remove_session_token,
    toggle_session_operator,
    clear_session_tokens,
)

# Get current tokens
tokens = get_session_tokens(request)

# Add a token
token = SessionToken(id="123", name="BRCA1", type="gene")
tokens = add_session_token(request, token)

# Remove a token
tokens = remove_session_token(request, token_id="123")

# Toggle operator (AND/OR) at index
tokens = toggle_session_operator(request, index=1)

# Clear all tokens
clear_session_tokens(request)
```

**Customization**: All functions accept an optional `session_key` parameter (default: `"search_tokens"`) for using different session storage keys.

## Related Documentation

- [Dependency Injection Architecture](./dependency_injection_architecture.md)
- [Component Flexibility & HTMX](./component_flexibility.md)
- [Agentic Coding Guide](./agentic_coding_guide.md)
- [FastHTML Documentation](./fasthtml_llms.txt)
