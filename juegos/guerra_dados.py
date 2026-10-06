"""Juego 2: Guerra de Dados."""

from bot.computadora import lanzar_dado
from clases.dado import Dado
from clases.jugador import Jugador
from core.juego_base import JuegoBase
from utils.consola import limpiar_pantalla


class GuerraDados(JuegoBase):
    titulo = "=== JUEGO 2: GUERRA DE DADOS ==="
    mensaje_total_rondas = "\nIngrese la cantidad de rondas a jugar: "
    max_rondas = 10

    def __init__(self) -> None:
        super().__init__()
        self.dado = Dado()

    def partida_terminada(self) -> bool:
        """En este juego se disputa un número fijo de rondas."""
        return self.numero_ronda > self.total_rondas

    def jugar_ronda(self) -> None:
        limpiar_pantalla()
        print(f"--- RONDA {self.numero_ronda} DE {self.total_rondas} ---")
        print(f"Marcador: {self.texto_marcador()}\n")

        ronda_empatada = True
        while ronda_empatada:
            dado_uno = self._lanzar(self.jugador_uno)
            dado_dos = self._lanzar(self.jugador_dos)

            if dado_uno == dado_dos:
                print("\n¡Empate de dados! Se debe repetir esta misma ronda.\n")
                continue

            ronda_empatada = False
            ganador_ronda = self.jugador_uno if dado_uno > dado_dos else self.jugador_dos
            print(f"\n¡{ganador_ronda.nombre} gana la ronda {self.numero_ronda}!")
            ganador_ronda.sumar_punto()

    def _lanzar(self, jugador: Jugador) -> int:
        if jugador.es_bot:
            print(f"\n{jugador.nombre} está lanzando el dado...")
            valor = lanzar_dado(self.dado)
        else:
            input(f"{jugador.nombre}, presione [ENTER] para lanzar su dado...")
            valor = self.dado.lanzar()
        print(f"-> {jugador.nombre} obtuvo un: {valor}")
        return valor

    def mostrar_resultado_final(self) -> None:
        print(f"Puntuación Final: {self.texto_marcador()}")
        print(f" ¡{self.ganador().nombre} ES EL GANADOR!")
