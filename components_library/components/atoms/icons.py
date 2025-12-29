"""SVG Icons module - Reusable SVG icon definitions.

This module provides SVG icon strings that can be used across Labs applications.
Icons are based on Lucide icons (https://lucide.dev/) for consistency.

Usage:
    from components_library import svg_icon, ICON_TARGET, ICON_INFO

    # Using the svg_icon helper function
    Div(NotStr(svg_icon("target", size=24)))

    # Or using raw SVG strings directly
    Div(NotStr(ICON_TARGET.format(size=24)))
"""

from __future__ import annotations

from typing import Literal

# =============================================================================
# Lucide-style Icons (stroke-based)
# All icons use viewBox="0 0 24 24" and support size formatting
# =============================================================================

# Target/crosshair icon - useful for indication expansion, targeting
ICON_TARGET = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="10"/>
<circle cx="12" cy="12" r="6"/>
<circle cx="12" cy="12" r="2"/>
<line x1="12" y1="2" x2="12" y2="6"/>
<line x1="12" y1="18" x2="12" y2="22"/>
<line x1="2" y1="12" x2="6" y2="12"/>
<line x1="18" y1="12" x2="22" y2="12"/>
</svg>"""

# Paperclip icon - useful for attachments, articles, documents
ICON_PAPERCLIP = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
</svg>"""

# Info icon (circle with i) - for information boxes
ICON_INFO = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="10"/>
<path d="M12 16v-4"/>
<path d="M12 8h.01"/>
</svg>"""

# Info icon (filled variant) - for info alerts with fill color
ICON_INFO_FILLED = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="none">
<circle cx="12" cy="12" r="10"/>
<path d="M12 16v-4M12 8h.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# Search/magnifying glass icon
ICON_SEARCH = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="11" cy="11" r="8"/>
<path d="m21 21-4.3-4.3"/>
</svg>"""

# File/document icon
ICON_FILE = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/>
<path d="M14 2v4a2 2 0 0 0 2 2h4"/>
</svg>"""

# Flask/beaker icon - for lab/science features
ICON_FLASK = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M9 3h6"/>
<path d="M10 9V3"/>
<path d="M14 9V3"/>
<path d="M9 9l-2 8a3 3 0 0 0 3 3h4a3 3 0 0 0 3-3l-2-8H9z"/>
</svg>"""

# DNA helix icon - for genetic/biological features
ICON_DNA = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M2 15c6.667-6 13.333 0 20-6"/>
<path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993"/>
<path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993"/>
<path d="m17 6-2.5-2.5"/>
<path d="m14 8-1-1"/>
<path d="m7 18 2.5 2.5"/>
<path d="m3.5 14.5.5.5"/>
<path d="m20 9 .5.5"/>
<path d="m6.5 12.5 1 1"/>
<path d="m16.5 10.5 1 1"/>
<path d="m10 16 1.5 1.5"/>
</svg>"""

# Activity/pulse icon - for health/medical data
ICON_ACTIVITY = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
</svg>"""

# Download icon
ICON_DOWNLOAD = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
<polyline points="7 10 12 15 17 10"/>
<line x1="12" y1="15" x2="12" y2="3"/>
</svg>"""

# External link icon
ICON_EXTERNAL_LINK = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M15 3h6v6"/>
<path d="M10 14 21 3"/>
<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
</svg>"""

# Check/checkmark icon
ICON_CHECK = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M20 6 9 17l-5-5"/>
</svg>"""

# X/close icon
ICON_X = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M18 6 6 18"/>
<path d="m6 6 12 12"/>
</svg>"""

# Alert triangle icon
ICON_ALERT_TRIANGLE = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
<path d="M12 9v4"/>
<path d="M12 17h.01"/>
</svg>"""

# Arrow left icon
ICON_ARROW_LEFT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m12 19-7-7 7-7"/>
<path d="M19 12H5"/>
</svg>"""

# Arrow right icon
ICON_ARROW_RIGHT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m12 5 7 7-7 7"/>
<path d="M5 12h14"/>
</svg>"""

# Chevron down icon
ICON_CHEVRON_DOWN = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m6 9 6 6 6-6"/>
</svg>"""

# Chevron up icon
ICON_CHEVRON_UP = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m18 15-6-6-6 6"/>
</svg>"""

# Plus icon
ICON_PLUS = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M5 12h14"/>
<path d="M12 5v14"/>
</svg>"""

