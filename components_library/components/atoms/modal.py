"""Modal component - Dialog overlay.

Uses native HTML <dialog> element for accessibility and built-in modal behavior.
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Dialog, Div, Form, Style

from ...design_system.tokens import BorderRadius, Colors, Shadows, Spacing
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()
shadows = Shadows()
radius = BorderRadius()

# Modal CSS for centering, backdrop, and theme colors
MODAL_CSS = """
dialog.modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin: 0;
    background: var(--theme-card-bg, var(--theme-background, #ffffff));
    color: var(--theme-text-primary, #171717);
    border: 1px solid var(--theme-card-border, var(--theme-border, #e5e5e5));
}
dialog.modal::backdrop {
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(4px);
}
dialog.modal[open] {
    display: flex;
    flex-direction: column;
}
dialog.modal .modal-header {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--theme-text-primary, #171717);
}
"""


def modal(
    *content: Any,
    modal_id: str,
    title: str | None = None,
    footer: Any = None,
    size: str = "500px",
    open: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
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
        Div containing modal styles and Dialog element

    Example:
        >>> modal(
        ...     "Are you sure you want to delete this item?",
        ...     modal_id="confirm-delete",
        ...     title="Confirm Delete",
        ...     footer=hstack(
        ...         Form(button("Cancel", variant="outline"), method="dialog"),
        ...         button("Delete", color_palette="red"),
        ...         gap=2
        ...     )
        ... )

    Opening the modal (from a button):
        JS Exception: showModal() is the native HTML5 dialog API - no CSS/HTMX alternative exists.
        >>> button("Open Modal",
        ...        **{"hx-on:click": "document.getElementById('my-modal').showModal()"})
    """
    css_class = merge_classes("modal", cls)

    # Modal styles (colors handled by MODAL_CSS for theme support)
    modal_style = generate_style_string(
        max_width=size,
        width="100%",
        padding="0",
        border_radius=radius.lg,
        box_shadow=shadows.xl,
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
            border_bottom="1px solid var(--theme-border, #e5e5e5)",
        )

        close_btn_style = generate_style_string(
            background="none",
            border="none",
            font_size="1.5rem",
            cursor="pointer",
            color="var(--theme-text-secondary, #525252)",
            padding="0",
            margin_left="auto",
        )

        # Use <form method="dialog"> for native dialog close (no JavaScript needed)
        modal_content.append(
            Div(
                title,
                Form(
                    Button("×", type="submit", style=close_btn_style),
                    method="dialog",
                    style="margin: 0; padding: 0;",
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
            border_top="1px solid var(--theme-border, #e5e5e5)",
            display="flex",
            justify_content="flex-end",
            gap=spacing._3,
        )
        modal_content.append(Div(footer, cls="modal-footer", style=footer_style))

    return Div(
        Style(MODAL_CSS),
        Dialog(
            *modal_content,
            id=modal_id,
            cls=css_class,
            style=modal_style,
            open=open if open else None,
            **kwargs,
        ),
    )
