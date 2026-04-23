"""Cliente Gemini (IA para preguntas abiertas)."""
from __future__ import annotations

from config import GeminiConfig


class GeminiCliente:
    def __init__(self, cfg: GeminiConfig) -> None:
        self._cfg = cfg

    def consultar(self, pregunta: str) -> str:
        """Envía `pregunta` a Gemini con búsqueda activada y devuelve la respuesta."""
        raise NotImplementedError("GeminiCliente.consultar() — integrar google-generativeai")
