"""FilterBar molecule - Filter controls sidebar."""

from __future__ import annotations

from typing import Any

from ..atoms import badge, button, checkbox, select, text, vstack


def filter_bar(
    result_count: int = 0,
    more_filters_url: str | None = None,
    more_filters_target: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Filter bar molecule providing filtering controls for search results.

    Displays time period selector, source selector, and result count in a sidebar layout.
    Uses HTMX for interactions - no JavaScript required.

    Args:
        result_count: Number of results to display
        more_filters_url: HTMX endpoint URL for "More filters" button
        more_filters_target: HTMX target selector for "More filters" response
        **kwargs: Additional HTML attributes

    Returns:
        VStack element with filter controls

    Example:
        >>> filter_bar(
        ...     result_count=42,
        ...     more_filters_url="/filters/advanced",
        ...     more_filters_target="#filter-panel"
        ... )
    """
    # Time period options
    time_period_options = [
        ("", "Select time period"),
        ("7d", "Last 7 days"),
        ("30d", "Last 30 days"),
        ("90d", "Last 90 days"),
        ("1y", "Last year"),
        ("all", "All time"),
    ]

    # Source options with default checked state
    source_options = [
        ("one", "One", True),
        ("two", "Two", True),
        ("three", "Three", True),
        ("toast", "Toast?", False),
    ]

    # Build time period section
    time_period_section = vstack(
        text(
            "Time Period",
            style="font-size: 0.875rem; font-weight: 500; color: var(--color-gray-700);",
        ),
        select(
            name="time_period",
            options=time_period_options,
            size="sm",
            placeholder="Select time period",
        ),
        gap=2,
        style="align-items: stretch;",
    )

    # Build sources section
    source_checkboxes = []
    for value, label_text, default_checked in source_options:
        source_checkboxes.append(
            checkbox(
                name="sources",
                value=value,
                label=label_text,
                checked=default_checked,
                color_palette="brand",
            )
        )

    sources_section = vstack(
        text(
            "SOURCES",
            style="font-size: 0.875rem; font-weight: 500; color: var(--color-gray-700);",
        ),
        vstack(*source_checkboxes, gap=3, style="align-items: stretch;"),
        gap=3,
        style="align-items: stretch;",
    )

    # More filters button with HTMX
    more_filters_attrs: dict[str, Any] = {
        "style": "align-self: flex-start;",
    }
    if more_filters_url:
        more_filters_attrs["hx-get"] = more_filters_url
        if more_filters_target:
            more_filters_attrs["hx-target"] = more_filters_target

    more_filters_btn = button(
        "⚙️ More filters",
        variant="outline",
        size="sm",
        color_palette="gray",
        **more_filters_attrs,
    )

    # Results count badge
    results_badge = badge(
        f"{result_count:,} results",
        variant="brand",
        size="sm",
        style="align-self: flex-start;",
    )

    return vstack(
        time_period_section,
        sources_section,
        more_filters_btn,
        results_badge,
        gap=4,
        style="""
            align-items: stretch;
            padding: 1rem;
            background-color: white;
            border-radius: 0.375rem;
            border: 1px solid var(--color-gray-200);
        """,
        **kwargs,
    )
