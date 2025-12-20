"""Chip Select component - Multi-select with toggleable chip buttons."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Input, Label, Style

from ...design_system.tokens import BorderRadius, Colors, Spacing, Transitions
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()
radius = BorderRadius()
transitions = Transitions()


def chip_select(
    name: str,
    options: list[tuple[str, str]] | list[str],
    selected: list[str] | None = None,
    size: Literal["sm", "md", "lg"] = "md",
    disabled: bool = False,
    required: bool = False,
    aria_label: str | None = None,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_trigger: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Multi-select component with toggleable chip-style buttons.

    Renders a group of checkbox inputs styled as pill-shaped chips that
    users can toggle on/off. Useful for selecting multiple tags, categories,
    or attributes.

    Args:
        name: Input name attribute (all chips share this name for form submission)
        options: List of options as (value, label) tuples or strings
        selected: List of currently selected values
        size: Chip size (sm, md, lg)
        disabled: Whether all chips are disabled
        required: Whether at least one selection is required
        aria_label: Accessible label for the group
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint (triggered on change)
        hx_post: HTMX POST endpoint (triggered on change)
        hx_trigger: HTMX trigger event (default: "change")
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Div containing styled checkbox chips

    Example:
        >>> # Basic usage
        >>> chip_select(
        ...     name="tags",
        ...     options=["Dark", "Hopeful", "Gritty"],
        ...     selected=["Dark"]
        ... )

        >>> # With value/label tuples
        >>> chip_select(
        ...     name="genre",
        ...     options=[("sci_fi", "Sci-Fi"), ("fantasy", "Fantasy")],
        ...     selected=["sci_fi"]
        ... )

        >>> # With HTMX
        >>> chip_select(
        ...     name="filters",
        ...     options=["Active", "Pending", "Completed"],
        ...     hx_post="/api/filter",
        ...     hx_target="#results"
        ... )
    """
    selected = selected or []
    css_class = merge_classes("chip-select", f"chip-select-{size}", cls)

    # Size-based padding
    padding_map = {
        "sm": f"{spacing._1} {spacing._3}",
        "md": f"{spacing._2} {spacing._4}",
        "lg": f"{spacing._3} {spacing._5}",
    }
    font_size_map = {
        "sm": "0.75rem",
        "md": "0.875rem",
        "lg": "1rem",
    }

    padding = padding_map.get(size, padding_map["md"])
    font_size = font_size_map.get(size, font_size_map["md"])

    # Build chip elements
    chips = []
    for i, opt in enumerate(options):
        if isinstance(opt, tuple):
            opt_value, opt_label = opt
        else:
            # opt is a string when not a tuple
            opt_str = str(opt)
            opt_value = opt_str.lower().replace("-", "_").replace(" ", "_")
            opt_label = opt_str

        chip_id = f"{name}-chip-{i}"
        is_selected = opt_value in selected

        # Build HTMX attributes for the checkbox
        input_attrs: dict[str, Any] = {
            "type": "checkbox",
            "name": name,
            "value": opt_value,
            "id": chip_id,
            "checked": is_selected,
            "disabled": disabled,
            "cls": "chip-select-input",
        }

        if hx_get:
            input_attrs["hx_get"] = hx_get
        if hx_post:
            input_attrs["hx_post"] = hx_post
        if hx_trigger:
            input_attrs["hx_trigger"] = hx_trigger
        elif hx_get or hx_post:
            input_attrs["hx_trigger"] = "change"
        if hx_target:
            input_attrs["hx_target"] = hx_target
        if hx_swap:
            input_attrs["hx_swap"] = hx_swap

        chip = Div(
            Input(**input_attrs),
            Label(
                opt_label,
                **{"for": chip_id},
                cls="chip-select-label",
            ),
            cls="chip-select-item",
        )
        chips.append(chip)

    # Container styles
    container_style = generate_style_string(
        display="flex",
        flex_wrap="wrap",
        gap=spacing._2,
    )

    # Inline styles for the chips (injected once)
    # Uses CSS variables for theming compatibility
    chip_styles = Style(f"""
        .chip-select-input {{
            position: absolute;
            opacity: 0;
            width: 0;
            height: 0;
            pointer-events: none;
        }}
        .chip-select-label {{
            display: inline-block;
            padding: {padding};
            border: 1px solid var(--theme-border, {colors.border});
            border-radius: {radius.full};
            cursor: pointer;
            transition: {transitions.fast};
            user-select: none;
            font-size: {font_size};
            background: transparent;
            color: var(--theme-text-primary, {colors.text_primary});
        }}
        .chip-select-label:hover {{
            border-color: var(--theme-accent-primary, {colors.primary.s500});
        }}
        .chip-select-input:checked + .chip-select-label {{
            background: var(--theme-accent-primary, {colors.primary.s500});
            border-color: var(--theme-accent-primary, {colors.primary.s500});
            color: white;
        }}
        .chip-select-input:disabled + .chip-select-label {{
            opacity: 0.5;
            cursor: not-allowed;
        }}
        .chip-select-input:disabled + .chip-select-label:hover {{
            border-color: var(--theme-border, {colors.border});
        }}
        .chip-select-item {{
            position: relative;
            display: inline-block;
        }}
    """)

    # Container attributes
    container_attrs: dict[str, Any] = {
        "cls": css_class,
        "style": container_style,
        "role": "group",
    }

    if aria_label:
        container_attrs["aria_label"] = aria_label

    if required:
        # Add data attribute for validation hint
        container_attrs["data_required"] = "true"

    return Div(
        chip_styles,
        *chips,
        **{**container_attrs, **kwargs},
    )
