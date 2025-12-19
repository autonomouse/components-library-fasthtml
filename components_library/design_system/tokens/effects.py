"""Effect tokens for shadows, borders, and other visual effects."""

from __future__ import annotations

from pydantic import BaseModel


class Shadows(BaseModel, frozen=True):
    """Design system shadow tokens."""

    # Box shadows
    xs: str = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    sm: str = "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)"
    md: str = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
    lg: str = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
    xl: str = "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
    xl2: str = "0 25px 50px -12px rgba(0, 0, 0, 0.25)"
    inner: str = "inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)"
    none: str = "none"


class BorderRadius(BaseModel, frozen=True):
    """Design system border radius tokens."""

    none: str = "0"
    sm: str = "0.125rem"  # 2px
    base: str = "0.25rem"  # 4px
    md: str = "0.375rem"  # 6px
    lg: str = "0.5rem"  # 8px
    xl: str = "0.75rem"  # 12px
    xl2: str = "1rem"  # 16px
    xl3: str = "1.5rem"  # 24px
    full: str = "9999px"


class BorderWidth(BaseModel, frozen=True):
    """Design system border width tokens."""

    none: str = "0"
    default: str = "1px"
    _2: str = "2px"
    _4: str = "4px"
    _8: str = "8px"


class Transitions(BaseModel, frozen=True):
    """Design system transition tokens."""

    fast: str = "150ms"
    base: str = "200ms"
    slow: str = "300ms"
    slower: str = "500ms"

    # Easing functions
    ease_in: str = "cubic-bezier(0.4, 0, 1, 1)"
    ease_out: str = "cubic-bezier(0, 0, 0.2, 1)"
    ease_in_out: str = "cubic-bezier(0.4, 0, 0.2, 1)"


class ZIndex(BaseModel, frozen=True):
    """Design system z-index tokens."""

    base: int = 0
    dropdown: int = 1000
    sticky: int = 1100
    fixed: int = 1200
    modal_backdrop: int = 1300
    modal: int = 1400
    popover: int = 1500
    tooltip: int = 1600
