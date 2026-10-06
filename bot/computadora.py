"""Lógica de decisión de la computadora (modo PvE).

Todo el comportamiento del bot vive aquí para poder mejorarlo
(por ejemplo, con estrategias más inteligentes) sin tocar los juegos.
"""

import random

from clases.dado import Dado
from clases.tablero_gato import TableroGato


def elegir_movimiento_ppt(opciones_validas: list[str]) -> str:
    """Elige al azar entre piedra, papel o tijera."""
    return random.choice(opciones_validas)


def lanzar_dado(dado: Dado) -> int:
    """Lanza el dado en nombre de la computadora."""
    return dado.lanzar()


def elegir_casilla_gato(tablero: TableroGato) -> int:
    """Elige al azar una casilla libre del tablero (índice 0-8)."""
    return random.choice(tablero.casillas_disponibles())
