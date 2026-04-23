"""Configuración centralizada de logging para NEXUS.

Expone `get_logger(name)`. En la primera llamada configura dos handlers:
  - Consola (stderr) a nivel INFO.
  - Archivo rotativo `logs/nexus.log` a nivel DEBUG (5 MB × 3 backups).

Las llamadas subsecuentes reutilizan la configuración (idempotente).
"""
from __future__ import annotations

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

_LOG_DIR = Path("logs")
_LOG_FILE = _LOG_DIR / "nexus.log"
_FORMAT = "%(asctime)s %(levelname)-7s %(name)-20s %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
_MAX_BYTES = 5 * 1024 * 1024
_BACKUP_COUNT = 3

_configured = False


def _configure() -> None:
    global _configured
    if _configured:
        return
    _LOG_DIR.mkdir(exist_ok=True)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    formatter = logging.Formatter(_FORMAT, datefmt=_DATE_FORMAT)

    console = logging.StreamHandler(sys.stderr)
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    root.addHandler(console)

    file_handler = RotatingFileHandler(
        _LOG_FILE,
        maxBytes=_MAX_BYTES,
        backupCount=_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)

    _configured = True


def get_logger(name: str) -> logging.Logger:
    """Retorna un logger con la config de NEXUS aplicada."""
    _configure()
    return logging.getLogger(name)
