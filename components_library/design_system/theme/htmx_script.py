"""HTMX script inclusion for interactive components."""

from __future__ import annotations


def htmx_script() -> str:
    """
    Return the HTMX CDN script tag.

    Returns:
        HTML script tag for HTMX
    """
    return '<script src="https://unpkg.com/htmx.org@2.0.4" integrity="sha384-HGfztofotfshcF7+8n44JQL2oJmowVChPTg48S+jvZoztPfvwD79OC/LTtG6dMp+" crossorigin="anonymous"></script>'


def htmx_config() -> str:
    """
    Return HTMX configuration script.

    Returns:
        HTML script tag with HTMX config
    """
    return """
    <script>
        htmx.config.defaultSwapStyle = 'innerHTML';
        htmx.config.defaultSwapDelay = 0;
        htmx.config.defaultSettleDelay = 20;
        htmx.config.includeIndicatorStyles = true;
    </script>
    """


def menu_click_outside_script() -> str:
    """
    Return minimal script for closing dropdown menus on outside clicks.

    DEPRECATED: Replaced by CSS-only solution in base_styles.py
    """
    return ""
