"""Minimal structured logging setup for the package."""

from __future__ import annotations

import logging
import sys
from typing import Any

import structlog


def configure_logging(level: int | str = logging.INFO) -> None:
    """Configure structlog with sane defaults for JSON output."""
    numeric_level = logging.getLevelName(level) if isinstance(level, str) else level

    logging.basicConfig(
        level=numeric_level,
        format="%(message)s",
        stream=sys.stdout,
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(numeric_level),
        cache_logger_on_first_use=True,
    )


def get_logger(*args: Any, **kwargs: Any) -> structlog.stdlib.BoundLogger:
    """Return a configured structlog logger."""
    return structlog.get_logger(*args, **kwargs)
