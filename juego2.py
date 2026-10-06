import random
import getpass
from utilerias import (
    limpiar_pantalla,
    pausar_pantalla,
    solicitar_entero_validado,
    solicitar_opcion_texto_validada,
    seleccionar_modo_juego,
)


def ejecutar_juego_guerra_dados() -> None:
    limpiar_pantalla()
    print("=== JUEGO 2: GUERRA DE DADOS ===")

    modo_juego = seleccionar_modo_juego()
    nombre_jugador_uno = input("\nNombre del Jugador 1: ").strip() or "Jugador 1"
    nombre_jugador_dos = (
        "Computadora"
        if modo_juego == 1
        else (input("Nombre del Jugador 2: ").strip() or "Jugador 2")
    )

    total_rondas = solicitar_entero_validado(
        "\nIngrese la cantidad de rondas a jugar: ", 1, 10
    )

    puntuacion_jugador_uno = 0
    puntuacion_jugador_dos = 0
    ronda_actual = 1

    while ronda_actual <= total_rondas:
        limpiar_pantalla()
        print(f"--- RONDA {ronda_actual} DE {total_rondas} ---")
        print(
            f"Marcador: {nombre_jugador_uno}: {puntuacion_jugador_uno} | {nombre_jugador_dos}: {puntuacion_jugador_dos}\n"
        )

        ronda_empatada = True
        while ronda_empatada:
            input(f"{nombre_jugador_uno}, presione [ENTER] para lanzar su dado...")
            dado_jugador_uno = random.randint(1, 6)
            print(f"-> {nombre_jugador_uno} obtuvo un: {dado_jugador_uno}")

            if modo_juego == 1:
                print(f"\n{nombre_jugador_dos} está lanzando el dado...")
                dado_jugador_dos = random.randint(1, 6)
            else:
                input(f"{nombre_jugador_dos}, presione [ENTER] para lanzar su dado...")
                dado_jugador_dos = random.randint(1, 6)

            print(f"-> {nombre_jugador_dos} obtuvo un: {dado_jugador_dos}")

            if dado_jugador_uno == dado_jugador_dos:
                print("\n¡Empate de dados! Se debe repetir esta misma ronda.\n")
            elif dado_jugador_uno > dado_jugador_dos:
                print(f"\n¡{nombre_jugador_uno} gana la ronda {ronda_actual}!")
                puntuacion_jugador_uno += 1
                ronda_empatada = False
            else:
                print(f"\n¡{nombre_jugador_dos} gana la ronda {ronda_actual}!")
                puntuacion_jugador_dos += 1
                ronda_empatada = False

        ronda_actual += 1
        pausar_pantalla()

    limpiar_pantalla()
    print("=== FIN DE LA PARTIDA ===")
    print(
        f"Puntuación Final: {nombre_jugador_uno}: {puntuacion_jugador_uno} | {nombre_jugador_dos}: {puntuacion_jugador_dos}"
    )

    if puntuacion_jugador_uno > puntuacion_jugador_dos:
        print(f" ¡{nombre_jugador_uno} ES EL GANADOR!")
    else:
        print(f" ¡{nombre_jugador_dos} ES EL GANADOR!")
    pausar_pantalla()