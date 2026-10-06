import random
import getpass
from utilerias import (
    limpiar_pantalla,
    pausar_pantalla,
    solicitar_entero_validado,
    solicitar_opcion_texto_validada,
    seleccionar_modo_juego,
)



def mostrar_tablero_gato(tablero: list[str]) -> None:
    print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} \n")


def verificar_ganador_gato(tablero: list[str], simbolo: str) -> bool:
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    return any(
        all(tablero[posicion] == simbolo for posicion in combo)
        for combo in combinaciones_ganadoras
    )


def ejecutar_juego_tres_en_raya() -> None:
    limpiar_pantalla()
    print("=== JUEGO 3: TRES EN RAYA (GATO) ===")

    modo_juego = seleccionar_modo_juego()
    nombre_jugador_uno = input("\nNombre del Jugador 1 (X): ").strip() or "Jugador 1"
    nombre_jugador_dos = (
        "Computadora (O)"
        if modo_juego == 1
        else (input("Nombre del Jugador 2 (O): ").strip() or "Jugador 2")
    )

    total_rondas = solicitar_entero_validado(
        "\n¿Cuántas rondas ganadas se requieren para ser el campeon?: ", 1, 5
    )

    puntuacion_jugador_uno = 0
    puntuacion_jugador_dos = 0
    numero_ronda = 1

    while (
        puntuacion_jugador_uno < total_rondas
        and puntuacion_jugador_dos < total_rondas
    ):
        ronda_concluida = False

        while not ronda_concluida:
            tablero = [str(i + 1) for i in range(9)]
            turnos_jugados = 0
            turno_actual_jugador_uno = True

            while turnos_jugados < 9:
                limpiar_pantalla()
                print(f"--- RONDA {numero_ronda} ---")
                print(
                    f"Marcador: {nombre_jugador_uno}: {puntuacion_jugador_uno} | {nombre_jugador_dos}: {puntuacion_jugador_dos}"
                )
                mostrar_tablero_gato(tablero)

                simbolo_actual = "X" if turno_actual_jugador_uno else "O"
                nombre_actual = (
                    nombre_jugador_uno
                    if turno_actual_jugador_uno
                    else nombre_jugador_dos
                )

                if not turno_actual_jugador_uno and modo_juego == 1:
                    casillas_disponibles = [
                        i for i in range(9) if tablero[i] not in ["X", "O"]
                    ]
                    posicion_elegida = random.choice(casillas_disponibles)
                else:
                    posicion = solicitar_entero_validado(
                        f"{nombre_actual} ({simbolo_actual}), seleccione una casilla (1-9): ",
                        1,
                        9,
                    )
                    posicion_elegida = posicion - 1

                    while tablero[posicion_elegida] in ["X", "O"]:
                        print("Casilla ocupada. Elija otra.")
                        posicion = solicitar_entero_validado(
                            f"{nombre_actual} ({simbolo_actual}), seleccione una casilla (1-9): ",
                            1,
                            9,
                        )
                        posicion_elegida = posicion - 1

                tablero[posicion_elegida] = simbolo_actual
                turnos_jugados += 1

                if verificar_ganador_gato(tablero, simbolo_actual):
                    limpiar_pantalla()
                    mostrar_tablero_gato(tablero)
                    print(f"¡{nombre_actual} ha ganado la ronda {numero_ronda}!")
                    if turno_actual_jugador_uno:
                        puntuacion_jugador_uno += 1
                    else:
                        puntuacion_jugador_dos += 1
                    ronda_concluida = True
                    break

                turno_actual_jugador_uno = not turno_actual_jugador_uno

            if not ronda_concluida and turnos_jugados == 9:
                limpiar_pantalla()
                mostrar_tablero_gato(tablero)
                print("¡Tablero lleno! La ronda terminó en empate.")
                print("REGLA: En caso de empate la ronda se reinicia por completo.\n")
                pausar_pantalla()

        numero_ronda += 1
        pausar_pantalla()

    limpiar_pantalla()
    print("=== FIN DE LA PARTIDA ===")
    if puntuacion_jugador_uno > puntuacion_jugador_dos:
        print(f" ¡FELICIDADES {nombre_jugador_uno.upper()}, CAMPEÓN DEL JUEGO!")
    else:
        print(f" ¡FELICIDADES {nombre_jugador_dos.upper()}, CAMPEÓN DEL JUEGO!")
    pausar_pantalla()