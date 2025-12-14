"""Document intelligence package."""

from .exceptions import DocumentProcessingError
from .processors.pdfplumber_processor import PDFPlumberProcessor

__all__ = ["DocumentProcessingError", "PDFPlumberProcessor"]
