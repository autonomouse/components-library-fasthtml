"""HTMX attribute helper functions."""

from __future__ import annotations

from typing import Any, Literal


def htmx_attrs(
    get: str | None = None,
    post: str | None = None,
    put: str | None = None,
    patch: str | None = None,
    delete: str | None = None,
    trigger: str | None = None,
    target: str | None = None,
    swap: Literal[
        "innerHTML",
        "outerHTML",
        "beforebegin",
        "afterbegin",
        "beforeend",
        "afterend",
        "delete",
        "none",
    ]
    | None = None,
    vals: str | None = None,
    confirm: str | None = None,
    indicator: str | None = None,
    push_url: str | bool | None = None,
    select: str | None = None,
    swap_oob: str | None = None,
    include: str | None = None,
    ext: str | None = None,
) -> dict[str, Any]:
    """
    Generate HTMX attributes dictionary.

    Args:
        get: URL for GET request
        post: URL for POST request
        put: URL for PUT request
        patch: URL for PATCH request
        delete: URL for DELETE request
        trigger: Event that triggers the request
        target: Target element for swap
        swap: How to swap the response
        vals: Additional values to include
        confirm: Confirmation message
        indicator: Loading indicator selector
        push_url: Push URL to browser history
        select: Select content from response
        swap_oob: Out of band swap
        include: Include additional elements
        ext: HTMX extensions to use

    Returns:
        Dictionary of HTMX attributes

    Example:
        >>> htmx_attrs(get="/api/search", trigger="keyup changed delay:300ms")
        {'hx_get': '/api/search', 'hx_trigger': 'keyup changed delay:300ms'}
    """
    attrs: dict[str, Any] = {}

    if get:
        attrs["hx_get"] = get
    if post:
        attrs["hx_post"] = post
    if put:
        attrs["hx_put"] = put
    if patch:
        attrs["hx_patch"] = patch
    if delete:
        attrs["hx_delete"] = delete
    if trigger:
        attrs["hx_trigger"] = trigger
    if target:
        attrs["hx_target"] = target
    if swap:
        attrs["hx_swap"] = swap
    if vals:
        attrs["hx_vals"] = vals
    if confirm:
        attrs["hx_confirm"] = confirm
    if indicator:
        attrs["hx_indicator"] = indicator
    if push_url is not None:
        attrs["hx_push_url"] = "true" if push_url is True else str(push_url)
    if select:
        attrs["hx_select"] = select
    if swap_oob:
        attrs["hx_swap_oob"] = swap_oob
    if include:
        attrs["hx_include"] = include
    if ext:
        attrs["hx_ext"] = ext

    return attrs


def debounced_search(url: str, target: str = "#results", delay: int = 300) -> dict[str, Any]:
    """
    Generate HTMX attributes for a debounced search input.

    Args:
        url: Search endpoint URL
        target: Target element for results
        delay: Debounce delay in milliseconds

    Returns:
        HTMX attributes dictionary

    Example:
        >>> debounced_search("/api/search", "#search-results")
        {'hx_get': '/api/search', 'hx_trigger': 'keyup changed delay:300ms', 'hx_target': '#search-results'}
    """
    return htmx_attrs(get=url, trigger=f"keyup changed delay:{delay}ms", target=target)


def modal_trigger(modal_url: str, modal_id: str = "modal") -> dict[str, Any]:
    """
    Generate HTMX attributes for modal trigger.

    Args:
        modal_url: URL to fetch modal content
        modal_id: ID of modal container

    Returns:
        HTMX attributes dictionary
    """
    return htmx_attrs(get=modal_url, target=f"#{modal_id}", swap="innerHTML")


def confirm_delete(url: str, message: str = "Are you sure?") -> dict[str, Any]:
    """
    Generate HTMX attributes for confirmed delete action.

    Args:
        url: Delete endpoint URL
        message: Confirmation message

    Returns:
        HTMX attributes dictionary
    """
    return htmx_attrs(delete=url, confirm=message, swap="outerHTML")
