"""Editable Header molecule - Heading with inline edit button."""

from __future__ import annotations

import uuid
from typing import Any

from fasthtml.common import Button, Div

from ...components.atoms.editable_heading import editable_heading
from ...components.atoms.icon import icon


def editable_header(
    value: str,
    name: str,
    post_url: str,
    edit_url: str | None = None,
    placeholder: str = "",
    level: int = 1,
    cls: str | None = None,
    icon_class: str = "text-blue-500 hover:text-blue-400 transition-colors cursor-pointer opacity-70 hover:opacity-100",
    multiline: bool = False,
    font_weight: str | int = "800",
    text_clickable: bool = True,
    is_editing: bool = False,
    max_lines: int | None = None,
    **kwargs: Any,
) -> Div:
    """
    A heading that relies on HTMX to toggle between a read-only text view and an editable input/textarea.
    The 'Click to Edit' interaction fetches this component in 'editing' mode from the server.

    Args:
        value: Current text value
        name: Form field name
        post_url: HTMX POST URL for updates (should return is_editing=False version)
        edit_url: HTMX GET URL to fetch the editor (should return is_editing=True version). Defaults to post_url + "?edit=true" if not provided.
        placeholder: Placeholder text
        level: Heading level (1-6) affecting font size
        cls: Additional CSS classes for the container
        icon_class: CSS classes for the edit icon
        multiline: Whether to use a textarea for editing
        font_weight: Font weight for text and input
        text_clickable: Whether clicking the text itself triggers edit mode (default True)
        is_editing: Whether to render the editing view instead of the read view
        max_lines: Max number of lines to show in read mode before truncating.
        **kwargs: Additional HTML attributes for the editable_heading

    Returns:
        Div containing either the read-only view OR the edit view (depending on is_editing).
    """
    # Prefer ID passed in kwargs, else generate one for the main container
    container_id = kwargs.pop("id", None)
    if container_id is None:
        container_id = f"editable-header-{uuid.uuid4()}"

    # If edit_url is not provided, default to the post_url with a query param
    # Note: caller must ensure the backend handles this!
    if edit_url is None:
        edit_url = f"{post_url}{'&' if '?' in post_url else '?'}edit=true"

    # Font sizes based on level (same as editable_heading for consistency)
    font_sizes = {
        1: "2.5rem",
        2: "2rem",
        3: "1.75rem",
        4: "1.5rem",
        5: "1.25rem",
        6: "1rem",
    }
    font_size = font_sizes.get(level, "2rem")

    # Extract style from kwargs if present
    user_style = kwargs.pop("style", "")

    # Common container style

    if is_editing:
        # --- RENDER EDIT VIEW ---
        # The edit view replaces the container content

        # Styles
        edit_view_style = f"""
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
            width: 100%;
            {user_style}
        """

        # If multiline, try to use field-sizing for auto-resize
        field_sizing_style = "field-sizing: content;" if multiline else ""

        edit_heading_comp = editable_heading(
            value=value,
            name=name,
            post_url=post_url,
            target=f"#{container_id}",  # Target the main container to replace everything on save
            hx_swap="outerHTML",
            placeholder=placeholder,
            level=level,
            multiline=multiline,
            font_weight=font_weight,
            # If multiline, provide reasonable starting rows, and use field-sizing
            rows=10 if multiline else 3,
            style=f"width: 100%; flex: 1; {field_sizing_style}",
            autofocus=True,  # Important: Focus when swapped in
            **kwargs,
        )

        # We can't use 'onclick document.getElementById.blur()' because that relies on JS.
        # But for 'save on click', a submit button is standard.
        # However, editable_heading already saves on 'blur'.
        # Click outside causes blur -> save.
        # Clicking the checkmark button should also cause a save.
        # A simple way without JS: Make it a submit button if wrapped in a form?
        # But editable_heading uses hx-post on the input itself.
        # So the 'check' button is purely visual/UX hint?
        # Actually, clicking it removes focus from input -> Blur -> Save.
        # Clicking *anything* else does that.
        # So a link or button that does nothing but take focus works?
        # Or make it a label for something?
        # Let's keep it as a button. Clicking it focuses the button, blurring the input.
        # This works perfectly without explicit JS!
        save_button = Button(
            icon("check", size="sm", cls="text-green-500"),
            type="button",
            cls="btn-ghost hover:bg-green-500/10 rounded-full p-2 transition-colors",
            style=f"margin-top: calc({font_size} * 0.1); cursor: pointer;",
            title="Save changes",
        )

        return Div(
            edit_heading_comp,
            save_button,
            id=container_id,  # MAINTAIN ID for smooth swapping
            cls=cls,
            style=edit_view_style,
        )

    else:
        # --- RENDER READ VIEW ---

        read_view_style = f"""
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            cursor: {"pointer" if text_clickable else "default"};
            padding: 2px 4px;
            margin: -2px -4px;
            border: 1px solid transparent;
            border-radius: 4px;
            transition: background-color 0.2s;
            {user_style}
        """

        text_style = f"""
            font-size: {font_size};
            font-weight: {font_weight};
            color: white;
            line-height: {user_style.split("line-height:")[-1].split(";")[0] if "line-height:" in user_style else "1.5"};
            flex: 1;
            overflow-wrap: break-word;
            min-width: 0;
        """

        # HTMX Attributes for fetching the editor
        # If the container is clicked (and text_clickable is true), fetch editor
        htmx_attrs = (
            {"hx_get": edit_url, "hx_target": f"#{container_id}", "hx_swap": "outerHTML"}
            if text_clickable
            else {}
        )

        text_container_id = f"{container_id}-text"

        # Line clamping styles if max_lines is set
        clamp_style = ""
        expansion_ui = ""

        if max_lines and value:
            # We only add clamp styles initially
            # We use a known ID to toggle it via inline script for simplicity
            clamp_style = f"overflow: hidden; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: {max_lines};"

            # JS Exception: Toggling -webkit-line-clamp requires JavaScript. CSS-only alternatives
            # (using :checked pseudo-class) would require restructuring the DOM significantly
            # and wouldn't integrate well with the existing HTMX-based edit functionality.
            # Note: We stop propagation to prevent triggering the edit mode if text_clickable is True
            toggle_script = f"""
                event.stopPropagation();
                var el = document.getElementById('{text_container_id}');
                if (el.style.webkitLineClamp && el.style.webkitLineClamp !== 'unset') {{
                    el.style.webkitLineClamp = 'unset';
                    this.textContent = 'Show less';
                }} else {{
                    el.style.webkitLineClamp = '{max_lines}';
                    this.textContent = 'Read more';
                }}
            """

            expansion_ui = kwargs.pop(
                "expansion_trigger",
                Div(
                    "Read more",
                    cls="text-xs cursor-pointer mt-2 font-bold uppercase tracking-wide hover:opacity-80 transition-opacity",
                    onclick=toggle_script,
                    style="display: inline-block; color: var(--theme-accent-primary);",
                ),
            )

        content = (
            [
                Div(
                    Div(
                        value or placeholder,
                        id=text_container_id,
                        style=f"{text_style} {clamp_style}",
                    ),
                    expansion_ui if expansion_ui else "",
                    style="flex: 1; min-width: 0;",  # Wrapper to hold text + expander
                )
            ]
            if value
            else [
                Div(
                    placeholder,
                    style=f"{text_style} color: rgba(255,255,255,0.5); font-style: italic;",
                )
            ]
        )

        # Edit Icon
        # If text is NOT clickable, the icon carries the HTMX trigger
        icon_htmx_attrs = (
            {}
            if text_clickable
            else {"hx_get": edit_url, "hx_target": f"#{container_id}", "hx_swap": "outerHTML"}
        )

        content.append(
            Div(
                icon(
                    "edit",
                    size="sm",
                    cls=f"{icon_class} edit-icon",
                    style="color: var(--theme-accent-primary);",
                ),
                style=f"""
                    margin-top: calc({font_size} * 0.1);
                    min-width: 32px;
                    height: 32px;
                    border-radius: 50%;
                    background: rgba(255, 255, 255, 0.05);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                """,
                cls="hover:bg-white/10 hover:border-white/20",
                **icon_htmx_attrs,
            )
        )

        return Div(
            *content,
            id=container_id,
            cls=f"group hover:bg-white/5 {cls or ''}" if text_clickable else f"group {cls or ''}",
            style=read_view_style,
            **htmx_attrs,
        )
