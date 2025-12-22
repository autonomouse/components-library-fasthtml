"""Kanban Board organism - horizontal scrolling container for kanban columns."""

from typing import Any

from fasthtml.common import Div


def kanban_board(
    *columns: Any,
    gap: str = "1.5rem",
    padding: str = "1rem",
    min_height: str = "400px",
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    A horizontal scrolling container for kanban-style columns.

    Args:
        *columns: kanban_column components to display
        gap: Gap between columns
        padding: Padding around the board
        min_height: Minimum height of the board
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Example:
        kanban_board(
            kanban_column("Act 1", scene_card(...)),
            kanban_column("Act 2", scene_card(...)),
            kanban_column("Act 3", scene_card(...)),
        )
    """
    from ...utils import merge_classes

    # Board container with horizontal scroll
    board_style = f"""
        display: flex;
        flex-direction: row;
        gap: {gap};
        padding: {padding};
        min-height: {min_height};
        overflow-x: auto;
        overflow-y: hidden;
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--theme-accent-primary, #00f0ff) transparent;
    """

    # WebKit scrollbar styling via CSS class
    scrollbar_css = """
        .kanban-board::-webkit-scrollbar {
            height: 8px;
        }
        .kanban-board::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
        }
        .kanban-board::-webkit-scrollbar-thumb {
            background: var(--theme-accent-primary, #00f0ff);
            border-radius: 4px;
            opacity: 0.5;
        }
        .kanban-board::-webkit-scrollbar-thumb:hover {
            opacity: 1;
        }
    """

    if "style" in kwargs:
        board_style = f"{board_style} {kwargs.pop('style')}"

    css_class = merge_classes("kanban-board", cls)

    # Include scrollbar styles inline (for Cloud Run compatibility)
    style_tag = Div(
        scrollbar_css,
        style="display: none;",
        cls="kanban-board-styles",
    )

    return Div(
        # Inject CSS as a style element
        Div(
            style_tag,
            Div(
                *columns,
                style=board_style,
                cls=css_class,
                **kwargs,
            ),
        ),
    )
