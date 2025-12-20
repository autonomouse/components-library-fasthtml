"""Hero section for the marketing homepage."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H1, Div, P
from fasthtml.xtend import Style

from components_library.design_system.tokens import Spacing

from ...atoms import button_link, vstack

# Instantiate tokens
spacing = Spacing()


def hero_section(
    headline: str,
    subheadline: str,
    cta_text: str,
    cta_link: str,
    **kwargs: Any,
) -> Div:
    """
    Hero section with space theme, large typography, and primary CTA.

    Args:
        headline: Main title text.
        subheadline: Subtitle text.
        cta_text: Text for the call-to-action button.
        cta_link: URL for the call-to-action button.
        **kwargs: Additional HTML attributes.

    Returns:
        Hero section component.
    """

    hero_styles = Style("""
        .hero-container {
            position: relative;
            min-height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: radial-gradient(circle at center, #1a1a4a 0%, var(--marketing-bg-start) 70%);
            overflow: hidden;
            padding: 4rem 1rem;
        }

        .hero-content {
            position: relative;
            z-index: 10;
            max-width: 800px;
        }

        .hero-headline {
            font-size: 4rem;
            font-weight: 800;
            line-height: 1.1;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #fff 30%, var(--marketing-accent-primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem;
            text-shadow: 0 0 40px rgba(0, 240, 255, 0.3);
        }

        .hero-subheadline {
            font-size: 1.5rem;
            color: var(--marketing-text-secondary);
            margin-bottom: 2.5rem;
            font-weight: 400;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-glow {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 50% 50%, rgba(121, 40, 202, 0.15) 0%, transparent 60%);
            pointer-events: none;
            z-index: 1;
        }

        /* Floating stars/particles animation could be added here */

        @media (max-width: 768px) {
            .hero-headline {
                font-size: 2.5rem;
            }
            .hero-subheadline {
                font-size: 1.125rem;
            }
        }
    """)

    return Div(
        # Background Glow
        Div(cls="hero-glow"),
        # Content
        vstack(
            H1(headline, cls="hero-headline"),
            P(subheadline, cls="hero-subheadline"),
            button_link(
                cta_text,
                href=cta_link,
                variant="solid",
                color_palette="brand",  # We might need a custom space palette, but brand is safe fallback
                size="lg",
                style="font-size: 1.25rem; padding: 1rem 2.5rem; box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);",
            ),
            align="center",
            cls="hero-content",
            gap=spacing._8,
        ),
        hero_styles,
        cls="hero-container",
        **kwargs,
    )
