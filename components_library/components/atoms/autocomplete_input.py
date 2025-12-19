"""AutocompleteInput component - Input with autocomplete suggestions."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Input

from ...utils import merge_classes


def autocomplete_input(
    name: str,
    value: str | None = None,
    placeholder: str | None = None,
    size: Literal["sm", "md", "lg"] = "md",
    disabled: bool = False,
    required: bool = False,
    error: bool = False,
    # Dependency injection: URL endpoint for suggestions
    search_url: str | None = None,
    suggestions_target: str | None = None,
    debounce_ms: int = 300,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Input with HTMX-powered autocomplete suggestions.

    This component uses dependency injection: the search_url endpoint
    should return HTML with suggestion items.

    Args:
        name: Input name attribute
        value: Input value
        placeholder: Placeholder text
        size: Input size (sm, md, lg)
        disabled: Whether input is disabled
        required: Whether input is required
        error: Whether input has an error state
        search_url: URL endpoint for fetching suggestions (injected)
        suggestions_target: Target selector for suggestions (default: adjacent)
        debounce_ms: Debounce delay in milliseconds
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div containing input and suggestions container

    Example:
        >>> autocomplete_input(
        ...     name="search",
        ...     placeholder="Search items...",
        ...     search_url="/api/items/search",
        ... )

        # In your API endpoint:
        @app.get("/api/items/search")
        def search_items(q: str = ""):
            results = item_service.search(q)
            return Div(
                *[Div(r.name, cls="suggestion-item") for r in results],
                id="suggestions"
            )
    """
    css_class = merge_classes("autocomplete", cls)
    input_class = merge_classes(
        "input",
        f"input-{size}",
        "input-error" if error else None,
    )

    # Determine suggestions target
    target_id = suggestions_target or f"{name}-suggestions"

    # Build input with HTMX attributes
    input_attrs = {
        "type": "text",
        "name": name,
        "placeholder": placeholder,
        "cls": input_class,
        "disabled": disabled,
        "required": required,
        "autocomplete": "off",  # Disable browser autocomplete
    }

    if value is not None:
        input_attrs["value"] = value

    # HTMX autocomplete attributes
    if search_url:
        input_attrs["hx_get"] = search_url
        input_attrs["hx_trigger"] = f"keyup changed delay:{debounce_ms}ms, search"
        input_attrs["hx_target"] = f"#{target_id}"
        input_attrs["hx_swap"] = "innerHTML"
        # Include input value in request
        input_attrs["hx_include"] = f"[name='{name}']"

    input_element = Input(**{**input_attrs, **kwargs})

    # Container for suggestions (populated by HTMX)
    suggestions_container = Div(
        id=target_id,
        cls="autocomplete-suggestions",
        style="position: relative;",
    )

    return Div(
        input_element,
        suggestions_container,
        cls=css_class,
        style="position: relative;",
    )
