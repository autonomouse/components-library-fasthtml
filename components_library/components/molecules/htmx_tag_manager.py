"""HTMX-based tag manager molecule - Pure HTMX implementation."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal

from fasthtml.common import Div

from ..atoms import button, heading, input, text, vstack
from ..atoms.separator import separator
from ..atoms.tag import tag
from .tag_manager import TagItem


def htmx_tag_manager(
    available_tags: list[TagItem],
    selected_tags: list[TagItem] | None = None,
    on_tag_toggle: Callable[[TagItem, bool], None] | None = None,  # noqa: ARG001
    on_create_tag: Callable[[str], None] | None = None,  # noqa: ARG001
    on_delete_tag: Callable[[str], None] | None = None,  # noqa: ARG001
    disabled: bool = False,
    max_tags: int | None = None,
    allow_create: bool = True,
    allow_delete: bool = False,
    placeholder: str = "Enter tag name",
    create_label: str = "Create tag",
    cancel_label: str = "Cancel",
    empty_message: str = "No tags available",
    trigger: Any | None = None,
    position: Literal["top", "bottom", "left", "right"] = "bottom",  # noqa: ARG001
    size: Literal["sm", "md", "lg"] = "md",
    color_palette: Literal["brand", "gray", "red", "green"] = "brand",
    **kwargs: Any,
) -> Any:
    """
    HTMX-based tag manager molecule.

    Uses pure HTMX for all interactions - no JavaScript required.
    All state changes are handled server-side via HTMX requests.

    Args:
        available_tags: List of available tag items
        selected_tags: Currently selected tags
        on_tag_toggle: Callback for tag toggle (server-side)
        on_create_tag: Callback for tag creation (server-side)
        on_delete_tag: Callback for tag deletion (server-side)
        disabled: Whether the manager is disabled
        max_tags: Maximum number of tags that can be selected
        allow_create: Whether new tags can be created
        allow_delete: Whether tags can be deleted
        placeholder: Placeholder text for tag input
        create_label: Label for create button
        cancel_label: Label for cancel button
        empty_message: Message when no tags available
        trigger: Custom trigger element
        position: Popover position (not used in HTMX version)
        size: Component size
        color_palette: Color scheme
        **kwargs: Additional HTML attributes

    Returns:
        Div element with HTMX-powered tag manager

    Example:
        >>> htmx_tag_manager(
        ...     available_tags=[TagItem(id="1", name="Important")],
        ...     selected_tags=[],
        ...     allow_create=True,
        ... )
    """
    selected_tags = selected_tags or []
    selected_ids = {tag.id for tag in selected_tags}

    # Tag selection buttons with HTMX
    tag_buttons = []
    for tag_item in available_tags:
        is_selected = tag_item.id in selected_ids
        tag_buttons.append(
            button(
                tag_item.name,
                variant="outline" if not is_selected else "solid",
                color_palette=color_palette if not is_selected else "brand",
                size=size,
                disabled=disabled
                or bool(max_tags and len(selected_tags) >= max_tags and not is_selected),
                hx_post="/api/tags/toggle",
                hx_vals=f'{{"tag_id": "{tag_item.id}", "selected": {str(not is_selected).lower()}}}',
                hx_target="#tag-manager-content",
                hx_swap="outerHTML",
                style=f"color: {tag_item.color};" if tag_item.color else None,
            )
        )

    # Create new tag form with HTMX
    create_form = vstack(
        heading("Create New Tag", level=4),
        input(
            name="new_tag_name",
            placeholder=placeholder,
            size=size,
            disabled=disabled,
        ),
        vstack(
            button(
                create_label,
                variant="solid",
                color_palette=color_palette,
                size=size,
                disabled=disabled,
                hx_post="/api/tags/create",
                hx_include="[name='new_tag_name']",
                hx_target="#tag-manager-content",
                hx_swap="outerHTML",
            ),
            button(
                cancel_label,
                variant="outline",
                color_palette="gray",
                size=size,
                hx_get="/api/tags/cancel-create",
                hx_target="#tag-manager-content",
                hx_swap="outerHTML",
            ),
            gap=2,
        ),
        gap=3,
        id="create-tag-form",
        style="display: none;",
    )

    # Show create form button
    show_create_btn = button(
        "+ Add Tag",
        variant="outline",
        color_palette=color_palette,
        size=size,
        disabled=disabled or not allow_create,
        hx_get="/api/tags/show-create",
        hx_target="#tag-manager-content",
        hx_swap="outerHTML",
        id="show-create-form",
    )

    # Selected tags display
    selected_tags_display = vstack(
        heading("Selected Tags", level=5),
        vstack(
            *[
                tag(
                    tag_item.name,
                    removable=allow_delete,
                    on_remove=f"/api/tags/remove/{tag_item.id}",
                    style=f"color: {tag_item.color};" if tag_item.color else None,
                )
                for tag_item in selected_tags
            ],
            gap=1,
        )
        if selected_tags
        else text(empty_message, variant="caption"),
        gap=2,
    )

    # Main content
    content = vstack(
        selected_tags_display,
        separator(),
        heading("Available Tags", level=5),
        vstack(*tag_buttons, gap=2) if tag_buttons else text(empty_message, variant="caption"),
        separator(),
        show_create_btn,
        create_form,
        gap=4,
        id="tag-manager-content",
    )

    return Div(
        trigger,
        content,
        style="position: relative; display: inline-block;",
        **kwargs,
    )
