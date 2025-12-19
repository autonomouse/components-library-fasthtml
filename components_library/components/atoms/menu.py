"""Menu component - Dropdown menu."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Div, Hr

from ...design_system.tokens import Colors, Shadows, Spacing
from ...utils import generate_style_string, merge_classes

colors = Colors()
shadows = Shadows()
spacing = Spacing()

# Menu item base style
_MENU_ITEM_STYLE = generate_style_string(
    display="block",
    padding=f"{spacing._2} {spacing._3}",
    color=colors.neutral.s700,
    text_decoration="none",
    font_size="0.875rem",
    white_space="nowrap",
    cursor="pointer",
    transition="background-color 0.15s",
)


def menu_item(
    text: str,
    href: str | None = None,
    icon: str | None = None,
    disabled: bool = False,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Menu item component.

    Args:
        text: Item text
        href: Link URL (if None, renders as Div)
        icon: Optional icon
        disabled: Whether item is disabled
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        **kwargs: Additional HTML attributes

    Returns:
        A or Div element

    Example:
        >>> menu_item("Profile", href="/profile")
        >>> menu_item("Settings", icon="⚙️", hx_get="/settings")
    """
    content = []
    if icon:
        content.append(icon + " ")
    content.append(text)

    style = _MENU_ITEM_STYLE
    if disabled:
        style = f"{style} pointer-events: none; opacity: 0.5;"

    attrs = {
        "cls": "menu-item" + (" menu-item-disabled" if disabled else ""),
        "style": style,
        **kwargs,
    }

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post

    if href and not disabled:
        return A(*content, href=href, **attrs)
    else:
        return Div(*content, **attrs)


def menu_divider() -> Any:
    """
    Menu divider component.

    Returns:
        Hr element

    Example:
        >>> menu_divider()
    """
    divider_style = generate_style_string(
        margin=f"{spacing._1} 0",
        border="none",
        border_top=f"1px solid {colors.border}",
    )
    return Hr(
        cls="menu-divider",
        style=divider_style,
    )


def menu(
    trigger: Any,
    *items: Any,
    position: str = "bottom-right",
    menu_id: str | None = None,
    group: str = "app-menus",
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Dropdown menu component using CSS-only toggle with details/summary.

    Uses the HTML `name` attribute to ensure only one menu in a group can
    be open at a time - clicking one menu automatically closes others.

    Args:
        trigger: Element that triggers the menu (usually a button or icon)
        *items: Menu items (use menu_item() and menu_divider())
        position: Menu position relative to trigger (bottom-left, bottom-right)
        menu_id: Optional ID for the menu (for styling or targeting)
        group: Group name for mutually exclusive menus (default: "app-menus").
               Menus with the same group name will close when another opens.
               Set to None to disable grouping.
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Details element with menu structure (CSS-only, no JavaScript)

    Example:
        >>> menu(
        ...     button("Actions"),
        ...     menu_item("Edit", icon="✏️", href="/edit"),
        ...     menu_item("Delete", icon="🗑️", hx_delete="/delete"),
        ...     menu_divider(),
        ...     menu_item("Settings", icon="⚙️", href="/settings"),
        ... )
    """
    from fasthtml.common import Details, Summary

    css_class = merge_classes("menu-wrapper", cls)

    # Position styles
    position_styles = {
        "bottom-left": "left: 0;",
        "bottom-right": "right: 0;",
    }
    pos_style = position_styles.get(position, position_styles["bottom-right"])

    # Menu content styles
    menu_style = generate_style_string(
        position="absolute",
        top="100%",
        z_index="1000",
        min_width="160px",
        margin_top=spacing._1,
        padding=f"{spacing._1} 0",
        background_color=colors.background,
        border=f"1px solid {colors.border}",
        border_radius="6px",
        box_shadow=shadows.md,
    )
    menu_style = f"{menu_style} {pos_style}"

    # Menu content
    menu_content = Div(
        *items,
        cls=f"menu menu-{position}",
        style=menu_style,
    )

    # Summary (trigger) styles - hide default arrow
    summary_style = generate_style_string(
        list_style="none",
        cursor="pointer",
        display="inline-flex",
    )

    # Wrapper styles
    wrapper_style = generate_style_string(
        position="relative",
        display="inline-block",
    )

    # Build attributes
    details_attrs: dict[str, Any] = {
        "cls": css_class,
        "style": wrapper_style,
        **kwargs,
    }
    if menu_id:
        details_attrs["id"] = menu_id
    if group:
        details_attrs["name"] = group

    return Details(
        Summary(
            trigger,
            style=summary_style,
        ),
        menu_content,
        **details_attrs,
    )
