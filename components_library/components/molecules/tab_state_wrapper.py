"""TabStateWrapper molecule - Tab state management."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import alert, empty_state, spinner, text, vstack


def tab_state_wrapper(
    children: Any,
    is_loading: bool = False,
    error: str | None = None,
    has_data: bool = True,
    has_search_entities: bool = True,
    search_prompt_title: str = "Search Required",
    search_prompt_description: str = "Search for a target to view data",
    search_prompt_icon: str = "🔍",
    empty_state_title: str = "No Data Found",
    empty_state_description: str = "No data found for the selected target",
    empty_state_icon: str = "ℹ️",
    loading_text: str = "Loading data...",
    error_title: str = "Error Loading Data",
    **kwargs: Any,
) -> Any:
    """
    Tab state wrapper molecule for handling common tab states.

    Provides consistent loading, empty, error, and search prompt states
    across all tab components in workflows.

    Args:
        children: Content to render when data is available
        is_loading: Whether data is loading
        error: Error message to display
        has_data: Whether data is available
        has_search_entities: Whether search entities are selected
        search_prompt_title: Title for search prompt state
        search_prompt_description: Description for search prompt state
        search_prompt_icon: Icon for search prompt state
        empty_state_title: Title for empty state
        empty_state_description: Description for empty state
        empty_state_icon: Icon for empty state
        loading_text: Text to show during loading
        error_title: Title for error alert
        **kwargs: Additional HTML attributes

    Returns:
        Div element with appropriate state content

    Example:
        >>> tab_state_wrapper(
        ...     table_content,
        ...     is_loading=False,
        ...     has_data=True,
        ...     has_search_entities=True
        ... )
    """
    # Show search prompt when no entities are selected
    if not has_search_entities:
        return vstack(
            empty_state(
                search_prompt_description,
                title=search_prompt_title,
                icon=search_prompt_icon,
            ),
            gap=4,
            style="align-items: center; justify-content: center; min-height: 400px;",
            **kwargs,
        )

    # Show loading state
    if is_loading:
        return vstack(
            spinner(size="lg"),
            text(loading_text),
            gap=4,
            style="align-items: center; justify-content: center; min-height: 400px;",
            **kwargs,
        )

    # Show error state
    if error:
        return vstack(
            alert(error, variant="error", title=error_title),
            gap=4,
            style="align-items: stretch;",
            **kwargs,
        )

    # Show empty state when no data
    if not has_data:
        return vstack(
            empty_state(
                empty_state_description,
                title=empty_state_title,
                icon=empty_state_icon,
            ),
            gap=4,
            style="align-items: center; justify-content: center; min-height: 400px;",
            **kwargs,
        )

    # Render children when data is available
    return Div(children, **kwargs)
