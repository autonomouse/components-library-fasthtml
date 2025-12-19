"""SidebarLayout template - Layout with sidebar."""

from __future__ import annotations

from typing import Any

from ..atoms import box, hstack, text, vstack
from .page_container import page_container


def sidebar_layout(
    children: Any,
    sidebar: Any,
    title: str | None = None,
    sidebar_width: str = "320px",
    sidebar_position: str = "right",
    background: str = "var(--color-gray-50)",
    **kwargs: Any,
) -> Any:
    """
    Sidebar layout template providing a layout with main content area and sidebar.

    This template is designed for applications that need:
    - Main content area for primary content
    - Sidebar for filters, navigation, or secondary content
    - Responsive design that works on different screen sizes

    Args:
        children: Main content to render in the center area
        sidebar: Sidebar content (filters, navigation, etc.)
        title: Optional page title to display above content
        sidebar_width: Width of the sidebar
        sidebar_position: Position of sidebar ("left" or "right")
        background: Background color for the page
        **kwargs: Additional HTML attributes

    Returns:
        PageContainer with sidebar layout

    Example:
        >>> sidebar_layout(
        ...     vstack(
        ...         heading("Main Content", level=2),
        ...         text("Your main content goes here")
        ...     ),
        ...     sidebar=filter_bar(result_count=42),
        ...     title="My Page",
        ...     sidebar_position="right"
        ... )
    """
    # Build page title header if provided
    title_section = None
    if title:
        title_section = box(
            hstack(
                text(
                    title,
                    style="font-size: 1.5rem; font-weight: 700; color: var(--color-gray-900);",
                ),
                gap=3,
                style="align-items: center;",
            ),
            style="""
                background-color: white;
                border-bottom: 1px solid var(--color-gray-200);
                padding: 1rem 1.5rem;
            """,
        )

    # Build main layout based on sidebar position
    if sidebar_position == "left":
        layout_content = hstack(
            # Sidebar on left
            box(
                sidebar,
                style=f"""
                    width: {sidebar_width};
                    background-color: white;
                    border-right: 1px solid var(--color-gray-200);
                    overflow-y: auto;
                    max-height: calc(100vh - 120px);
                """,
            ),
            # Main content
            box(
                children,
                style="flex: 1; background-color: " + background + ";",
            ),
            gap=0,
            style="align-items: stretch; min-height: calc(100vh - 120px);",
        )
    else:
        layout_content = hstack(
            # Main content
            box(
                children,
                style="flex: 1; background-color: " + background + ";",
            ),
            # Sidebar on right
            box(
                sidebar,
                style=f"""
                    width: {sidebar_width};
                    background-color: white;
                    border-left: 1px solid var(--color-gray-200);
                    overflow-y: auto;
                    max-height: calc(100vh - 120px);
                """,
            ),
            gap=0,
            style="align-items: stretch; min-height: calc(100vh - 120px);",
        )

    # Combine title and layout
    content = vstack(title_section, layout_content, gap=0) if title_section else layout_content

    return page_container(
        content,
        background=background,
        padding="0",
        **kwargs,
    )
