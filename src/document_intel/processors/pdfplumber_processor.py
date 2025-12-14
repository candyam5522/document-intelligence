from __future__ import annotations

from pathlib import Path
from typing import Any


class PDFPlumberProcessor:
    """Placeholder processor for PDF documents."""

    def __init__(self, source: str | Path) -> None:
        self.source = Path(source)

    def process(self) -> Any:
        """Process the PDF into structured data once implemented."""
        raise NotImplementedError("PDF processing not implemented yet.")
