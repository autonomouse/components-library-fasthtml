"""Child Entries Section - A reusable carousel section for displaying child/sub-entries."""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from fasthtml.common import A, Div

from ..atoms.heading import heading
from ..atoms.icon import icon
from ..atoms.stack import vstack
from ..atoms.text import text
from .carousel import carousel


@dataclass
class ChildEntry:
    """Data class for a child entry to display in the carousel."""

    id: str
    title: str
    description: str | None = None
    icon_name: str = "file"
    href: str | None = None
    image_url: str | None = None


def _child_card(entry: ChildEntry) -> Any:
    """Render a single child entry card with optional image."""
    # Card with image background
    if entry.image_url:
        card_content = Div(
            # Background image with gradient overlay
            Div(
                style=f"""
                    position: absolute;
                    inset: 0;
                    background-image: url('{entry.image_url}');
                    background-size: cover;
                    background-position: center;
                    border-radius: 0.75rem;
                """,
            ),
            # Gradient overlay for text readability
            Div(
                style="""
                    position: absolute;
                    inset: 0;
                    background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 50%, rgba(0,0,0,0.2) 100%);
                    border-radius: 0.75rem;
                """,
            ),
            # Content
            vstack(
                heading(
                    entry.title,
                    level=4,
                    style="font-size: 1rem; font-weight: 600; color: white; margin: 0; text-shadow: 0 1px 3px rgba(0,0,0,0.5);",
                ),
                text(
                    (entry.description[:60] + "...")
                    if entry.description and len(entry.description) > 60
                    else (entry.description or ""),
                    style="font-size: 0.75rem; color: rgba(255,255,255,0.8); margin-top: 0.25rem; text-shadow: 0 1px 2px rgba(0,0,0,0.5);",
                )
                if entry.description
                else None,
                align="start",
                gap="0",
                style="position: relative; z-index: 1; margin-top: auto; padding: 1rem;",
            ),
            style="""
                position: relative;
                min-width: 200px;
                max-width: 240px;
                height: 140px;
                border-radius: 0.75rem;
                overflow: hidden;
                flex-shrink: 0;
                display: flex;
                flex-direction: column;
                border: 1px solid rgba(255,255,255,0.1);
                transition: transform 0.2s, box-shadow 0.2s;
            """,
            cls="hover:scale-[1.02] hover:shadow-lg",
        )
    else:
        # Card without image - icon-based
        card_content = Div(
            vstack(
                icon(entry.icon_name, size="md", style="color: var(--theme-accent-primary);"),
                heading(
                    entry.title,
                    level=4,
                    style="font-size: 0.95rem; font-weight: 600; color: white; margin: 0; text-align: center;",
                ),
                text(
                    (entry.description[:50] + "...")
                    if entry.description and len(entry.description) > 50
                    else (entry.description or ""),
                    style="font-size: 0.75rem; color: var(--theme-text-muted); text-align: center;",
                )
                if entry.description
                else None,
                align="center",
                justify="center",
                gap="0.5rem",
                style="height: 100%; padding: 1rem;",
            ),
            style="""
                min-width: 180px;
                max-width: 220px;
                height: 120px;
                border-radius: 0.75rem;
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(255,255,255,0.08);
                flex-shrink: 0;
                transition: transform 0.2s, background 0.2s;
            """,
            cls="hover:scale-[1.02] hover:bg-white/5",
        )

    # Wrap in link if href provided
    if entry.href:
        return A(
            card_content,
            href=entry.href,
            style="text-decoration: none; display: block;",
        )
    return card_content


def child_entries_section(
    entries: Sequence[ChildEntry],
    title: str = "Child Entries",
    empty_message: str | None = None,
    cls: str = "",
    style: str = "",
) -> Any:
    """
    A section displaying child entries in a horizontal scrolling carousel.

    This component renders a titled section with a carousel of cards, each representing
    a child entry. Cards show images when available, otherwise display an icon.

    Args:
        entries: List of ChildEntry objects to display.
        title: Section heading text.
        empty_message: Optional message to show when entries is empty.
                      If None and entries is empty, returns None.
        cls: Additional CSS classes.
        style: Additional inline styles.

    Returns:
        A vstack containing the section title and carousel, or None if empty
        and no empty_message provided.

    Example:
        >>> child_entries_section(
        ...     entries=[
        ...         ChildEntry(
        ...             id="1",
        ...             title="Dark Castle",
        ...             description="A foreboding fortress",
        ...             icon_name="map-pin",
        ...             href="/projects/1/locations/1",
        ...             image_url="https://example.com/castle.jpg",
        ...         ),
        ...     ],
        ...     title="Sub-Locations",
        ... )
    """
    if not entries:
        if empty_message:
            return Div(
                text(
                    empty_message,
                    style="color: var(--theme-text-muted); text-align: center; padding: 2rem;",
                ),
                cls=cls,
                style=style,
            )
        return None

    cards = [_child_card(entry) for entry in entries]

    return vstack(
        heading(
            title,
            level=3,
            style="font-size: 1.1rem; font-weight: 600; color: white; margin-bottom: 0.75rem;",
        ),
        carousel(cards, gap="1rem"),
        cls=f"w-full {cls}",
        style=f"margin-top: 2rem; {style}",
    )
