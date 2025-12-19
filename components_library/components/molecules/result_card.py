"""Result card molecule - Clickable card for displaying item information."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import button, hstack, text, vstack


def result_card(
    item_id: str | int,
    item_name: str,
    detail_url: str | None = None,
    record_id: int | None = None,
    show_arrow: bool = True,
    hx_target: str = "#search-results",
    hx_swap: str = "innerHTML",
    push_url: bool = True,
    id_label: str = "ID",
    **kwargs: Any,
) -> Div:
    """
    Result card - clickable card displaying item information.

    Creates a touch-optimized card with item name and ID that can be
    clicked to view details. Commonly used in search results and
    item listings. Uses HTMX for partial page updates.

    Args:
        item_id: The item's ID number
        item_name: Display name of the item
        detail_url: URL for viewing item details (defaults to /item/{record_id})
        record_id: Database record ID (used for default URL)
        show_arrow: Whether to show the arrow indicator (default: True)
        hx_target: HTMX target selector for content injection (default: "#search-results")
        hx_swap: HTMX swap strategy (default: "innerHTML")
        push_url: Whether to update browser URL (default: True)
        id_label: Label for the ID field (default: "ID")
        **kwargs: Additional HTML attributes

    Returns:
        Clickable result card

    Example:
        >>> # Standard usage with navigation
        >>> result_card(
        ...     item_id=123,
        ...     item_name="Example Item",
        ...     record_id=1
        ... )
        >>> # Showcase usage without navigation
        >>> result_card(
        ...     item_id="ABC-001",
        ...     item_name="Another Item",
        ...     record_id=2,
        ...     push_url=False
        ... )
    """
    # Determine the URL
    url = detail_url or f"/item/{record_id or 0}"

    # Build the card content
    content = vstack(
        vstack(
            text(
                item_name,
                weight="medium",
                cls="item-name",
                style=(
                    "overflow: hidden; "
                    "text-overflow: ellipsis; "
                    "word-wrap: break-word; "
                    "word-break: break-word; "
                    "line-height: 1.4; "
                    "display: -webkit-box; "
                    "-webkit-line-clamp: 3; "  # Allow up to 3 lines
                    "-webkit-box-orient: vertical; "
                    "hyphens: auto; "  # Better text breaking
                ),
            ),
            text(
                f"{id_label}: {item_id}",
                variant="caption",
                cls="item-id",
                style="overflow: hidden; text-overflow: ellipsis; margin-top: 0.5rem;",
            ),
            gap=1,
            style="flex: 1; min-width: 0;",
        ),
        hstack(
            text("→", cls="arrow-icon", style="flex-shrink: 0; margin-left: auto;")
            if show_arrow
            else None,
            justify="end",
            align="center",
            style="margin-top: auto;",
        )
        if show_arrow
        else None,
        gap=2,
        style="height: 100%; width: 100%;",
    )

    # Extract cls from kwargs or use default
    component_cls = kwargs.pop("cls", "result-card")

    # Build button attributes with HTMX configuration
    button_attrs: dict[str, Any] = {
        "variant": "ghost",
        "size": "lg",
        "cls": "result-item touch-target",
        "hx_get": url,
        "hx_target": hx_target,
        "hx_swap": hx_swap,
        "style": (
            "width: 100%; "
            "height: 160px; "  # Fixed height for consistency
            "padding: 1.25rem; "
            "border: 1px solid #e5e7eb; "
            "border-radius: 12px; "
            "background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); "  # Subtle gradient
            "overflow: hidden; "
            "display: flex; "
            "flex-direction: column; "
            "justify-content: space-between; "
            "transition: all 0.2s ease; "
            "cursor: pointer; "
            "box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.1); "
            "position: relative; "
            "border-left: 4px solid #3b82f6; "  # Subtle blue accent
        ),
    }

    # Add push_url only if True
    if push_url:
        button_attrs["hx_push_url"] = "true"

    # Merge component_cls with button_attrs
    button_attrs["cls"] = f"{button_attrs.get('cls', '')} {component_cls}".strip()

    return button(content, **button_attrs, **kwargs)
