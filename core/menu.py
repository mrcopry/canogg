"""Menú principal del programa."""

from core.juego_base import JuegoBase
from juegos import GuerraDados, PiedraPapelTijera, TresEnRaya
from utils.consola import limpiar_pantalla, pausar_pantalla
from utils.entradas import solicitar_entero_validado

JUEGOS_DISPONIBLES: dict[int, type[JuegoBase]] = {
    1: PiedraPapelTijera,
    2: GuerraDados,
    3: TresEnRaya,
}
OPCION_SALIR = 4


def mostrar_menu_principal() -> None:
    """Muestra en pantalla las opciones del menú de juegos disponibles."""
    limpiar_pantalla()
    print("==========================================")
    print("    MENÚ DE JUEGOS - EVALUACIÓN EQUIPO   ")
    print("==========================================")
    print("1. Piedra, Papel o Tijera (Integrante 1)")
    print("2. Guerra de Dados        (Integrante 2)")
    print("3. Tres en Raya / Gato    (Integrante 3)")
    print("4. Salir del programa")
    print("==========================================")


def ejecutar_menu_principal() -> None:
    """Controla la ejecución iterativa del programa principal."""
    programa_activo = True

    while programa_activo:
        mostrar_menu_principal()
        opcion_seleccionada = solicitar_entero_validado(
            "Seleccione una opción (1-4): ", 1, OPCION_SALIR
        )

        if opcion_seleccionada == OPCION_SALIR:
            limpiar_pantalla()
            print("Gracias por jugar. Saliendo del programa...")
            programa_activo = False
        else:
            JUEGOS_DISPONIBLES[opcion_seleccionada]().ejecutar()

    pausar_pantalla()
