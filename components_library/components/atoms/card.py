"""Card component - Content container with sections."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...utils import merge_classes


def card(
    *content: Any,
    header: Any = None,
    footer: Any = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Card component with optional header and footer.

    Args:
        *content: Card body content
        header: Optional header content
        footer: Optional footer content
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with card structure

    Example:
        >>> card(
        ...     text("Card body content"),
        ...     header=heading("Card Title", level=3),
        ...     footer=hstack(
        ...         button("Cancel", variant="outline"),
        ...         button("Save"),
        ...         gap=2
        ...     )
        ... )
    """
    css_class = merge_classes("card", cls)

    elements = []

    # Header
    if header:
        elements.append(Div(header, cls="card-header"))

    # Body
    elements.append(Div(*content, cls="card-body"))

    # Footer
    if footer:
        elements.append(Div(footer, cls="card-footer"))

    return Div(*elements, cls=css_class, **kwargs)
