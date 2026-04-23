"""Comandos predefinidos y ejecución."""
from __future__ import annotations

import subprocess

from log import get_logger

logger = get_logger(__name__)

COMANDOS: dict[str, str] = {
    # Sistema
    "apaga la pantalla": "xset dpms force off",
    "bloquea la pantalla": "loginctl lock-session",
    "captura de pantalla": "gnome-screenshot",
    # Audio
    "sube el volumen": "pactl set-sink-volume @DEFAULT_SINK@ +10%",
    "baja el volumen": "pactl set-sink-volume @DEFAULT_SINK@ -10%",
    "silencia": "pactl set-sink-mute @DEFAULT_SINK@ toggle",
    # Aplicaciones
    "abre el navegador": "firefox &",
    "abre la terminal": "gnome-terminal &",
    "abre el editor": "code &",
    # Música
    "pausa la música": "playerctl pause",
    "siguiente canción": "playerctl next",
    "canción anterior": "playerctl previous",
}


def ejecutar(comando: str) -> None:
    logger.info("Ejecutando: %s", comando)
    result = subprocess.run(comando, shell=True, check=False)
    if result.returncode != 0:
        logger.warning(
            "Comando terminó con código %d: %s", result.returncode, comando
        )
