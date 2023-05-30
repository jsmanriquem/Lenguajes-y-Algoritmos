class Cube:
    def __init__(self):
        self.cube = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                     ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                     ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                     ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]

    def rotate_row_left(self, row):
        temp = self.cube[0][3 * row:3 * row + 3]
        self.cube[0][3 * row:3 * row + 3] = self.cube[4][3 * row:3 * row + 3]
        self.cube[4][3 * row:3 * row + 3] = self.cube[2][3 * row:3 * row + 3]
        self.cube[2][3 * row:3 * row + 3] = self.cube[5][3 * row:3 * row + 3]
        self.cube[5][3 * row:3 * row + 3] = temp

    def rotate_row_right(self, row):
        temp = self.cube[0][3 * row:3 * row + 3]
        self.cube[0][3 * row:3 * row + 3] = self.cube[5][3 * row:3 * row + 3]
        self.cube[5][3 * row:3 * row + 3] = self.cube[2][3 * row:3 * row + 3]
        self.cube[2][3 * row:3 * row + 3] = self.cube[4][3 * row:3 * row + 3]
        self.cube[4][3 * row:3 * row + 3] = temp

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
        print("         ---------------")
        print("        | " + self.cube[0][0] + " | " + self.cube[0][1] + " | " + self.cube[0][2] + " |")
        print("        |---|---|---|")
        print("        | " + self.cube[0][3] + " | " + self.cube[0][4] + " | " + self.cube[0][5] + " |")
        print("        |---|---|---|")
        print("        | " + self.cube[0][6] + " | " + self.cube[0][7] + " | " + self.cube[0][8] + " |")
        print("-----------------------------")
        for i in range(1, 5):
            print("         ---------------")
            print("        | " + self.cube[i][0] + " | " + self.cube[i][1] + " | " + self.cube[i][2] + " |")
            print("        |---|---|---|")
            print("        | " + self.cube[i][3] + " | " + self.cube[i][4] + " | " + self.cube[i][5] + " |")
            print("        |---|---|---|")
            print("        | " + self.cube[i][6] + " | " + self.cube[i][7] + " | " + self.cube[i][8] + " |")
            print("-----------------------------")
            print("|---|---|---|---|---|---|---|---|---|")
        print("        | " + self.cube[5][0] + " | " + self.cube[5][1] + " | " + self.cube[5][2] + " |")
        print("        |---|---|---|")
        print("        | " + self.cube[5][3] + " | " + self.cube[5][4] + " | " + self.cube[5][5] + " |")
        print("        |---|---|---|")
        print("        | " + self.cube[5][6] + " | " + self.cube[5][7] + " | " + self.cube[5][8] + " |")
        print("         ---------------")


def main():
    cube = Cube()
    cube.print_cube()

    while True:
        print("\n==============================")
        print("Selecciona una opción:")
        print("1. Rotar fila hacia la izquierda")
        print("2. Rotar fila hacia la derecha")
        print("3. Rotar columna hacia arriba")
        print("4. Rotar columna hacia abajo")
        print("5. Salir")
        print("==============================")

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