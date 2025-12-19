"""Modal component - Dialog overlay.

Uses native HTML <dialog> element for accessibility and built-in modal behavior.
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Dialog, Div

from ...design_system.tokens import BorderRadius, Colors, Shadows, Spacing
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()
shadows = Shadows()
radius = BorderRadius()


def modal(
    *content: Any,
    modal_id: str,
    title: str | None = None,
    footer: Any = None,
    size: str = "500px",
    open: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Dialog:
    """
    Modal dialog component using native HTML dialog element.

    The dialog must be opened via HTMX or by adding the 'open' attribute.
    Use hx-on::after-request="document.getElementById('modal-id').showModal()"
    to open the modal after fetching content.

    Args:
        *content: Modal body content
        modal_id: Required unique ID for the dialog (used for opening/closing)
        title: Modal title/header
        footer: Modal footer content (buttons, etc.)
        size: Modal max-width (CSS value)
        open: Whether modal is initially open
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Dialog element with modal structure

    Example:
        >>> modal(
        ...     "Are you sure you want to delete this item?",
        ...     modal_id="confirm-delete",
        ...     title="Confirm Delete",
        ...     footer=hstack(
        ...         button("Cancel", variant="outline",
        ...                **{"hx-on:click": "this.closest('dialog').close()"}),
        ...         button("Delete", color_palette="red"),
        ...         gap=2
        ...     )
        ... )

    Opening the modal (from a button):
        >>> button("Open Modal",
        ...        **{"hx-on:click": "document.getElementById('my-modal').showModal()"})
    """
    css_class = merge_classes("modal", cls)

    # Modal styles
    modal_style = generate_style_string(
        max_width=size,
        width="100%",
        padding="0",
        border="none",
        border_radius=radius.lg,
        box_shadow=shadows.xl,
        background_color=colors.background,
    )

    # Modal container content
    modal_content = []

    # Header with close button
    if title:
        header_style = generate_style_string(
            display="flex",
            align_items="center",
            justify_content="space-between",
            padding=spacing._6,
            border_bottom=f"1px solid {colors.border}",
        )

        close_btn_style = generate_style_string(
            background="none",
            border="none",
            font_size="1.5rem",
            cursor="pointer",
            color=colors.text_secondary,
            padding="0",
            margin_left="auto",
        )

        modal_content.append(
            Div(
                title,
                Button(
                    "×",
                    type="button",
                    style=close_btn_style,
                    **{"hx-on:click": "this.closest('dialog').close()"},
                ),
                cls="modal-header",
                style=header_style,
            )
        )

    # Body
    body_style = generate_style_string(padding=spacing._6)
    modal_content.append(Div(*content, cls="modal-body", style=body_style))

    # Footer
    if footer:
        footer_style = generate_style_string(
            padding=spacing._6,
            border_top=f"1px solid {colors.border}",
            display="flex",
            justify_content="flex-end",
            gap=spacing._3,
        )
        modal_content.append(Div(footer, cls="modal-footer", style=footer_style))

    return Dialog(
        *modal_content,
        id=modal_id,
        cls=css_class,
        style=modal_style,
        open=open if open else None,
        **kwargs,
    )
