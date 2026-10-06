from utilerias import (
    limpiar_pantalla,
    pausar_pantalla,
    solicitar_entero_validado,
)
from juego1 import ejecutar_juego_piedra_papel_tijera
from juego2 import ejecutar_juego_guerra_dados
from juego3 import ejecutar_juego_tres_en_raya

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
            "Seleccione una opción (1-4): ", 1, 4
        )

        if opcion_seleccionada == 1:
            ejecutar_juego_piedra_papel_tijera()
        elif opcion_seleccionada == 2:
            ejecutar_juego_guerra_dados()
        elif opcion_seleccionada == 3:
            ejecutar_juego_tres_en_raya()
        elif opcion_seleccionada == 4:
            limpiar_pantalla()
            print("Gracias por jugar. Saliendo del programa...")
            programa_activo = False

    pausar_pantalla()


if __name__ == "__main__":
    ejecutar_menu_principal()