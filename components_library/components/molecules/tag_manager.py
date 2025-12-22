"""TagManager molecule - Tag selection and management interface."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal

from fasthtml.common import Button as FtButton
from fasthtml.common import Details, Div, Summary
from pydantic import BaseModel

from ..atoms import (
    box,
    button,
    checkbox,
    field,
    flex,
    icon_button,
    input,
    text,
    vstack,
)


class TagItem(BaseModel):
    """Tag item data structure."""

    id: str
    name: str
    color: str | None = None
    disabled: bool = False


def tag_manager(
    available_tags: list[TagItem],
    selected_tags: list[TagItem] | None = None,
    on_tag_toggle: Callable[[TagItem, bool], None] | None = None,  # noqa: ARG001
    on_create_tag: Callable[[str], None] | None = None,
    on_delete_tag: Callable[[str], None] | None = None,
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
    Tag manager molecule providing a popover interface for managing tags.

    Supports selecting existing tags, creating new tags, and deleting tags.

    Args:
        available_tags: List of available TagItem objects
        selected_tags: List of currently selected TagItem objects
        on_tag_toggle: Callback when tag is toggled (receives tag, is_selected)
        on_create_tag: Callback when creating new tag (receives tag_name)
        on_delete_tag: Callback when deleting tag (receives tag_id)
        disabled: Whether the tag manager is disabled
        max_tags: Maximum number of tags that can be selected
        allow_create: Whether to allow creating new tags
        allow_delete: Whether to allow deleting tags
        placeholder: Placeholder for new tag input
        create_label: Label for create button
        cancel_label: Label for cancel button
        empty_message: Message when no tags are available
        trigger: Custom trigger element (default: icon button)
        position: Popover position
        size: Size of the component
        color_palette: Color palette for the component
        **kwargs: Additional HTML attributes

    Returns:
        Popover element with tag manager

    Example:
        >>> tag_manager(
        ...     available_tags=[
        ...         TagItem(id="1", name="Important"),
        ...         TagItem(id="2", name="Review"),
        ...     ],
        ...     selected_tags=[TagItem(id="1", name="Important")],
        ...     on_tag_toggle=lambda tag, selected: print(f"{tag.name}: {selected}")
        ... )
    """
    if selected_tags is None:
        selected_tags = []

    selected_tag_ids = [tag.id for tag in selected_tags]
    can_create_more = not max_tags or len(selected_tags) < max_tags

    # Default trigger if none provided
    if trigger is None:
        trigger = icon_button(
            "+",
            aria_label="Manage tags",
            variant="ghost",
            size=size,
            disabled=disabled,
        )

    # Build tag list
    tag_checkboxes = []
    if available_tags:
        for tag in available_tags:
            is_selected = tag.id in selected_tag_ids
            checkbox_disabled = (
                tag.disabled or disabled or (not is_selected and not can_create_more)
            )

            # Tag checkbox with delete button if allowed
            tag_row_children = [
                checkbox(
                    name=f"tag-{tag.id}",
                    value=tag.id,
                    label=tag.name,
                    checked=is_selected,
                    disabled=checkbox_disabled,
                    color_palette=color_palette,
                    style=f"color: {tag.color or 'var(--color-gray-700)'}; font-size: {'0.875rem' if size == 'sm' else '1rem'};",
                )
            ]

            if allow_delete and on_delete_tag:
                tag_row_children.append(
                    icon_button(
                        "🗑️",
                        aria_label=f"Delete {tag.name} tag",
                        variant="ghost",
                        size="xs",
                        color_palette="red",
                        disabled=disabled,
                    )
                )

            tag_row = flex(
                *tag_row_children,
                style="align-items: center; justify-content: space-between; width: 100%;",
            )
            tag_checkboxes.append(tag_row)

        tags_list = vstack(*tag_checkboxes, gap=3, style="width: 100%; align-items: flex-start;")
    else:
        tags_list = text(
            empty_message,
            style="font-size: 0.875rem; color: var(--color-gray-500); font-style: italic; text-align: center; padding: 1rem 0;",
        )

    # Create tag form using details/summary for CSS-only toggle (no JavaScript)
    create_tag_section = Details(
        Summary(
            "+ Create a tag",
            cls="create-tag-summary",
            style="""
                display: flex;
                align-items: center;
                justify-content: flex-start;
                padding: 0.5rem 0;
                cursor: pointer;
                font-weight: 400;
                color: var(--color-text-secondary);
                list-style: none;
            """,
        ),
        vstack(
            field(
                input(
                    name="new_tag_name",
                    placeholder=placeholder,
                    size=size,
                    id="new-tag-input",
                ),
                label="Tag name",
                label_for="new-tag-input",
            ),
            flex(
                # JS Exception: Closing a <details> element requires JS to remove
                # the 'open' attribute. Only the <summary> can toggle natively.
                FtButton(
                    cancel_label,
                    type="button",
                    cls="btn btn-outline btn-gray",
                    style="flex: 1;",
                    **{"hx-on:click": "this.closest('details').removeAttribute('open')"},
                ),
                button(
                    create_label,
                    color_palette=color_palette,
                    size=size,
                    style="flex: 1;",
                    id="create-tag-btn",
                ),
                gap="0.5rem",
            ),
            gap=3,
            style="align-items: stretch; padding-top: 0.5rem;",
        ),
        cls="create-tag-details",
        id="create-tag-form",
    )

    # Popover content
    content_children = [
        # Header
        box(
            text("Manage Tags", style="font-weight: 600; color: var(--color-gray-700);"),
            style="padding: 1rem; border-bottom: 1px solid var(--color-gray-100);",
        ),
        # Tags list
        box(
            tags_list,
            style="padding: 1rem; max-height: 250px; overflow-y: auto;",
        ),
    ]

    # Add create section if allowed
    if allow_create and on_create_tag:
        content_children.append(
            box(
                create_tag_section,
                style="padding: 1rem; border-top: 1px solid var(--color-gray-100);",
            )
        )

    # Add tag count indicator if max_tags is set
    if max_tags:
        count_text = f"{len(selected_tags)} / {max_tags} tags selected"
        if len(selected_tags) >= max_tags:
            count_text += " (Maximum reached)"

        content_children.append(
            box(
                text(
                    count_text,
                    style="font-size: 0.75rem; color: var(--color-gray-500); text-align: center;",
                ),
                style="padding: 0 1rem 0.5rem;",
            )
        )

    popover_content = box(
        *content_children,
        style="""
            width: 320px;
            max-height: 400px;
            border: 1px solid var(--color-gray-200);
            border-radius: 0.375rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            background-color: white;
        """,
    )

    return Div(
        trigger,
        popover_content,
        style="position: relative; display: inline-block;",
        **kwargs,
    )
