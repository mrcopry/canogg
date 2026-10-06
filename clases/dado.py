"""Modelo de un dado."""

import random


class Dado:
    """Dado de N caras (6 por defecto)."""

    def __init__(self, caras: int = 6) -> None:
        self.caras = caras

    def lanzar(self) -> int:
        """Devuelve un valor aleatorio entre 1 y el número de caras."""
        return random.randint(1, self.caras)
