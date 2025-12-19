"""Typography tokens for the design system."""

from __future__ import annotations

from pydantic import BaseModel


class FontSize(BaseModel, frozen=True):
    """Font size with line height."""

    size: str
    line_height: str


class Typography(BaseModel, frozen=True):
    """Design system typography tokens."""

    # Font families
    font_sans: str = (
        '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    )
    font_mono: str = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Monaco, Consolas, monospace'

    # Font sizes (using a type scale)
    xs: FontSize = FontSize(size="0.75rem", line_height="1rem")  # 12px
    sm: FontSize = FontSize(size="0.875rem", line_height="1.25rem")  # 14px
    base: FontSize = FontSize(size="1rem", line_height="1.5rem")  # 16px
    lg: FontSize = FontSize(size="1.125rem", line_height="1.75rem")  # 18px
    xl: FontSize = FontSize(size="1.25rem", line_height="1.75rem")  # 20px
    xl2: FontSize = FontSize(size="1.5rem", line_height="2rem")  # 24px
    xl3: FontSize = FontSize(size="1.875rem", line_height="2.25rem")  # 30px
    xl4: FontSize = FontSize(size="2.25rem", line_height="2.5rem")  # 36px
    xl5: FontSize = FontSize(size="3rem", line_height="1")  # 48px
    xl6: FontSize = FontSize(size="3.75rem", line_height="1")  # 60px
    xl7: FontSize = FontSize(size="4.5rem", line_height="1")  # 72px
    xl8: FontSize = FontSize(size="6rem", line_height="1")  # 96px
    xl9: FontSize = FontSize(size="8rem", line_height="1")  # 128px

    # Font weights
    font_thin: str = "100"
    font_extralight: str = "200"
    font_light: str = "300"
    font_normal: str = "400"
    font_medium: str = "500"
    font_semibold: str = "600"
    font_bold: str = "700"
    font_extrabold: str = "800"
    font_black: str = "900"
