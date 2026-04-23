"""Reconocimiento de comandos (Vosk)."""
from __future__ import annotations

from config import ReconocimientoConfig


class ReconocedorComandos:
    def __init__(self, cfg: ReconocimientoConfig) -> None:
        self._cfg = cfg

    def capturar(self, timeout_s: int) -> str | None:
        """Captura audio por `timeout_s` segundos y retorna texto transcrito.

        Retorna None si no se detectó habla.
        """
        raise NotImplementedError("ReconocedorComandos.capturar() — integrar Vosk")
