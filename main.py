"""NEXUS — punto de entrada. Orquesta el pipeline de voz."""
from __future__ import annotations

from comandos import COMANDOS, ejecutar
from config import cargar_config
from log import get_logger
from modules.gemini import GeminiCliente
from modules.reconocimiento import ReconocedorComandos
from modules.verificacion import VerificadorVoz
from modules.voz import VozTTS
from modules.wake_word import WakeWord

logger = get_logger(__name__)


def main() -> None:
    logger.info("NEXUS iniciando...")
    cfg = cargar_config("config.yaml")
    wake = WakeWord(cfg.wake_word)
    verificador = VerificadorVoz(cfg.verificacion)
    reconocedor = ReconocedorComandos(cfg.reconocimiento)
    gemini = GeminiCliente(cfg.gemini)
    voz = VozTTS(cfg.voz)
    logger.info("Módulos inicializados. Entrando al loop principal.")

    try:
        while True:
            wake.esperar()
            if not verificador.verificar(cfg.verificacion.duracion_muestra):
                continue
            texto = reconocedor.capturar(cfg.reconocimiento.timeout)
            if texto is None:
                continue
            if texto in COMANDOS:
                ejecutar(COMANDOS[texto])
                voz.hablar(f"Ejecutando {texto}")
            else:
                respuesta = gemini.consultar(texto)
                voz.hablar(respuesta)
    except KeyboardInterrupt:
        logger.info("NEXUS detenido por el usuario (Ctrl+C).")


if __name__ == "__main__":
    main()
