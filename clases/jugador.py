"""Modelo de un participante de la partida."""

from dataclasses import dataclass


@dataclass
class Jugador:
    """Representa a un jugador (humano o computadora) y su puntuación."""

    nombre: str
    es_bot: bool = False
    puntuacion: int = 0

    def sumar_punto(self) -> None:
        """Incrementa en uno la puntuación del jugador."""
        self.puntuacion += 1
