"""Wake word detection (Porcupine)."""
from __future__ import annotations

from config import WakeWordConfig


class WakeWord:
    def __init__(self, cfg: WakeWordConfig) -> None:
        self._cfg = cfg

    def esperar(self) -> None:
        """Bloquea hasta detectar la palabra 'NEXUS'."""
        raise NotImplementedError("WakeWord.esperar() — integrar pvporcupine")
