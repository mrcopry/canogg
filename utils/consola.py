"""Utilidades de presentación en la terminal."""

import os


def limpiar_pantalla() -> None:
    """Limpia la terminal según el sistema operativo utilizado."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar_pantalla() -> None:
    """Detiene la ejecución del programa hasta que el usuario presiona Enter."""
    input("\nPresione [ENTER] para continuar...")
