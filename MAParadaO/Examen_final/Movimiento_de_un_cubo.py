class Cube:
    def __init__(self):
        self.colors = {
            'O ': '\033[1m\033[37m',  # Blanco
            ' O': '\033[38;5;208m',  # Naranja
            'O.': '\033[1m\033[92m',  # Verde
            '.O': '\033[1m\033[31m',  # Rojo
            'O,': '\033[1m\033[94m',  # Azúl
            ',O': '\033[1m\033[93m'   # Amarillo
        }
        self.cube = [['O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O '],
                     [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'],
                     ['O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.'],
                     ['.O', '.O', '.O', '.O', '.O', '.O', '.O', '.O', '.O'],
                     ['O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,'],
                     [',O', ',O', ',O', ',O', ',O', ',O', ',O', ',O', ',O']]

    # Rotar una fila hacia la izquierda

    def rotate_row_left(self, row):
        temp = self.cube[0][3 * row:3 * row + 3]
        self.cube[0][3 * row:3 * row + 3] = self.cube[4][3 * row:3 * row + 3]
        self.cube[4][3 * row:3 * row + 3] = self.cube[2][3 * row:3 * row + 3]
        self.cube[2][3 * row:3 * row + 3] = self.cube[5][3 * row:3 * row + 3]
        self.cube[5][3 * row:3 * row + 3] = temp


    # Rotar una fila hacia la derecha

    def rotate_row_right(self, row):
        temp = self.cube[0][3 * row:3 * row + 3]
        self.cube[0][3 * row:3 * row + 3] = self.cube[5][3 * row:3 * row + 3]
        self.cube[5][3 * row:3 * row + 3] = self.cube[2][3 * row:3 * row + 3]
        self.cube[2][3 * row:3 * row + 3] = self.cube[4][3 * row:3 * row + 3]
        self.cube[4][3 * row:3 * row + 3] = temp


    # Rotar una columna hacia arriba

    def rotate_column_up(self, col):
        temp = [self.cube[0][col], self.cube[0][col + 3], self.cube[0][col + 6]]
        self.cube[0][col] = self.cube[3][col]
        self.cube[0][col + 3] = self.cube[3][col + 3]
        self.cube[0][col + 6] = self.cube[3][col + 6]
        self.cube[3][col] = self.cube[2][col]
        self.cube[3][col + 3] = self.cube[2][col + 3]
        self.cube[3][col + 6] = self.cube[2][col + 6]
        self.cube[2][col] = self.cube[1][col]
        self.cube[2][col + 3] = self.cube[1][col + 3]
        self.cube[2][col + 6] = self.cube[1][col + 6]
        self.cube[1][col] = temp[0]
        self.cube[1][col + 3] = temp[1]
        self.cube[1][col + 6] = temp[2]


    # Rotar una columna hacia abajo


    def rotate_column_down(self, col):
        temp = [self.cube[0][col], self.cube[0][col + 3], self.cube[0][col + 6]]
        self.cube[0][col] = self.cube[1][col]
        self.cube[0][col + 3] = self.cube[1][col + 3]
        self.cube[0][col + 6] = self.cube[1][col + 6]
        self.cube[1][col] = self.cube[2][col]
        self.cube[1][col + 3] = self.cube[2][col + 3]
        self.cube[1][col + 6] = self.cube[2][col + 6]
        self.cube[2][col] = self.cube[3][col]
        self.cube[2][col + 3] = self.cube[3][col + 3]
        self.cube[2][col + 6] = self.cube[3][col + 6]
        self.cube[3][col] = temp[0]
        self.cube[3][col + 3] = temp[1]
        self.cube[3][col + 6] = temp[2]

    def print_cube(self):
        for i in range(0, 6):
            print("----------------")
            for j in range(3):
                print(f"| {self.colors[self.cube[i][3 * j]]}{self.cube[i][3 * j]} \033[0m", end="")
                print(f"| {self.colors[self.cube[i][3 * j + 1]]}{self.cube[i][3 * j + 1]} \033[0m", end="")
                print(f"| {self.colors[self.cube[i][3 * j + 2]]}{self.cube[i][3 * j + 2]} \033[0m|")
            print("----------------")


def main():
    cube = Cube()
    cube.print_cube()

    while True:
        print("\n============================")
        print("Selecciona una opción:")
        print("1. Rotar fila hacia la izquierda")
        print("2. Rotar fila hacia la derecha")
        print("3. Rotar columna hacia arriba")
        print("4. Rotar columna hacia abajo")
        print("5. Salir")
        print("============================")

        option = int(input("Opción: "))

        if option == 1:
            row = int(input("Indica el número de la fila a rotar (0-2): "))
            cube.rotate_row_left(row)
        elif option == 2:
            row = int(input("Indica el número de la fila a rotar (0-2): "))
            cube.rotate_row_right(row)
        elif option == 3:
            col = int(input("Indica el número de la columna a rotar (0-2): "))
            cube.rotate_column_up(col)
        elif option == 4:
            col = int(input("Indica el número de la columna a rotar (0-2): "))
            cube.rotate_column_down(col)
        elif option == 5:
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

        cube.print_cube()


if __name__ == "__main__":
    main()