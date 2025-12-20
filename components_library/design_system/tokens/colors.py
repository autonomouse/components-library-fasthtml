"""Color tokens for the design system."""

from __future__ import annotations

from pydantic import BaseModel


class ColorScale(BaseModel, frozen=True):
    """A color scale with multiple shades."""

    s50: str
    s100: str
    s200: str
    s300: str
    s400: str
    s500: str
    s600: str
    s700: str
    s800: str
    s900: str
    s950: str


class Colors(BaseModel, frozen=True):
    """Design system color tokens."""

    # Primary colors
    primary: ColorScale = ColorScale(
        s50="#eff6ff",
        s100="#dbeafe",
        s200="#bfdbfe",
        s300="#93c5fd",
        s400="#60a5fa",
        s500="#3b82f6",
        s600="#2563eb",
        s700="#1d4ed8",
        s800="#1e40af",
        s900="#1e3a8a",
        s950="#172554",
    )

    # Neutral colors
    neutral: ColorScale = ColorScale(
        s50="#fafafa",
        s100="#f5f5f5",
        s200="#e5e5e5",
        s300="#d4d4d4",
        s400="#a3a3a3",
        s500="#737373",
        s600="#525252",
        s700="#404040",
        s800="#262626",
        s900="#171717",
        s950="#0a0a0a",
    )

    # Success colors
    success: ColorScale = ColorScale(
        s50="#f0fdf4",
        s100="#dcfce7",
        s200="#bbf7d0",
        s300="#86efac",
        s400="#4ade80",
        s500="#22c55e",
        s600="#16a34a",
        s700="#15803d",
        s800="#166534",
        s900="#14532d",
        s950="#052e16",
    )

    # Warning colors
    warning: ColorScale = ColorScale(
        s50="#fffbeb",
        s100="#fef3c7",
        s200="#fde68a",
        s300="#fcd34d",
        s400="#fbbf24",
        s500="#f59e0b",
        s600="#d97706",
        s700="#b45309",
        s800="#92400e",
        s900="#78350f",
        s950="#451a03",
    )

    # Error colors
    error: ColorScale = ColorScale(
        s50="#fef2f2",
        s100="#fee2e2",
        s200="#fecaca",
        s300="#fca5a5",
        s400="#f87171",
        s500="#ef4444",
        s600="#dc2626",
        s700="#b91c1c",
        s800="#991b1b",
        s900="#7f1d1d",
        s950="#450a0a",
    )

    # Semantic color aliases (computed as regular fields with defaults)
    text_primary: str = "var(--theme-text-primary, #171717)"
    text_secondary: str = "var(--theme-text-secondary, #525252)"
    text_disabled: str = "var(--theme-text-disabled, #a3a3a3)"
    background: str = "var(--theme-background, #ffffff)"
    background_alt: str = "var(--theme-background-alt, #fafafa)"
    border: str = "var(--theme-border, #e5e5e5)"
    border_focus: str = "var(--theme-border-focus, #3b82f6)"
