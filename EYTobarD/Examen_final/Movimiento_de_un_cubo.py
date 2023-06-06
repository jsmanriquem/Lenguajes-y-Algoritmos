import random

class Cubo:
    def __init__(self):
        self.colores = {
            'O ': '\033[1m\033[37m',  # Blanco
            ' O': '\033[1m\033[92m',  # Verde
            'O.': '\033[1m\033[93m',  # Amarillo
            '.O': '\033[1m\033[31m',  # Rojo
            'O,': '\033[1m\033[94m',  # Azúl
            ',O': '\033[38;5;208m',   # Naranja
        }
        self.cubo = [['O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O '],
                     [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'],
                     ['O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.'],
                     ['.O', '.O', '.O', '.O', '.O', '.O', '.O', '.O', '.O'],
                     ['O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,'],
                     [',O', ',O', ',O', ',O', ',O', ',O', ',O', ',O', ',O']]


    # Rotar una fila hacia la izquierda

    def rotar_fila_izquierda(self, fila):
        temp = self.cubo[0][3 * fila:3 * fila + 3]
        self.cubo[0][3 * fila:3 * fila + 3] = self.cubo[4][3 * fila:3 * fila + 3]
        self.cubo[4][3 * fila:3 * fila + 3] = self.cubo[2][3 * fila:3 * fila + 3]
        self.cubo[2][3 * fila:3 * fila + 3] = self.cubo[5][3 * fila:3 * fila + 3]
        self.cubo[5][3 * fila:3 * fila + 3] = temp


    # Rotar una fila hacia la derecha

    def rotar_fila_derecha(self, fila):
        temp = self.cubo[0][3 * fila:3 * fila + 3]
        self.cubo[0][3 * fila:3 * fila + 3] = self.cubo[5][3 * fila:3 * fila + 3]
        self.cubo[5][3 * fila:3 * fila + 3] = self.cubo[2][3 * fila:3 * fila + 3]
        self.cubo[2][3 * fila:3 * fila + 3] = self.cubo[4][3 * fila:3 * fila + 3]
        self.cubo[4][3 * fila:3 * fila + 3] = temp


    # Rotar una columna hacia arriba

    def rotar_columna_arriba(self, col):
        temp = [self.cubo[0][col], self.cubo[0][col + 3], self.cubo[0][col + 6]]
        self.cubo[0][col] = self.cubo[3][col]
        self.cubo[0][col + 3] = self.cubo[3][col + 3]
        self.cubo[0][col + 6] = self.cubo[3][col + 6]
        self.cubo[3][col] = self.cubo[2][col]
        self.cubo[3][col + 3] = self.cubo[2][col + 3]
        self.cubo[3][col + 6] = self.cubo[2][col + 6]
        self.cubo[2][col] = self.cubo[1][col]
        self.cubo[2][col + 3] = self.cubo[1][col + 3]
        self.cubo[2][col + 6] = self.cubo[1][col + 6]
        self.cubo[1][col] = temp[0]
        self.cubo[1][col + 3] = temp[1]
        self.cubo[1][col + 6] = temp[2]


    # Rotar una columna hacia abajo


    def rotar_columna_abajo(self, col):
        temp = [self.cubo[0][col], self.cubo[0][col + 3], self.cubo[0][col + 6]]
        self.cubo[0][col] = self.cubo[1][col]
        self.cubo[0][col + 3] = self.cubo[1][col + 3]
        self.cubo[0][col + 6] = self.cubo[1][col + 6]
        self.cubo[1][col] = self.cubo[2][col]
        self.cubo[1][col + 3] = self.cubo[2][col + 3]
        self.cubo[1][col + 6] = self.cubo[2][col + 6]
        self.cubo[2][col] = self.cubo[3][col]
        self.cubo[2][col + 3] = self.cubo[3][col + 3]
        self.cubo[2][col + 6] = self.cubo[3][col + 6]
        self.cubo[3][col] = temp[0]
        self.cubo[3][col + 3] = temp[1]
        self.cubo[3][col + 6] = temp[2]


    
    # Armar el cubo

    def armar_cubo(self):
        self.cubo = [['O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O '],
                     [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'],
                     ['O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.', 'O.'],
                     ['.O', '.O', '.O', '.O', '.O', '.O', '.O', '.O', '.O'],
                     ['O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,', 'O,'],
                     [',O', ',O', ',O', ',O', ',O', ',O', ',O', ',O', ',O']]


    # Desarmar el cubo

    def desarmar_cubo(self):

        for _ in range(random.randint(10, 60)):
            
            # Escoger aleatoriamente entre rotar fila o columna
            if random.choice([True, False]):
                fila = random.randint(0, 2)
                dirección = random.choice(['izquierda', 'derecha'])
                if dirección == 'izquierda':
                    self.rotar_fila_izquierda(fila)
                else:
                    self.rotar_fila_derecha(fila)
            else:
                col = random.randint(0, 2)
                dirección = random.choice(['arriba', 'abajo'])
                if dirección == 'arriba':
                    self.rotar_columna_arriba(col)
                else:
                    self.rotar_columna_abajo(col)

    def print_cubo(self):
        for i in range(0, 6):
            print("----------------")
            for j in range(3):
                print(f"| {self.colores[self.cubo[i][3 * j]]}{self.cubo[i][3 * j]} \033[0m", end="")
                print(f"| {self.colores[self.cubo[i][3 * j + 1]]}{self.cubo[i][3 * j + 1]} \033[0m", end="")
                print(f"| {self.colores[self.cubo[i][3 * j + 2]]}{self.cubo[i][3 * j + 2]} \033[0m|")
            print("----------------")


def main():
    cubo = Cubo()
    cubo.print_cubo()

    while True:
        print("\n============================")
        print("Selecciona una opción:")
        print("1. Rotar fila hacia la izquierda")
        print("2. Rotar fila hacia la derecha")
        print("3. Rotar columna hacia arriba")
        print("4. Rotar columna hacia abajo")
        print("5. Armar el cubo")
        print("6. Desarmar el cubo")
        print("7. Salir")
        print("============================")

        option = int(input("Opción: "))

        if option == 1:
            fila = int(input("Indica el número de la fila a rotar (0-2): "))
            cubo.rotar_fila_izquierda(fila)
        elif option == 2:
            fila = int(input("Indica el número de la fila a rotar (0-2): "))
            cubo.rotar_fila_derecha(fila)
        elif option == 3:
            col = int(input("Indica el número de la columna a rotar (0-2): "))
            cubo.rotar_columna_arriba(col)
        elif option == 4:
            col = int(input("Indica el número de la columna a rotar (0-2): "))
            cubo.rotar_columna_abajo(col)
        elif option == 5:
            cubo.armar_cubo()
        elif option == 6:
            cubo.desarmar_cubo()
        elif option == 7:
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

        cubo.print_cubo()


if __name__ == "__main__":
    main()