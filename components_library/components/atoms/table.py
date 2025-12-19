"""Table component - Data table."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Table as FtTable
from fasthtml.common import Tbody, Td, Th, Thead, Tr

from ...utils import merge_classes


def table(
    headers: list[str],
    rows: list[list[Any]],
    striped: bool = False,
    hoverable: bool = True,
    cls: str | None = None,
    **kwargs: Any,
) -> FtTable:
    """
    Data table component.

    Args:
        headers: List of column header texts
        rows: List of rows, each row is a list of cell values
        striped: Whether to stripe alternate rows
        hoverable: Whether rows highlight on hover
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Table element

    Example:
        >>> table(
        ...     headers=["Name", "Email", "Status"],
        ...     rows=[
        ...         ["John Doe", "john@example.com", badge("Active", variant="success")],
        ...         ["Jane Smith", "jane@example.com", badge("Pending", variant="gray")],
        ...     ]
        ... )
    """
    css_class = merge_classes(
        "table",
        "table-striped" if striped else None,
        "table-hover" if hoverable else None,
        cls,
    )

    # Header row
    header_cells = [Th(header) for header in headers]
    thead = Thead(Tr(*header_cells))

    # Body rows
    body_rows = []
    for row in rows:
        cells = [Td(cell) for cell in row]
        body_rows.append(Tr(*cells))

    tbody = Tbody(*body_rows)

    return FtTable(thead, tbody, cls=css_class, **kwargs)
