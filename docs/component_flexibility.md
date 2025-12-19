# Component Flexibility & HTMX Configuration

## Overview

All components follow a flexible, configurable design pattern that allows them to be used in different contexts without hardcoding behavior. This aligns with HTMX-first design for partial page updates.

## Key Principles

### Minimize JavaScript

**Prefer native HTML/CSS and HTMX over custom JavaScript.**

When implementing interactive features, consider solutions in this order:

1. **HTML first**: Use semantic elements (`<details>`, `<dialog>`, `<form>`, `<datalist>`)
2. **CSS second**: Use modern CSS (`:has()`, `@container`, transitions, animations)
3. **HTMX third**: Use HTMX attributes for server interactions
4. **JavaScript last**: Only when no alternative exists

This approach ensures simplicity, better performance, accessibility, and Cloud Run compatibility.

### 1. Configurable HTMX Behavior

Components that trigger navigation or data fetching accept parameters to control:
- **Target**: Where content should be injected (`hx_target`)
- **Swap Strategy**: How content should be replaced (`hx_swap`)
- **URL Pushing**: Whether to update browser history (`hx_push_url`)

### 2. Context-Appropriate Defaults

- **Production context**: Full navigation with URL updates (default)
- **Showcase context**: Demonstrations without navigation (`push_url=False`)
- **Modal context**: Content injection into overlays

## Component Examples

### button

```python
from components_library import button

# Standard usage - full navigation
button(
    "View Details",
    hx_get="/item/123",
    hx_target="#main-content",
    hx_push_url="true",
)

# Showcase usage - no navigation
button(
    "View Details",
    hx_get="/item/123",
    hx_target="#main-content",
    # No hx_push_url
)

# Modal usage - inject into modal
button(
    "Quick View",
    hx_get="/item/123/preview",
    hx_target="#modal-body",
    hx_swap="innerHTML",
)
```

### card with HTMX

```python
from components_library import card, heading, text

# Clickable card with HTMX
card(
    heading("Item Title", level=3),
    text("Item description here"),
    hx_get="/item/123",
    hx_target="#main-content",
    hx_swap="innerHTML",
    hx_push_url="true",
    style="cursor: pointer;",
)
```

### search_bar

```python
from components_library import search_bar

# Live search with debounce
search_bar(
    hx_get="/api/search",
    hx_target="#search-results",
    hx_trigger="input changed delay:300ms",
    hx_indicator="#loading-spinner",
)
```

### data_table

```python
from components_library import data_table

# Table with sortable columns
data_table(
    data=items,
    columns=[
        {"key": "name", "label": "Name", "sortable": True},
        {"key": "status", "label": "Status"},
    ],
    hx_get="/api/items",
    hx_target="#table-container",
    hx_trigger="click from:.sortable-header",
)
```

## HTMX Helpers

The library provides utility functions for common HTMX patterns:

### htmx_attrs

```python
from components_library import htmx_attrs, button

# Generate HTMX attributes
attrs = htmx_attrs(
    get="/api/data",
    target="#content",
    swap="innerHTML",
    trigger="click",
)
button("Load Data", **attrs)
```

### debounced_search

```python
from components_library import debounced_search, input

# Create debounced search input
attrs = debounced_search(
    endpoint="/api/search",
    target="#results",
    delay=300,
)
input(type="search", placeholder="Search...", **attrs)
```

### modal_trigger

```python
from components_library import modal_trigger, button

# Button that opens a modal
attrs = modal_trigger(
    modal_id="edit-modal",
    content_url="/api/edit-form/123",
)
button("Edit", **attrs)
```

### confirm_delete

```python
from components_library import confirm_delete, button

# Delete button with confirmation
attrs = confirm_delete(
    delete_url="/api/item/123",
    confirm_message="Are you sure you want to delete this item?",
    target="#item-row-123",
    swap="outerHTML",
)
button("Delete", variant="danger", **attrs)
```

## Benefits

### Reusability
Components can be used in multiple contexts (pages, modals, showcases) without duplication

### Testability
Components can be tested in isolation without triggering actual navigation

### HTMX-First Design
All interactions use HTMX partial updates rather than full page reloads

### Flexibility
Developers can easily customize behavior for specific use cases

## HTMX Best Practices

### 1. Default to Partial Updates
Components should inject content into targets rather than full page navigation:
```python
hx_get="/api/endpoint"
hx_target="#content-area"
hx_swap="innerHTML"
```

### 2. Use URL Pushing Selectively
Only update browser history when necessary:
```python
# For major navigation
hx_push_url="true"

# For content updates/showcases
# Omit hx_push_url
```

### 3. Configure Targets Appropriately
```python
# Main content area
hx_target="#main-content"

# Modal overlay
hx_target="#modal-body"

# Inline replacement
hx_target="this"
hx_swap="outerHTML"
```

### 4. Use Loading Indicators
```python
from components_library import spinner

# Show spinner during request
button(
    "Load",
    hx_get="/api/data",
    hx_target="#content",
    hx_indicator="#loading",
)
spinner(id="loading", cls="htmx-indicator")
```

### 5. Handle Errors Gracefully
```python
from components_library import error_fallback

# Error display component
error_fallback(
    error="Failed to load data",
    show_retry=True,
    hx_get="/api/data",
    hx_target="#content",
)
```

## Complete Example

```python
from components_library import (
    base_page, card, heading, text, button,
    search_bar, data_table, modal, htmx_attrs
)

def list_page():
    return base_page(
        heading("Items", level=1),

        # Search with live results
        search_bar(
            hx_get="/api/items/search",
            hx_target="#items-table",
            hx_trigger="input changed delay:300ms",
        ),

        # Data table with sorting
        data_table(
            id="items-table",
            data=items,
            columns=[
                {"key": "name", "label": "Name", "sortable": True},
                {"key": "status", "label": "Status"},
            ],
            row_click_url="/item/{id}",
            hx_target="#main-content",
        ),

        # Add button opens modal
        button(
            "Add Item",
            **htmx_attrs(
                get="/item/new",
                target="#modal-body",
                swap="innerHTML",
            ),
            data_modal_trigger="add-modal",
        ),

        # Modal container
        modal(id="add-modal"),

        title="Items"
    )
```

## Related Documentation

- [Dependency Injection Architecture](./dependency_injection_architecture.md)
- [FastHTML Documentation](./fasthtml_llms.txt)
- [HTMX Documentation](https://htmx.org/docs/)
