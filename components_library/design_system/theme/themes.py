"""Theme definitions for the design system.

This module defines available themes and provides utilities for theme switching.
Themes override CSS custom properties to change the look and feel of components.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class ThemeColors:
    """Color values for a theme."""

    bg_start: str
    bg_end: str
    accent_primary: str
    accent_secondary: str
    text_primary: str
    text_secondary: str
    card_bg: str
    card_border: str
    background: str  # Semi-transparent for inputs
    border: str
    autofill_bg: str  # Background for autofilled inputs


@dataclass(frozen=True)
class Theme:
    """Theme definition with metadata and colors."""

    id: str
    name: str
    description: str
    colors: ThemeColors


# Theme Definitions
THEMES: dict[str, Theme] = {
    "space": Theme(
        id="space",
        name="Space",
        description="Dark theme with cyan and purple accents",
        colors=ThemeColors(
            bg_start="#0a0a1f",
            bg_end="#1a1a3a",
            accent_primary="#00f0ff",
            accent_secondary="#7928ca",
            text_primary="#ffffff",
            text_secondary="#e0e0e0",
            card_bg="rgba(255, 255, 255, 0.03)",
            card_border="rgba(255, 255, 255, 0.1)",
            background="rgba(10, 10, 31, 0.6)",
            border="rgba(255, 255, 255, 0.1)",
            autofill_bg="#0a0a1f",
        ),
    ),
    "ocean": Theme(
        id="ocean",
        name="Ocean",
        description="Deep blue theme with teal accents",
        colors=ThemeColors(
            bg_start="#0a192f",
            bg_end="#112240",
            accent_primary="#64ffda",
            accent_secondary="#5ccfe6",
            text_primary="#ccd6f6",
            text_secondary="#8892b0",
            card_bg="rgba(100, 255, 218, 0.03)",
            card_border="rgba(100, 255, 218, 0.1)",
            background="rgba(10, 25, 47, 0.6)",
            border="rgba(100, 255, 218, 0.1)",
            autofill_bg="#0a192f",
        ),
    ),
    "sunset": Theme(
        id="sunset",
        name="Sunset",
        description="Warm dark theme with orange and pink accents",
        colors=ThemeColors(
            bg_start="#1a1423",
            bg_end="#2d1f3d",
            accent_primary="#ff6b6b",
            accent_secondary="#feca57",
            text_primary="#ffffff",
            text_secondary="#d4d4d8",
            card_bg="rgba(255, 107, 107, 0.03)",
            card_border="rgba(255, 107, 107, 0.1)",
            background="rgba(26, 20, 35, 0.6)",
            border="rgba(255, 107, 107, 0.1)",
            autofill_bg="#1a1423",
        ),
    ),
    "forest": Theme(
        id="forest",
        name="Forest",
        description="Dark green theme with emerald accents",
        colors=ThemeColors(
            bg_start="#0d1f17",
            bg_end="#1a3328",
            accent_primary="#10b981",
            accent_secondary="#34d399",
            text_primary="#ecfdf5",
            text_secondary="#a7f3d0",
            card_bg="rgba(16, 185, 129, 0.03)",
            card_border="rgba(16, 185, 129, 0.1)",
            background="rgba(13, 31, 23, 0.6)",
            border="rgba(16, 185, 129, 0.1)",
            autofill_bg="#0d1f17",
        ),
    ),
    "light": Theme(
        id="light",
        name="Light",
        description="Clean light theme with blue accents",
        colors=ThemeColors(
            bg_start="#ffffff",
            bg_end="#f8fafc",
            accent_primary="#3b82f6",
            accent_secondary="#8b5cf6",
            text_primary="#1e293b",
            text_secondary="#64748b",
            card_bg="rgba(255, 255, 255, 0.8)",
            card_border="rgba(0, 0, 0, 0.1)",
            background="rgba(255, 255, 255, 0.9)",
            border="rgba(0, 0, 0, 0.1)",
            autofill_bg="#ffffff",
        ),
    ),
}

# Default theme
DEFAULT_THEME = "space"

ThemeId = Literal["space", "ocean", "sunset", "forest", "light"]


def get_theme(theme_id: str) -> Theme:
    """Get a theme by ID, falling back to default if not found."""
    return THEMES.get(theme_id, THEMES[DEFAULT_THEME])


def get_available_themes() -> list[Theme]:
    """Get all available themes."""
    return list(THEMES.values())


def get_theme_css(theme_id: str) -> str:
    """
    Generate CSS that overrides theme variables for the specified theme.

    This CSS should be injected after the base styles to override the default theme.
    """
    theme = get_theme(theme_id)
    colors = theme.colors

    return f"""
        :root {{
            --theme-bg-start: {colors.bg_start};
            --theme-bg-end: {colors.bg_end};
            --theme-accent-primary: {colors.accent_primary};
            --theme-accent-secondary: {colors.accent_secondary};
            --theme-text-primary: {colors.text_primary};
            --theme-text-secondary: {colors.text_secondary};
            --theme-card-bg: {colors.card_bg};
            --theme-card-border: {colors.card_border};
            --theme-background: {colors.background};
            --theme-border: {colors.border};
            --theme-border-focus: {colors.accent_primary};
        }}

        /* Override autofill styles for this theme */
        input:-webkit-autofill,
        input:-webkit-autofill:hover,
        input:-webkit-autofill:focus,
        input:-webkit-autofill:active {{
            -webkit-box-shadow: 0 0 0px 1000px {colors.autofill_bg} inset !important;
        }}
    """
