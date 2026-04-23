"""NEXUS — punto de entrada. Orquesta el pipeline de voz."""
from __future__ import annotations

from comandos import COMANDOS, ejecutar
from config import cargar_config
from modules.gemini import GeminiCliente
from modules.reconocimiento import ReconocedorComandos
from modules.verificacion import VerificadorVoz
from modules.voz import VozTTS
from modules.wake_word import WakeWord


def main() -> None:
    cfg = cargar_config("config.yaml")
    wake = WakeWord(cfg.wake_word)
    verificador = VerificadorVoz(cfg.verificacion)
    reconocedor = ReconocedorComandos(cfg.reconocimiento)
    gemini = GeminiCliente(cfg.gemini)
    voz = VozTTS(cfg.voz)

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


if __name__ == "__main__":
    main()
