def binary_search(l, objeto, min=None, max=None):
    if min is None:
        min = 0
    if max is None:
        max = len(l) - 1

    if max < min:
        return -1

    # example l = [1, 3, 5, 10, 12]  # should return 3
    punto_medio = (min + max) // 2  # 2

    # we'll check if l[midpoint] == target, and if not, we can find out if
    # target will be to the left or right of midpoint
    # we know everything to the left of midpoint is smaller than the midpoint
    # and everything to the right is larger
    
    if l[punto_medio] == objeto:
        return punto_medio
    elif objeto < l[punto_medio]:
        return binary_search(l, objeto, min, punto_medio - 1)
    else:
        # target > l[midpoint]
        return binary_search(l, objeto, punto_medio + 1, max)
    
if __name__=='__main__':
    l=[]
n = int(input("Ingrese la cantidad de números enteros que quiere enlistar:"))

for x in range(n):
    valor=int(input("Ingrese número entero de la lista y pulse enter para el siguiente "))
    l.append(valor)

print(l)
print("Ingrese el número que desea comprobar si pertenece a la lista")
objeto = int(input())

if binary_search(l, objeto) > -1:
    print(f"Sí pertenece y está en la posición {binary_search(l, objeto) + 1}")
else: 
    print("No está en la lista")
