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
    multiline: bool = False,
    rows: int = 3,
    font_weight: str | int = "800",
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    An input field styled to look like a heading, for inline editing.

    Args:
        value: Current text value
        name: Form field name
        post_url: HTMX POST URL for updates
        target: HTMX target selector (for swap)
        placeholder: Placeholder text
        level: Heading level (1-6) affecting font size
        multiline: Whether to use a textarea instead of input
        rows: Number of rows for textarea (if multiline=True)
        font_weight: Font weight (default 800)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Input or Textarea element styled as a heading
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
        font-weight: {font_weight};
        background: transparent;
        border: 1px solid transparent;
        border-radius: 4px;
        color: white;
        width: 100%;
        padding: 2px 4px;
        margin: -2px -4px;
        outline: none;
        transition: border-color 0.2s, background-color 0.2s;
    """

    # Merge with any style in kwargs
    if "style" in kwargs:
        base_style = f"{base_style} {kwargs.pop('style')}"

    # Common attributes
    attrs = {
        "name": name,
        "placeholder": placeholder,
        "style": base_style,
        "hx_post": post_url,
        "hx_target": target,
        "hx_swap": "outerHTML",
        "cls": merge_classes("editable-heading", cls),
        **kwargs,
    }

    if multiline:
        from fasthtml.common import Textarea

        # For textarea, we want to trigger on blur (change)
        attrs["hx_trigger"] = "blur"
        return Textarea(
            value or "",  # Textarea uses children or value, but safely pass content
            rows=rows,
            **attrs,
        )
    else:
        # For input, trigger on blur or Enter
        attrs["hx_trigger"] = "blur, keydown[key=='Enter']"
        return Input(type="text", value=value, **attrs)
