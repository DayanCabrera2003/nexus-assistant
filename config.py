"""Carga y tipado de config.yaml."""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv


@dataclass(frozen=True)
class WakeWordConfig:
    modelo: str
    sensibilidad: float


@dataclass(frozen=True)
class VerificacionConfig:
    huella_vocal: str
    umbral: float
    duracion_muestra: int


@dataclass(frozen=True)
class ReconocimientoConfig:
    modelo: str
    timeout: int


@dataclass(frozen=True)
class GeminiConfig:
    api_key: str
    modelo: str
    busqueda_tiempo_real: bool
    prompt_sistema: str


@dataclass(frozen=True)
class VozConfig:
    velocidad: int
    volumen: float
    idioma: str


@dataclass(frozen=True)
class Config:
    wake_word: WakeWordConfig
    verificacion: VerificacionConfig
    reconocimiento: ReconocimientoConfig
    gemini: GeminiConfig
    voz: VozConfig


_ENV_PATTERN = re.compile(r"\$\{([A-Z_][A-Z0-9_]*)\}")


def _expand_env(value: str) -> str:
    return _ENV_PATTERN.sub(lambda m: os.environ.get(m.group(1), ""), value)


def cargar_config(path: str | Path) -> Config:
    load_dotenv()
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    gemini_raw = raw["gemini"]
    return Config(
        wake_word=WakeWordConfig(**raw["wake_word"]),
        verificacion=VerificacionConfig(**raw["verificacion"]),
        reconocimiento=ReconocimientoConfig(**raw["reconocimiento"]),
        gemini=GeminiConfig(
            api_key=_expand_env(gemini_raw["api_key"]),
            modelo=gemini_raw["modelo"],
            busqueda_tiempo_real=gemini_raw["busqueda_tiempo_real"],
            prompt_sistema=gemini_raw["prompt_sistema"],
        ),
        voz=VozConfig(**raw["voz"]),
    )
