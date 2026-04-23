"""Verificación de identidad vocal (Resemblyzer)."""
from __future__ import annotations

from config import VerificacionConfig


class VerificadorVoz:
    def __init__(self, cfg: VerificacionConfig) -> None:
        self._cfg = cfg

    def verificar(self, duracion_s: int) -> bool:
        """Graba audio por `duracion_s` segundos y compara con la huella del usuario.

        Retorna True si la similitud coseno es >= cfg.umbral.
        """
        raise NotImplementedError("VerificadorVoz.verificar() — integrar Resemblyzer")
