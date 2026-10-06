"""Clase base con el flujo común de todos los juegos."""

from abc import ABC, abstractmethod

from clases.jugador import Jugador
from utils.consola import limpiar_pantalla, pausar_pantalla
from utils.entradas import (
    MODO_PVE,
    seleccionar_modo_juego,
    solicitar_entero_validado,
    solicitar_nombre,
)


class JuegoBase(ABC):
    """Plantilla de una partida por rondas entre dos jugadores.

    Las subclases definen los atributos de configuración e implementan
    ``jugar_ronda`` y ``mostrar_resultado_final``.
    """

    titulo: str = ""
    mensaje_nombre_jugador_uno: str = "\nNombre del Jugador 1: "
    mensaje_nombre_jugador_dos: str = "Nombre del Jugador 2: "
    nombre_computadora: str = "Computadora"
    mensaje_total_rondas: str = ""
    max_rondas: int = 10

    def __init__(self) -> None:
        self.modo_juego: int = MODO_PVE
        self.jugador_uno: Jugador = Jugador("Jugador 1")
        self.jugador_dos: Jugador = Jugador("Jugador 2")
        self.total_rondas: int = 0
        self.numero_ronda: int = 1

    # ----- Flujo principal -------------------------------------------------

    def ejecutar(self) -> None:
        """Ejecuta una partida completa."""
        limpiar_pantalla()
        print(self.titulo)

        self.modo_juego = seleccionar_modo_juego()
        self.configurar_jugadores()
        self.total_rondas = solicitar_entero_validado(
            self.mensaje_total_rondas, 1, self.max_rondas
        )
        self.numero_ronda = 1

        while not self.partida_terminada():
            self.jugar_ronda()
            self.numero_ronda += 1
            pausar_pantalla()

        limpiar_pantalla()
        print("=== FIN DE LA PARTIDA ===")
        self.mostrar_resultado_final()
        pausar_pantalla()

    # ----- Pasos reutilizables ---------------------------------------------

    def configurar_jugadores(self) -> None:
        """Solicita los nombres; en PvE el segundo jugador es la computadora."""
        self.jugador_uno = Jugador(
            solicitar_nombre(self.mensaje_nombre_jugador_uno, "Jugador 1")
        )
        if self.modo_juego == MODO_PVE:
            self.jugador_dos = Jugador(self.nombre_computadora, es_bot=True)
        else:
            self.jugador_dos = Jugador(
                solicitar_nombre(self.mensaje_nombre_jugador_dos, "Jugador 2")
            )

    def partida_terminada(self) -> bool:
        """Por defecto gana quien llegue primero a ``total_rondas`` victorias."""
        return (
            self.jugador_uno.puntuacion >= self.total_rondas
            or self.jugador_dos.puntuacion >= self.total_rondas
        )

    def ganador(self) -> Jugador:
        """Devuelve al jugador con más puntos (el 2 en caso de igualdad)."""
        if self.jugador_uno.puntuacion > self.jugador_dos.puntuacion:
            return self.jugador_uno
        return self.jugador_dos

    def texto_marcador(self) -> str:
        """Texto con la puntuación actual de ambos jugadores."""
        return (
            f"{self.jugador_uno.nombre}: {self.jugador_uno.puntuacion} | "
            f"{self.jugador_dos.nombre}: {self.jugador_dos.puntuacion}"
        )

    # ----- A implementar por cada juego ------------------------------------

    @abstractmethod
    def jugar_ronda(self) -> None:
        """Juega una ronda completa (repitiéndola si hay empate)."""

    @abstractmethod
    def mostrar_resultado_final(self) -> None:
        """Muestra el mensaje del ganador de la partida."""
