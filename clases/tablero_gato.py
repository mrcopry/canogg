"""Modelo del tablero de Tres en Raya (Gato)."""

SIMBOLOS_JUGADORES = ("X", "O")

COMBINACIONES_GANADORAS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
    (0, 4, 8), (2, 4, 6),             # Diagonales
)


class TableroGato:
    """Tablero 3x3. Las casillas libres muestran su número (1-9)."""

    def __init__(self) -> None:
        self.casillas: list[str] = [str(i + 1) for i in range(9)]

    def mostrar(self) -> None:
        """Imprime el tablero en la terminal."""
        c = self.casillas
        print(f"\n {c[0]} | {c[1]} | {c[2]} ")
        print("---+---+---")
        print(f" {c[3]} | {c[4]} | {c[5]} ")
        print("---+---+---")
        print(f" {c[6]} | {c[7]} | {c[8]} \n")

    def esta_ocupada(self, posicion: int) -> bool:
        """Indica si la casilla (índice 0-8) ya tiene un símbolo."""
        return self.casillas[posicion] in SIMBOLOS_JUGADORES

    def marcar(self, posicion: int, simbolo: str) -> None:
        """Coloca el símbolo en la casilla (índice 0-8)."""
        self.casillas[posicion] = simbolo

    def casillas_disponibles(self) -> list[int]:
        """Devuelve los índices (0-8) de las casillas libres."""
        return [i for i in range(9) if not self.esta_ocupada(i)]

    def esta_lleno(self) -> bool:
        """Indica si ya no quedan casillas libres."""
        return not self.casillas_disponibles()

    def hay_ganador(self, simbolo: str) -> bool:
        """Indica si el símbolo completa alguna línea ganadora."""
        return any(
            all(self.casillas[posicion] == simbolo for posicion in combo)
            for combo in COMBINACIONES_GANADORAS
        )
