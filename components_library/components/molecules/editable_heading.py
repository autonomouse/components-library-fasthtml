"""Editable Heading molecule - Input that looks like a heading."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Input

from ...utils import merge_classes


def editable_heading(
    value: str,
    name: str,
    post_url: str,
    target: str | None = None,
    placeholder: str = "",
    level: int = 1,
    cls: str | None = None,
    **kwargs: Any,
) -> Input:
    """
    An input field styled to look like a heading, for inline editing.

    Args:
        value: Current text value
        name: Form field name
        post_url: HTMX POST URL for updates
        target: HTMX target selector (for swap)
        placeholder: Placeholder text
        level: Heading level (1-6) affecting font size
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Input element styled as a heading
    """
    # Font sizes based on level (approximate tailwind/standard sizes)
    font_sizes = {
        1: "2.5rem",
        2: "2rem",
        3: "1.75rem",
        4: "1.5rem",
        5: "1.25rem",
        6: "1rem",
    }
    font_size = font_sizes.get(level, "2rem")

    base_style = f"""
        font-size: {font_size};
        font-weight: 800;
        background: transparent;
        border: none;
        border-bottom: 2px solid transparent;
        color: white;
        width: 100%;
        padding: 0;
        margin: 0;
        outline: none;
        transition: border-color 0.2s;
    """

    # Merge with any style in kwargs
    if "style" in kwargs:
        base_style = f"{base_style} {kwargs.pop('style')}"

    return Input(
        type="text",
        name=name,
        value=value,
        placeholder=placeholder,
        style=base_style,
        hx_post=post_url,
        hx_trigger="blur changed, keydown[key=='Enter']",
        hx_target=target,
        hx_swap="outerHTML",
        onfocus="this.style.borderBottomColor='#a855f7'",
        onblur="this.style.borderBottomColor='transparent'",
        cls=merge_classes("editable-heading", cls),
        **kwargs,
    )
