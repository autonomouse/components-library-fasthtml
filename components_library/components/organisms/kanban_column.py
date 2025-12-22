"""Kanban Column organism - a column for kanban-style boards."""

from typing import Any

from fasthtml.common import Div

from ...components.atoms import flex, heading


def kanban_column(
    title: str,
    *children: Any,
    header_action: Any | None = None,
    accent_color: str = "var(--theme-accent-primary, #00f0ff)",
    min_width: str = "300px",
    max_height: str | None = None,
    empty_message: str = "No items",
    column_id: str | None = None,
    sortable: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    A column component for kanban-style boards.

    Args:
        title: Column header title
        *children: Card components to display in the column
        header_action: Optional action element for the header (e.g., add button)
        accent_color: Color for header accent/underline
        min_width: Minimum column width
        max_height: Maximum height before scrolling (optional)
        empty_message: Message to show when column is empty
        column_id: Unique ID for this column (used for drag-and-drop)
        sortable: Enable Sortable.js drag-and-drop for this column
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Example:
        kanban_column(
            "Act 1",
            scene_card(...),
            scene_card(...),
            header_action=button("+", variant="ghost"),
            accent_color="#00f0ff",
            column_id="chapter-123",
            sortable=True,
        )
    """
    from ...components.atoms import text
    from ...utils import merge_classes

    # Header
    header_items = [
        heading(
            title,
            level=3,
            style=f"""
                font-size: 1.1rem;
                font-weight: 600;
                color: white;
                margin: 0;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid {accent_color};
            """,
        )
    ]
    if header_action:
        header_items.append(header_action)

    header = flex(
        *header_items,
        justify="between",
        align="center",
        style="margin-bottom: 1rem; width: 100%;",
    )

    # Content area - always include empty message for sortable columns
    content_items = list(children) if children else []

    # Add empty message that shows/hides based on content
    empty_display = "none" if content_items else "block"
    empty_msg = Div(
        text(
            empty_message,
            style="color: var(--theme-text-muted, #64748b); text-align: center; padding: 2rem 0;",
        ),
        cls="empty-message",
        style=f"display: {empty_display};",
    )

    # Scrollable content area style
    content_style = (
        "display: flex; flex-direction: column; gap: 0.75rem; width: 100%; min-height: 50px;"
    )
    if max_height:
        content_style += f" max-height: {max_height}; overflow-y: auto;"

    # Build content div with optional sortable attributes
    content_attrs: dict[str, Any] = {"style": content_style}
    if sortable:
        content_attrs["cls"] = "sortable-column"
        if column_id:
            content_attrs["data_column_id"] = column_id

    content = Div(
        empty_msg,
        *content_items,
        **content_attrs,
    )

    # Column container styles
    column_style = f"""
        min-width: {min_width};
        flex: 0 0 {min_width};
        background: rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1rem;
    """

    if "style" in kwargs:
        column_style = f"{column_style} {kwargs.pop('style')}"

    css_class = merge_classes("kanban-column", cls)

    return Div(
        header,
        content,
        style=column_style,
        cls=css_class,
        **kwargs,
    )
