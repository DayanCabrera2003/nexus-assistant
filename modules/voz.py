"""Síntesis de voz (pyttsx3 + espeak)."""
from __future__ import annotations

from config import VozConfig


class VozTTS:
    def __init__(self, cfg: VozConfig) -> None:
        self._cfg = cfg

    def hablar(self, texto: str) -> None:
        """Sintetiza `texto` y lo reproduce por los altavoces."""
        raise NotImplementedError("VozTTS.hablar() — integrar pyttsx3")
