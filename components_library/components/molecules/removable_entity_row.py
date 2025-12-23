"""Removable Entity Row molecule - List item with avatar, text, and remove button."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Button, Div

from ...components.atoms import avatar, icon, text
from ...utils import merge_classes


def removable_entity_row(
    name: str,
    remove_url: str,
    remove_target: str,
    image_url: str | None = None,
    href: str = "#",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    A row displaying an entity (avatar + name) with a remove button.
    Useful for list management (e.g., characters in a scene).

    Args:
        name: Name of the entity
        remove_url: HTMX DELETE URL
        remove_target: HTMX target for the delete action
        image_url: Avatar URL
        href: URL to link the entity name/avatar to
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div containing the row
    """
    # Avatar component
    avatar_comp = (
        avatar(
            image_url=image_url,
            name=name,
            size=32,
        )
        if image_url
        else Div(
            name[0].upper(),
            style="width: 32px; height: 32px; border-radius: 50%; background: var(--theme-accent-secondary); display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;",
        )
    )

    style = "padding: 0.5rem; background: rgba(0,0,0,0.2); border-radius: 0.5rem;"
    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(
        Div(
            A(
                Div(
                    avatar_comp,
                    text(name, style="color: white; font-weight: 500;"),
                    style="display: flex; gap: 0.5rem; align-items: center;",
                ),
                href=href,
                style="text-decoration: none; flex: 1;",
            ),
            Button(
                icon("x", size="sm"),
                type="button",
                hx_delete=remove_url,
                hx_target=remove_target,
                hx_swap="outerHTML",
                style="background: transparent; border: none; color: var(--theme-text-muted); cursor: pointer; padding: 0.25rem;",
            ),
            style="display: flex; justify-content: space-between; align-items: center; width: 100%;",
            cls="w-full",
        ),
        style=style,
        cls=merge_classes("removable-entity-row", cls),
        **kwargs,
    )