# Minus icon
ICON_MINUS = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M5 12h14"/>
</svg>"""

# Settings/gear icon
ICON_SETTINGS = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
<circle cx="12" cy="12" r="3"/>
</svg>"""

# User icon
ICON_USER = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
<circle cx="12" cy="7" r="4"/>
</svg>"""

# Logout icon
ICON_LOGOUT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
<polyline points="16 17 21 12 16 7"/>
<line x1="21" y1="12" x2="9" y2="12"/>
</svg>"""

# Calendar icon
ICON_CALENDAR = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect width="18" height="18" x="3" y="4" rx="2" ry="2"/>
<line x1="16" y1="2" x2="16" y2="6"/>
<line x1="8" y1="2" x2="8" y2="6"/>
<line x1="3" y1="10" x2="21" y2="10"/>
</svg>"""

# Clock icon
ICON_CLOCK = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="10"/>
<polyline points="12 6 12 12 16 14"/>
</svg>"""

# Filter icon
ICON_FILTER = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>
</svg>"""

# Sort icon (bars descending)
ICON_SORT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<line x1="4" y1="6" x2="20" y2="6"/>
<line x1="4" y1="12" x2="16" y2="12"/>
<line x1="4" y1="18" x2="12" y2="18"/>
</svg>"""

# Refresh icon
ICON_REFRESH = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/>
<path d="M21 3v5h-5"/>
<path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/>
<path d="M3 21v-5h5"/>
</svg>"""

# Book icon
ICON_BOOK = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>
</svg>"""

# Script/Screenplay icon
ICON_SCRIPT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/>
<polyline points="14 2 14 8 20 8"/>
<path d="M12 13v6"/>
<path d="M12 18l3-3"/>
<path d="M9 15l3 3"/>
</svg>"""

# Audio/Headphones icon
ICON_AUDIO = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 18v-6a9 9 0 0 1 18 0v6"/>
<path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>
</svg>"""

# Edit/Pencil icon
ICON_EDIT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/>
<path d="m15 5 4 4"/>
</svg>"""

# File Text icon
ICON_FILE_TEXT = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/>
<path d="M14 2v4a2 2 0 0 0 2 2h4"/>
<path d="M10 9H8"/>
<path d="M16 13H8"/>
<path d="M16 17H8"/>
</svg>"""

# Map Pin icon
ICON_MAP_PIN = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
<circle cx="12" cy="10" r="3"/>
</svg>"""

# Book Open icon
ICON_BOOK_OPEN = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
</svg>"""

# Trash 2 icon
ICON_TRASH_2 = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 6h18"/>
<path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/>
<path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>
<line x1="10" x2="10" y1="11" y2="17"/>
<line x1="14" x2="14" y1="11" y2="17"/>
</svg>"""

# Eye icon
ICON_EYE = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
<circle cx="12" cy="12" r="3"/>
</svg>"""

# Eye Off icon
ICON_EYE_OFF = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/>
<path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/>
<path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7c.44 0 .87-.03 1.28-.09"/>
<path d="M2 2l20 20"/>
</svg>"""

# More Vertical icon
ICON_MORE_VERTICAL = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="1"/>
<circle cx="12" cy="5" r="1"/>
<circle cx="12" cy="19" r="1"/>
</svg>"""

# Check Square icon
ICON_CHECK_SQUARE = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="m9 11 3 3L22 4"/>
<path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
</svg>"""

# Square icon
ICON_SQUARE = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect width="18" height="18" x="3" y="3" rx="2"/>
</svg>"""

# Layout Dashboard icon
ICON_LAYOUT_DASHBOARD = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect width="7" height="9" x="3" y="3" rx="1"/>
<rect width="7" height="5" x="14" y="3" rx="1"/>
<rect width="7" height="9" x="14" y="12" rx="1"/>
<rect width="7" height="5" x="3" y="16" rx="1"/>
</svg>"""

# Image icon
ICON_IMAGE = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/>
<circle cx="9" cy="9" r="2"/>
<path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>
</svg>"""

# Clapperboard icon
ICON_CLAPPERBOARD = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M20.2 6 3 11l-.9-2.4c-.5-1.1.2-2.3 1.3-2.8l3.2-1.2c1.1-.5 2.3.2 2.8 1.3l.9 2.4"/>
<path d="m13.7 4.5 2 5"/>
<path d="m10 6 2 5"/>
<path d="m6.3 7.5 2 5"/>
</svg>"""

# Star icon
ICON_STAR = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
</svg>"""

