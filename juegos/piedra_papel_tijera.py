"""Juego 1: Piedra, Papel o Tijera."""

from bot.computadora import elegir_movimiento_ppt
from clases.jugador import Jugador
from core.juego_base import JuegoBase
from utils.consola import limpiar_pantalla
from utils.entradas import solicitar_opcion_oculta, solicitar_opcion_texto_validada

OPCIONES_VALIDAS = ["piedra", "papel", "tijera"]

# Cada opción vence a la opción indicada como valor.
VENCE_A = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel",
}


def gana_primer_movimiento(movimiento_uno: str, movimiento_dos: str) -> bool:
    """Indica si ``movimiento_uno`` vence a ``movimiento_dos``."""
    return VENCE_A[movimiento_uno] == movimiento_dos


class PiedraPapelTijera(JuegoBase):
    titulo = "=== JUEGO 1: PIEDRA, PAPEL O TIJERA ==="
    mensaje_total_rondas = "\n¿Cuántas rondas ganadas se requieren para ganar la partida?: "
    max_rondas = 10

    def jugar_ronda(self) -> None:
        limpiar_pantalla()
        print(f"--- RONDA {self.numero_ronda} ---")
        print(f"Marcador: {self.texto_marcador()}\n")

        ronda_empatada = True
        while ronda_empatada:
            movimiento_uno = solicitar_opcion_texto_validada(
                f"{self.jugador_uno.nombre}, elija (Piedra, Papel, Tijera): ",
                OPCIONES_VALIDAS,
            )
            movimiento_dos = self._obtener_movimiento_jugador_dos()

            if movimiento_uno == movimiento_dos:
                print("\n¡EMPATE EN LA RONDA! Según las reglas, se repite la ronda actual.\n")
                continue

            ronda_empatada = False
            ganador_ronda: Jugador = (
                self.jugador_uno
                if gana_primer_movimiento(movimiento_uno, movimiento_dos)
                else self.jugador_dos
            )
            print(f"\n¡{ganador_ronda.nombre} gana la ronda {self.numero_ronda}!")
            ganador_ronda.sumar_punto()

    def _obtener_movimiento_jugador_dos(self) -> str:
        if self.jugador_dos.es_bot:
            movimiento = elegir_movimiento_ppt(OPCIONES_VALIDAS)
            print(f"{self.jugador_dos.nombre} eligió: {movimiento.capitalize()}")
            return movimiento
        # Ocultar la entrada del jugador 2 en PvP local
        return solicitar_opcion_oculta(
            f"{self.jugador_dos.nombre}, elija (Piedra, Papel, Tijera) [Oculto]: ",
            OPCIONES_VALIDAS,
        )

    def mostrar_resultado_final(self) -> None:
        print(f" ¡FELICIDADES {self.ganador().nombre.upper()}, HAS GANADO EL JUEGO!")
