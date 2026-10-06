"""Utilidades generales de consola y entrada de datos."""

from utils.consola import limpiar_pantalla, pausar_pantalla
from utils.entradas import (
    MODO_PVE,
    MODO_PVP,
    seleccionar_modo_juego,
    solicitar_entero_validado,
    solicitar_nombre,
    solicitar_opcion_oculta,
    solicitar_opcion_texto_validada,
)

__all__ = [
    "MODO_PVE",
    "MODO_PVP",
    "limpiar_pantalla",
    "pausar_pantalla",
    "seleccionar_modo_juego",
    "solicitar_entero_validado",
    "solicitar_nombre",
    "solicitar_opcion_oculta",
    "solicitar_opcion_texto_validada",
]
