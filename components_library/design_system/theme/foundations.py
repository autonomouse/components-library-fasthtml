"""Foundation styles - base CSS for the application."""

from __future__ import annotations

from ..tokens import Breakpoints, Colors, Spacing, Typography

colors = Colors()
spacing = Spacing()
typography = Typography()
breakpoints = Breakpoints()


def base_styles() -> str:
    """
    Generate base CSS styles for the application.

    Returns:
        CSS string with base styles
    """
    return f"""
        /* CSS Reset and Base Styles */
        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        :root {{
            /* Marketing / Space Theme Variables */
            --marketing-bg-start: #0a0a1f;
            --marketing-bg-end: #1a1a3a;
            --marketing-accent-primary: #00f0ff;
            --marketing-accent-secondary: #7928ca;
            --marketing-text-primary: #ffffff;
            --marketing-text-secondary: #e0e0e0;
            --marketing-card-bg: rgba(255, 255, 255, 0.03);
            --marketing-card-border: rgba(255, 255, 255, 0.1);
        }}

        html {{
            font-size: 16px;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}

        body {{
            font-family: {typography.font_sans};
            font-size: {typography.base.size};
            line-height: {typography.base.line_height};
            color: {colors.text_primary};
            background-color: {colors.background};
            min-height: 100vh;
        }}

        /* Responsive touch targets for tablets */
        @media (min-width: {breakpoints.tablet}) {{
            button, a, input, select, textarea {{
                min-height: 44px;
            }}
        }}

        /* Focus styles for accessibility */
        *:focus {{
            outline: 2px solid {colors.border_focus};
            outline-offset: 2px;
        }}

        /* Remove focus outline for mouse users */
        *:focus:not(:focus-visible) {{
            outline: none;
        }}

        /* Utility classes */
        .container {{
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 {spacing._4};
        }}

        .sr-only {{
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border-width: 0;
        }}

        /* ===== COMMON LAYOUT STYLES ===== */

        /* Page content wrapper - consistent across all pages */
        .page-content-wrapper {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
        }}

        /* Mobile responsive page wrapper */
        @media (max-width: {breakpoints.tablet}) {{
            .page-content-wrapper {{
                padding: 0.75rem;
            }}
        }}

        @media (max-width: 480px) {{
            .page-content-wrapper {{
                padding: 0.5rem;
            }}
        }}

        /* ===== NAVIGATION RESPONSIVE STYLES ===== */

        /* Mobile navigation fixes */
        @media (max-width: {breakpoints.tablet}) {{
            .navigation {{
                padding: 0.75rem 1rem !important;
            }}

            /* Hide navigation links on mobile */
            .nav-links {{
                display: none !important;
            }}

            /* Hide user email on mobile to save space */
            .user-nav .user-email {{
                display: none !important;
            }}

            /* Make user nav more compact */
            .user-nav button {{
                font-size: 0.75rem !important;
                padding: 0.375rem 0.5rem !important;
                min-width: auto !important;
            }}

            /* Ensure navigation doesn't overflow */
            .navigation .hstack {{
                gap: 0.5rem !important;
            }}
        }}
    """
