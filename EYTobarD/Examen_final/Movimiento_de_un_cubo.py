class Cube:
    def __init__(self):
        # Inicialización del estado inicial del cubo
        self.cube = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],  # Cara blanca
                     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],  # Cara naranja
                     ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],  # Cara verde
                     ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],  # Cara roja
                     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],  # Cara azul
                     ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]  # Cara amarilla

    def rotate_face_clockwise(self, face):
        # Rotar una cara en el sentido de las agujas del reloj
        self.cube[face] = [self.cube[face][6], self.cube[face][3], self.cube[face][0],
                           self.cube[face][7], self.cube[face][4], self.cube[face][1],
                           self.cube[face][8], self.cube[face][5], self.cube[face][2]]

    def rotate_face_counter_clockwise(self, face):
        # Rotar una cara en sentido contrario a las agujas del reloj
        self.cube[face] = [self.cube[face][2], self.cube[face][5], self.cube[face][8],
                           self.cube[face][1], self.cube[face][4], self.cube[face][7],
                           self.cube[face][0], self.cube[face][3], self.cube[face][6]]

    def rotate_row_left(self, row):
        # Rotar una fila hacia la izquierda
        temp = self.cube[0][3 * row:3 * row + 3]
        self.cube[0][3 * row:3 * row + 3] = self.cube[4][3 * row:3 * row + 3]
        self.cube[4][3 * row:3 * row + 3] = self.cube[2][3 * row:3 * row + 3]
        self.cube[2][3 * row:3 * row + 3] = self.cube[5][3 * row:3 * row + 3]
        self.cube[5][3 * row:3 * row + 3] = temp

    def rotate_row_right(self, row):
        # Rotar una fila hacia la derecha
        temp = self.cube[0][3 * row:3 * row + 3]
        self.cube[0][3 * row:3 * row + 3] = self.cube[5][3 * row:3 * row + 3]
        self.cube[5][3 * row:3 * row + 3] = self.cube[2][3 * row:3 * row + 3]
        self.cube[2][3 * row:3 * row + 3] = self.cube[4][3 * row:3 * row + 3]
        self.cube[4][3 * row:3 * row + 3] = temp

    def rotate_column_up(self, col):
        # Rotar una columna hacia arriba
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
        # Rotar una columna hacia abajo
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
        # Imprimir el estado actual del cubo
        print("         ---------------")
        print("        | " + self.cube[0][0] + " | " + self.cube[0][1] + " | " + self.cube[0][2] + " |")
        print("        |---|---|---|")
        print("        | " + self.cube[0][3] + " | " + self.cube[0][4] + " | " + self.cube[0][5] + " |")
        print("        |---|---|---|")
        print("        | " + self.cube[0][6] + " | " + self.cube[0][7] + " | " + self.cube[0][8] + " |")
        print("-----------------------------")
        for i in range(1, 5):
            print("| " + self.cube[i][0] + " | " + self.cube[i][1] + " | " + self.cube[i][2] + " | " +
                  self.cube[i][3] + " | " + self.cube[i][4] + " | " + self.cube[i][5] + " | " +
                  self.cube[i][6] + " | " + self.cube[i][7] + " | " + self.cube[i][8] + " |")
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
        print("1. Rotar cara en el sentido de las agujas del reloj")
        print("2. Rotar cara en sentido contrario a las agujas del reloj")
        print("3. Rotar fila hacia la izquierda")
        print("4. Rotar fila hacia la derecha")
        print("5. Rotar columna hacia arriba")
        print("6. Rotar columna hacia abajo")
        print("7. Salir")
        print("==============================")

        option = int(input("Opción: "))

        if option == 1:
            face = int(input("Indica el número de la cara a rotar (0-5): "))
            cube.rotate_face_clockwise(face)
        elif option == 2:
            face = int(input("Indica el número de la cara a rotar (0-5): "))
            cube.rotate_face_counter_clockwise(face)
        elif option == 3:
            row = int(input("Indica el número de la fila a rotar (0-2): "))
            cube.rotate_row_left(row)
        elif option == 4:
            row = int(input("Indica el número de la fila a rotar (0-2): "))
            cube.rotate_row_right(row)
        elif option == 5:
            col = int(input("Indica el número de la columna a rotar (0-2): "))
            cube.rotate_column_up(col)
        elif option == 6:
            col = int(input("Indica el número de la columna a rotar (0-2): "))
            cube.rotate_column_down(col)
        elif option == 7:
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

        cube.print_cube()


if __name__ == "__main__":
    main() 