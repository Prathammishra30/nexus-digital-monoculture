"""NEXUS Structured Logging Configuration.

Configures standard application logging with timestamp formatting,
log level controls, and sensitive token/credential redaction filters.
"""

import logging
import re
from typing import Any

# Redaction patterns for sensitive authorization tokens and keys
SENSITIVE_PATTERNS = [
    re.compile(r"(ghp_[A-Za-z0-9_]{36})"),
    re.compile(r"(sk-[A-Za-z0-9_]{20,})"),
    re.compile(r"(password=)([^\s&]+)", re.IGNORECASE),
    re.compile(r"(token=)([^\s&]+)", re.IGNORECASE),
]


class SensitiveDataFilter(logging.Filter):
    """Filter that masks API keys, passwords, and authorization tokens in log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            for pattern in SENSITIVE_PATTERNS:
                record.msg = pattern.sub(r"\1[REDACTED]", record.msg)
        return True


def setup_logging(log_level: str = "INFO", app_env: str = "development") -> None:
    """Initialize system-wide logging configuration."""
    level = getattr(logging, log_level.upper(), logging.INFO)

    log_format = (
        "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s"
        if app_env == "development"
        else '{"time": "%(asctime)s", "level": "%(levelname)s", "name": "%(name)s", "message": "%(message)s"}'
    )

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(log_format))
    handler.addFilter(SensitiveDataFilter())

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    # Avoid duplicate handlers if re-initialized
    if not root_logger.handlers:
        root_logger.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    """Return a named logger with sensitive data filtering enabled."""
    logger = logging.getLogger(name)
    logger.addFilter(SensitiveDataFilter())
    return logger