# =============================================================================
# Icon Name Registry - maps friendly names to icon constants
# =============================================================================

ICON_REGISTRY: dict[str, str] = {
    "target": ICON_TARGET,
    "paperclip": ICON_PAPERCLIP,
    "info": ICON_INFO,
    "info-filled": ICON_INFO_FILLED,
    "search": ICON_SEARCH,
    "file": ICON_FILE,
    "flask": ICON_FLASK,
    "dna": ICON_DNA,
    "activity": ICON_ACTIVITY,
    "download": ICON_DOWNLOAD,
    "external-link": ICON_EXTERNAL_LINK,
    "check": ICON_CHECK,
    "x": ICON_X,
    "alert-triangle": ICON_ALERT_TRIANGLE,
    "arrow-left": ICON_ARROW_LEFT,
    "arrow-right": ICON_ARROW_RIGHT,
    "chevron-down": ICON_CHEVRON_DOWN,
    "chevron-up": ICON_CHEVRON_UP,
    "plus": ICON_PLUS,
    "minus": ICON_MINUS,
    "settings": ICON_SETTINGS,
    "user": ICON_USER,
    "logout": ICON_LOGOUT,
    "calendar": ICON_CALENDAR,
    "clock": ICON_CLOCK,
    "filter": ICON_FILTER,
    "sort": ICON_SORT,
    "refresh": ICON_REFRESH,
    "book": ICON_BOOK,
    "script": ICON_SCRIPT,
    "audio": ICON_AUDIO,
    "edit": ICON_EDIT,
    "file-text": ICON_FILE_TEXT,
    "map-pin": ICON_MAP_PIN,
    "book-open": ICON_BOOK_OPEN,
    "trash-2": ICON_TRASH_2,
    "trash": ICON_TRASH_2,  # Alias
    "eye": ICON_EYE,
    "eye-off": ICON_EYE_OFF,
    "more-vertical": ICON_MORE_VERTICAL,
    "check-square": ICON_CHECK_SQUARE,
    "square": ICON_SQUARE,
    "layout-dashboard": ICON_LAYOUT_DASHBOARD,
    "image": ICON_IMAGE,
    "clapperboard": ICON_CLAPPERBOARD,
    "star": ICON_STAR,
}


# =============================================================================
# Helper Functions
# =============================================================================


def svg_icon(
    name: str,
    size: int = 24,
    fill: str = "#2563EB",
    color: str | None = None,
) -> str:
    """
    Get a formatted SVG icon string by name.

    Args:
        name: Icon name (e.g., "target", "info", "search")
        size: Icon size in pixels (default 24)
        fill: Fill color for filled icons (default brand blue)
        color: Stroke color override (applies via style attribute)

    Returns:
        Formatted SVG string ready to use with NotStr()

    Example:
        from fasthtml.common import Div, NotStr
        from components_library import svg_icon

        Div(NotStr(svg_icon("target", size=32)))
        Div(NotStr(svg_icon("info-filled", size=20, fill="#22C55E")))
    """
    icon_template = ICON_REGISTRY.get(name)
    if icon_template is None:
        msg = f"Unknown icon: {name}. Available icons: {list(ICON_REGISTRY.keys())}"
        raise ValueError(msg)

    # Format with size and fill
    svg = icon_template.format(size=size, fill=fill)

    # Apply color override if specified
    if color:
        # Add style attribute for stroke color
        svg = svg.replace("<svg ", f'<svg style="color: {color};" ')

    return svg


IconName = Literal[
    "target",
    "paperclip",
    "info",
    "info-filled",
    "search",
    "file",
    "flask",
    "dna",
    "activity",
    "download",
    "external-link",
    "check",
    "x",
    "alert-triangle",
    "arrow-left",
    "arrow-right",
    "chevron-down",
    "chevron-up",
    "plus",
    "minus",
    "settings",
    "user",
    "logout",
    "calendar",
    "clock",
    "filter",
    "sort",
    "refresh",
    "book",
    "script",
    "audio",
    "edit",
    "file-text",
    "map-pin",
    "book-open",
    "trash-2",
    "trash",
    "eye",
    "eye-off",
    "more-vertical",
    "check-square",
    "square",
    "layout-dashboard",
    "image",
    "clapperboard",
    "star",
]
"""Type alias for valid icon names."""
