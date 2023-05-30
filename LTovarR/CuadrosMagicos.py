def crear_cuadro_magico(n):
    if n % 2 == 0:
        print("La dimensión debe ser impar.")
        return None

    cuadro = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n ** 2:
        cuadro[i][j] = num
        num += 1
        nuevo_i = (i - 1) % n
        nuevo_j = (j + 1) % n

        if cuadro[nuevo_i][nuevo_j] != 0:
            i += 1
        else:
            i, j = nuevo_i, nuevo_j

    return cuadro

def mostrar_cuadro_magico(cuadro):
    n = len(cuadro)
    suma_fila = [sum(fila) for fila in cuadro]
    suma_columna = [sum(cuadro[i][j] for i in range(n)) for j in range(n)]

    # Imprimir el cuadro mágico
    for i in range(n):
        for j in range(n):
            print(cuadro[i][j], end="\t")
        print("|", suma_fila[i])

    print("-" * (8 * n + n - 1))

    for j in range(n):
        print(suma_columna[j], end="\t")

    print()

# Ejemplo de uso
dim = int(input("Ingresa la dimensión del cuadro mágico (debe ser impar): "))
cuadro_magico = crear_cuadro_magico(dim)

if cuadro_magico:
    # Mostrar el cuadro mágico con las sumas de fila y columna
    mostrar_cuadro_magico(cuadro_magico)
