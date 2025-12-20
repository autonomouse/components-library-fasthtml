#!/usr/bin/env python3
"""
Component Library Showcase Server.

Run with: python showcase.py
Or via: make showcase
"""

from typing import Any

from fasthtml.common import fast_app, serve

from components_library import (
    base_page,
    button_link,
    card,
    grid,
    heading,
    text,
    ui_showcase_page,
    vstack,
)
from components_library.design_system import get_available_themes, get_theme

app, rt = fast_app()


@rt("/")
def get() -> Any:
    """Home page with theme selection buttons."""
    themes = get_available_themes()

    # Create a card for each theme
    theme_cards = []
    for theme in themes:
        theme_cards.append(
            card(
                vstack(
                    heading(theme.name, level=3, size="lg"),
                    text(theme.description, variant="caption"),
                    button_link(
                        f"View in {theme.name} Theme →",
                        href=f"/showcase?theme={theme.id}",
                        variant="solid",
                        size="sm",
                        style=f"background: {theme.colors.accent_primary}; border-color: {theme.colors.accent_primary};",
                    ),
                    gap=3,
                    style="align-items: flex-start;",
                ),
                style=f"""
                    background: linear-gradient(135deg, {theme.colors.bg_start}, {theme.colors.bg_end});
                    border: 1px solid {theme.colors.card_border};
                    color: {theme.colors.text_primary};
                """,
            )
        )

    return base_page(
        vstack(
            heading("Components Library", level=1),
            text("A Python component library for FastHTML applications."),
            text("Select a theme to view the component showcase:", variant="caption"),
            grid(
                *theme_cards,
                columns=2,
                gap="1.5rem",
                style="margin-top: 1.5rem; width: 100%;",
            ),
            gap=4,
            style="max-width: 48rem; margin: 4rem auto; text-align: center; padding: 2rem;",
        ),
        title="Components Library",
    )


@rt("/showcase")
def showcase(theme: str | None = None) -> Any:
    """Component showcase page with optional theme."""
    # Get theme info for the title
    if theme:
        theme_info = get_theme(theme)
        title = f"Components Library - {theme_info.name} Theme"
    else:
        title = "Components Library Showcase"

    return ui_showcase_page(title=title, theme_id=theme)


if __name__ == "__main__":
    print("\n  Components Library Showcase")
    print("  ============================")
    print("  Home:     http://localhost:6007/")
    print("  Showcase: http://localhost:6007/showcase")
    print("  Themes:   http://localhost:6007/showcase?theme=space")
    print("            http://localhost:6007/showcase?theme=ocean")
    print("            http://localhost:6007/showcase?theme=sunset")
    print("            http://localhost:6007/showcase?theme=forest")
    print("            http://localhost:6007/showcase?theme=light")
    print("\n")
    serve(port=6007)
