"""Helper functions for component development."""

from __future__ import annotations

from typing import Any


def merge_classes(*classes: str | None) -> str:
    """
    Merge multiple class names, filtering out None values.

    Args:
        *classes: Variable number of class names (can include None)

    Returns:
        Space-separated string of class names

    Example:
        >>> merge_classes("btn", "btn-primary", None, "btn-lg")
        "btn btn-primary btn-lg"
    """
    return " ".join(cls for cls in classes if cls)


def generate_style_string(**styles: Any) -> str:
    """
    Generate inline style string from keyword arguments.

    Args:
        **styles: CSS properties as keyword arguments (use underscores for hyphens)

    Returns:
        Semicolon-separated CSS string

    Example:
        >>> generate_style_string(padding="1rem", background_color="blue")
        "padding: 1rem; background-color: blue;"
    """
    if not styles:
        return ""

    css_props = []
    for key, value in styles.items():
        if value is not None:
            # Convert snake_case to kebab-case
            css_key = key.replace("_", "-")
            css_props.append(f"{css_key}: {value}")

    return "; ".join(css_props) + ";" if css_props else ""


def get_size_class(size: str, prefix: str = "size", mapping: dict[str, str] | None = None) -> str:
    """
    Generate a size-based class name.

    Args:
        size: Size variant (xs, sm, md, lg, xl)
        prefix: Class prefix
        mapping: Optional custom size mapping

    Returns:
        Size class name

    Example:
        >>> get_size_class("md", "btn")
        "btn-md"
    """
    if mapping and size in mapping:
        return f"{prefix}-{mapping[size]}"
    return f"{prefix}-{size}"


def get_variant_class(variant: str, prefix: str = "variant") -> str:
    """
    Generate a variant-based class name.

    Args:
        variant: Variant name
        prefix: Class prefix

    Returns:
        Variant class name

    Example:
        >>> get_variant_class("solid", "btn")
        "btn-solid"
    """
    return f"{prefix}-{variant}"
