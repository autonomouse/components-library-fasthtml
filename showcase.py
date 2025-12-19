#!/usr/bin/env python3
"""
Component Library Showcase Server.

Run with: python showcase.py
Or via: make showcase
"""

from typing import Any

from fasthtml.common import fast_app, serve

from components_library import base_page, button_link, heading, text, ui_showcase_page, vstack

app, rt = fast_app()


@rt("/")
def get() -> Any:
    """Home page with link to showcase."""
    return base_page(
        vstack(
            heading("Components Library", level=1),
            text("A Python component library for FastHTML applications."),
            vstack(
                button_link("View Component Showcase →", href="/showcase", variant="solid"),
                text("Browse all available components", variant="caption"),
                gap=1,
            ),
            gap=4,
            style="max-width: 32rem; margin: 4rem auto; text-align: center; padding: 2rem;",
        ),
        title="Components Library",
    )


@rt("/showcase")
def showcase() -> Any:
    """Component showcase page."""
    return ui_showcase_page(title="Components Library Showcase")


if __name__ == "__main__":
    print("\n  Components Library Showcase")
    print("  ============================")
    print("  Home:     http://localhost:6007/")
    print("  Showcase: http://localhost:6007/showcase")
    print("\n")
    serve(port=6007)
