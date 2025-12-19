"""FilterPanel molecule - Advanced filter panel with collapsible sections."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Input
from pydantic import BaseModel

from ..atoms import (
    accordion,
    accordion_item,
    box,
    button,
    checkbox,
    flex,
    hstack,
    radio,
    text,
    tooltip,
    vstack,
)


class FilterGroup(BaseModel):
    """Filter group data structure."""

    id: str
    title: str
    type: Literal["radio", "checkbox", "range", "custom"]
    description: str | None = None
    help_text: str | None = None
    options: list[tuple[str, str, bool]] | None = None  # (value, label, disabled)
    value: str | list[str] | int | None = None
    min_val: int | None = None
    max_val: int | None = None
    step: int | None = None
    custom_content: Any | None = None
    disabled: bool = False


def filter_panel(
    filters: list[FilterGroup],
    title: str = "Filters",
    reset_url: str | None = None,
    reset_target: str | None = None,
    reset_label: str = "Reset",
    default_open_filters: list[str] | None = None,
    min_width: str = "320px",
    max_width: str = "320px",
    variant: Literal["sidebar", "inline"] = "sidebar",
    size: Literal["sm", "md", "lg"] = "md",
    **kwargs: Any,
) -> Any:
    """
    Filter panel molecule providing a collapsible filter interface.

    Supports radio buttons, checkboxes, range sliders, and custom content.
    Uses HTMX for interactions - no JavaScript required.

    Args:
        filters: List of FilterGroup objects defining the filters
        title: Title for the filter panel
        reset_url: HTMX endpoint URL for reset button
        reset_target: HTMX target selector for reset response
        reset_label: Label for reset button
        default_open_filters: List of filter IDs to be open by default
        min_width: Minimum width of the panel
        max_width: Maximum width of the panel
        variant: Display variant (sidebar or inline)
        size: Size of the component
        **kwargs: Additional HTML attributes

    Returns:
        Box element with filter panel

    Example:
        >>> filter_panel(
        ...     filters=[
        ...         FilterGroup(
        ...             id="status",
        ...             title="Status",
        ...             type="checkbox",
        ...             options=[("active", "Active", False), ("pending", "Pending", False)],
        ...             value=["active"]
        ...         )
        ...     ],
        ...     reset_url="/filters/reset",
        ...     reset_target="#filter-panel"
        ... )
    """
    if default_open_filters is None:
        default_open_filters = []

    def render_filter_content(filter_item: FilterGroup) -> Any:
        """Render the content for a filter based on its type."""
        if filter_item.type == "radio":
            # Radio buttons
            radio_options = []
            for value, label, option_disabled in filter_item.options or []:
                radio_options.append(
                    radio(
                        name=filter_item.id,
                        value=value,
                        label=label,
                        checked=filter_item.value == value,
                        disabled=option_disabled or filter_item.disabled,
                    )
                )

            return vstack(*radio_options, gap=2, style="align-items: flex-start;")

        elif filter_item.type == "checkbox":
            # Checkboxes
            checkbox_options = []
            selected_values = filter_item.value if isinstance(filter_item.value, list) else []

            for value, label, option_disabled in filter_item.options or []:
                checkbox_options.append(
                    checkbox(
                        name=f"{filter_item.id}[]",
                        value=value,
                        label=label,
                        checked=value in selected_values,
                        disabled=option_disabled or filter_item.disabled,
                        style=f"font-size: {'0.875rem' if size == 'sm' else '1rem'};",
                    )
                )

            return vstack(*checkbox_options, gap=2, style="align-items: flex-start;")

        elif filter_item.type == "range":
            # Range slider
            return box(
                Input(
                    type="range",
                    name=filter_item.id,
                    min=filter_item.min_val or 0,
                    max=filter_item.max_val or 100,
                    step=filter_item.step or 1,
                    value=filter_item.value or 0,
                    disabled=filter_item.disabled,
                    style="width: 100%; margin-bottom: 0.5rem;",
                ),
                text(
                    str(filter_item.value),
                    style="font-size: 0.875rem; color: var(--color-gray-600); text-align: center;",
                ),
                style="width: 100%;",
            )

        elif filter_item.type == "custom":
            # Custom content
            return filter_item.custom_content

        return None

    # Build filter accordion items
    accordion_items = []
    for filter_item in filters:
        # Build item content
        item_content = vstack(
            text(
                filter_item.description,
                style="font-size: 0.875rem; color: var(--color-gray-600); margin-bottom: 1rem; text-align: left;",
            )
            if filter_item.description
            else None,
            render_filter_content(filter_item),
            gap=0,
        )

        # Build item title with optional help tooltip
        if filter_item.help_text:
            item_title = hstack(
                text(
                    filter_item.title,
                    style=f"font-weight: 500; font-size: {'0.875rem' if size == 'sm' else '1rem'}; text-align: left; flex: 1;",
                ),
                tooltip("ℹ️", filter_item.help_text, position="top"),
                gap=2,
                style="flex: 1;",
            )
        else:
            item_title = text(
                filter_item.title,
                style=f"font-weight: 500; font-size: {'0.875rem' if size == 'sm' else '1rem'}; text-align: left;",
            )

        accordion_items.append(
            accordion_item(
                item_title,
                item_content,
                open=filter_item.id in default_open_filters,
            )
        )

    # Build reset button with HTMX if URL provided
    reset_btn = None
    if reset_url:
        reset_attrs: dict[str, Any] = {"hx-get": reset_url}
        if reset_target:
            reset_attrs["hx-target"] = reset_target
        reset_btn = button(
            reset_label, variant="ghost", size="sm", color_palette="gray", **reset_attrs
        )

    # Build the header
    header = flex(
        text(
            title,
            style=f"font-weight: 600; font-size: {('1.125rem' if size == 'lg' else '1rem')};",
        ),
        reset_btn,
        style="justify-content: space-between; align-items: center; padding: 1.5rem 1.5rem 1rem;"
        if variant == "sidebar"
        else "justify-content: space-between; align-items: center; padding-bottom: 1rem;",
    )

    # Styles based on variant
    if variant == "sidebar":
        panel_style = f"""
            min-width: {min_width};
            max-width: {max_width};
            border-left: 1px solid var(--color-gray-200);
            border-right: 1px solid var(--color-gray-200);
            border-bottom: 1px solid var(--color-gray-200);
            background-color: white;
        """
    else:
        panel_style = """
            border: 1px solid var(--color-gray-200);
            border-radius: 0.375rem;
            background-color: white;
            padding: 1rem;
        """

    return box(
        header,
        accordion(*accordion_items),
        style=panel_style,
        **kwargs,
    )
