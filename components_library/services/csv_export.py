"""CSV export utilities for FastHTML applications.

Provides helpers for generating CSV content and streaming responses
for file downloads.

Usage:
    from components_library.services import generate_csv, csv_response

    # Generate CSV content
    headers = ["Name", "Value", "Score"]
    rows = [
        ["Item 1", "A", "0.95"],
        ["Item 2", "B", "0.87"],
    ]
    content = generate_csv(headers, rows)

    # Create streaming response for download
    @rt("/export")
    def export_data():
        return csv_response(content, filename="export.csv")
"""

from __future__ import annotations

import csv
import io
from collections.abc import Iterable
from typing import Any

from starlette.responses import StreamingResponse


def generate_csv(
    headers: list[str],
    rows: Iterable[list[Any]],
) -> str:
    """Generate CSV content from headers and rows.

    Args:
        headers: List of column header strings
        rows: Iterable of row data (each row is a list of values)

    Returns:
        CSV content as a string
    """
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)

    output.seek(0)
    return output.getvalue()


def csv_response(
    content: str,
    filename: str = "export.csv",
) -> StreamingResponse:
    """Create a streaming response for CSV download.

    Args:
        content: CSV content string
        filename: Download filename (default: export.csv)

    Returns:
        StreamingResponse with appropriate headers for file download
    """
    return StreamingResponse(
        iter([content]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
