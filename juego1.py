import random
import getpass
from utilerias import (
    limpiar_pantalla,
    pausar_pantalla,
    solicitar_entero_validado,
    solicitar_opcion_texto_validada,
    seleccionar_modo_juego,
)


def ejecutar_juego_piedra_papel_tijera() -> None:
    limpiar_pantalla()
    print("=== JUEGO 1: PIEDRA, PAPEL O TIJERA ===")

    modo_juego = seleccionar_modo_juego()
    nombre_jugador_uno = input("\nNombre del Jugador 1: ").strip() or "Jugador 1"
    nombre_jugador_dos = (
        "Computadora"
        if modo_juego == 1
        else (input("Nombre del Jugador 2: ").strip() or "Jugador 2")
    )

    total_rondas = solicitar_entero_validado(
        "\n¿Cuántas rondas ganadas se requieren para ganar la partida?: ", 1, 10
    )

    puntuacion_jugador_uno = 0
    puntuacion_jugador_dos = 0
    numero_ronda_actual = 1

    opciones_validas = ["piedra", "papel", "tijera"]

    while (
        puntuacion_jugador_uno < total_rondas
        and puntuacion_jugador_dos < total_rondas
    ):
        limpiar_pantalla()
        print(f"--- RONDA {numero_ronda_actual} ---")
        print(
            f"Marcador: {nombre_jugador_uno}: {puntuacion_jugador_uno} | {nombre_jugador_dos}: {puntuacion_jugador_dos}\n"
        )

        ronda_empatada = True
        while ronda_empatada:
            movimiento_jugador_uno = solicitar_opcion_texto_validada(
                f"{nombre_jugador_uno}, elija (Piedra, Papel, Tijera): ",
                opciones_validas,
            )

            if modo_juego == 1:
                movimiento_jugador_dos = random.choice(opciones_validas)
                print(f"{nombre_jugador_dos} eligió: {movimiento_jugador_dos.capitalize()}")
            else:
                # Ocultar la entrada del jugador 2 en PvP local
                movimiento_jugador_dos = getpass.getpass(
                    f"{nombre_jugador_dos}, elija (Piedra, Papel, Tijera) [Oculto]: "
                ).strip().lower()
                while movimiento_jugador_dos not in opciones_validas:
                    print("Opción inválida.")
                    movimiento_jugador_dos = getpass.getpass(
                        f"{nombre_jugador_dos}, elija (Piedra, Papel, Tijera) [Oculto]: "
                    ).strip().lower()

            # Evaluación de la ronda
            if movimiento_jugador_uno == movimiento_jugador_dos:
                print("\n¡EMPATE EN LA RONDA! Según las reglas, se repite la ronda actual.\n")
            else:
                ronda_empatada = False
                gana_jugador_uno = (
                    (movimiento_jugador_uno == "piedra" and movimiento_jugador_dos == "tijera")
                    or (movimiento_jugador_uno == "papel" and movimiento_jugador_dos == "piedra")
                    or (movimiento_jugador_uno == "tijera" and movimiento_jugador_dos == "papel")
                )

                if gana_jugador_uno:
                    print(f"\n¡{nombre_jugador_uno} gana la ronda {numero_ronda_actual}!")
                    puntuacion_jugador_uno += 1
                else:
                    print(f"\n¡{nombre_jugador_dos} gana la ronda {numero_ronda_actual}!")
                    puntuacion_jugador_dos += 1

        numero_ronda_actual += 1
        pausar_pantalla()

    # Ganador Final
    limpiar_pantalla()
    print("=== FIN DE LA PARTIDA ===")
    if puntuacion_jugador_uno > puntuacion_jugador_dos:
        print(f" ¡FELICIDADES {nombre_jugador_uno.upper()}, HAS GANADO EL JUEGO!")
    else:
        print(f" ¡FELICIDADES {nombre_jugador_dos.upper()}, HAS GANADO EL JUEGO!")
    pausar_pantalla()

