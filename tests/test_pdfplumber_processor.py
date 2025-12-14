import pytest

from document_intel.processors.pdfplumber_processor import PDFPlumberProcessor


def test_process_raises_not_implemented():
    processor = PDFPlumberProcessor("sample.pdf")

    with pytest.raises(NotImplementedError):
        processor.process()
