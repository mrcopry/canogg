import os


def limpiar_pantalla() -> None:
    """Limpia la terminal según el sistema operativo utilizado."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar_pantalla() -> None:
    """Detiene la ejecución del programa hasta que el usuario presiona Enter."""
    input("\nPresione [ENTER] para continuar...")


def solicitar_entero_validado(
    mensaje_solicitud: str, limite_inferior: int, limite_superior: int
) -> int:
    """Solicita un número entero y valida que se encuentre dentro del rango especificado."""
    while True:
        try:
            numero_ingresado = int(input(mensaje_solicitud))
            if limite_inferior <= numero_ingresado <= limite_superior:
                return numero_ingresado
            print(
                f"Error: Ingrese un número entre {limite_inferior} y {limite_superior}."
            )
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero.")


def solicitar_opcion_texto_validada(
    mensaje_solicitud: str, opciones_permitidas: list[str]
) -> str:
    """Solicita una entrada de texto y valida que pertenezca a la lista de opciones permitidas."""
    opciones_normalizadas = [
        opcion.lower() for opcion in opciones_permitidas
    ]
    while True:
        entrada_usuario = input(mensaje_solicitud).strip().lower()
        if entrada_usuario in opciones_normalizadas:
            return entrada_usuario
        print(
            f"Error: Opción inválida. Opciones válidas: {', '.join(opciones_permitidas)}"
        )


def seleccionar_modo_juego() -> int:
    """Muestra y valida el menú para seleccionar la modalidad de juego (PvE o PvP)."""
    print("\n--- Seleccione el Modo de Juego ---")
    print("1. Jugador vs Entorno (PvE)")
    print("2. Jugador vs Jugador (PvP)")
    return solicitar_entero_validado("Opción: ", 1, 2)