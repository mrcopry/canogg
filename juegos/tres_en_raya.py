"""Juego 3: Tres en Raya (Gato)."""

from bot.computadora import elegir_casilla_gato
from clases.jugador import Jugador
from clases.tablero_gato import TableroGato
from core.juego_base import JuegoBase
from utils.consola import limpiar_pantalla, pausar_pantalla
from utils.entradas import solicitar_entero_validado


class TresEnRaya(JuegoBase):
    titulo = "=== JUEGO 3: TRES EN RAYA (GATO) ==="
    mensaje_nombre_jugador_uno = "\nNombre del Jugador 1 (✅): "
    mensaje_nombre_jugador_dos = "Nombre del Jugador 2 (❌): "
    nombre_computadora = "Computadora (⭕)"
    mensaje_total_rondas = (
        "\n¿Cuántas rondas ganadas se requieren para ser el campeon?: "
    )
    max_rondas = 5

    def jugar_ronda(self) -> None:
        ronda_concluida = False

        # Si el tablero se llena sin ganador, la ronda se reinicia por completo.
        while not ronda_concluida:
            tablero = TableroGato()
            turno_jugador_uno = True

            while not tablero.esta_lleno():
                limpiar_pantalla()
                print(f"--- RONDA {self.numero_ronda} ---")
                print(f"Marcador: {self.texto_marcador()}")
                tablero.mostrar()

                jugador = self.jugador_uno if turno_jugador_uno else self.jugador_dos
                simbolo = "✅" if turno_jugador_uno else "❌"

                posicion = self._elegir_casilla(jugador, simbolo, tablero)
                tablero.marcar(posicion, simbolo)

                if tablero.hay_ganador(simbolo):
                    limpiar_pantalla()
                    tablero.mostrar()
                    print(f"¡{jugador.nombre} ha ganado la ronda {self.numero_ronda}!")
                    jugador.sumar_punto()
                    ronda_concluida = True
                    break

                turno_jugador_uno = not turno_jugador_uno

            if not ronda_concluida:
                limpiar_pantalla()
                tablero.mostrar()
                print("¡Tablero lleno! La ronda terminó en empate.")
                print("REGLA: En caso de empate la ronda se reinicia por completo.\n")
                pausar_pantalla()

    def _elegir_casilla(
        self, jugador: Jugador, simbolo: str, tablero: TableroGato
    ) -> int:
        """Devuelve el índice (0-8) de la casilla elegida por el jugador en turno."""
        if jugador.es_bot:
            return elegir_casilla_gato(tablero)

        mensaje = f"{jugador.nombre} ({simbolo}), seleccione una casilla (1-9): "
        posicion = solicitar_entero_validado(mensaje, 1, 9) - 1
        while tablero.esta_ocupada(posicion):
            print("Casilla ocupada. Elija otra.")
            posicion = solicitar_entero_validado(mensaje, 1, 9) - 1
        return posicion

    def mostrar_resultado_final(self) -> None:
        print(f" ¡FELICIDADES {self.ganador().nombre.upper()}, CAMPEÓN DEL JUEGO!")
