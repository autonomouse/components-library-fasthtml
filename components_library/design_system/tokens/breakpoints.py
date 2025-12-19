"""Breakpoint tokens for responsive design."""

from __future__ import annotations

from pydantic import BaseModel


class Breakpoints(BaseModel, frozen=True):
    """Design system breakpoint tokens."""

    # Mobile-first breakpoints
    sm: str = "640px"  # Small devices (landscape phones)
    md: str = "768px"  # Medium devices (tablets)
    lg: str = "1024px"  # Large devices (desktops)
    xl: str = "1280px"  # Extra large devices
    xl2: str = "1536px"  # 2X Extra large devices

    # Aliases (computed as regular fields)
    tablet: str = "768px"  # Same as md
    desktop: str = "1024px"  # Same as lg
