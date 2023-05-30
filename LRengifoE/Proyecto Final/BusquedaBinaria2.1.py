#Esta versión DEFINITIVA del proyecto de búsqueda binaria solicita al usuario una lista de números enteros no repetidos y un número que desee conocer si pertenece a la lista. 
#Adicionalmente, el programa indicará el índice del número en el arreglo.
#La funcion busqueda binaria funciona para listas de numeros ordenados sin valores repetidos, tenga eso en cuenta al usar esta funcion.
#
#
def binary_search(l, objeto, min=None, max=None):
    if min is None:
        min = 0
    if max is None:
        max = len(l) - 1

    if max < min:
        return -1

    punto_medio = (min + max) // 2  # 2

    # revisaremos si l[punto_medio] == objeto, de lo contrario, puede encontrarse si
    # el objeto estará a la izquierda o a  la derecha del punto medio
    # sabemos que todo a la izquierda del midpoint o punto medio es menor que el punto medio
    # y todo a la derecha, es mayor
    
    if l[punto_medio] == objeto:
        return punto_medio
    elif objeto < l[punto_medio]:
        return binary_search(l, objeto, min, punto_medio - 1)
    else:
        # target > l[midpoint]
        return binary_search(l, objeto, punto_medio + 1, max)
    
    
        #Ahora, permitimos que se use como módulo y como script. 
    #A continuación, usamos la función input para solicitar al usuario
    #la lista que desee ingresar
if __name__=='__main__':
    print("Bienvenido a busqueda binaria, este script te permite encontrar si un elemento pertence a una lista ordenada y su posicion en la misma, tenga en cuenta que la lista que introduzcano puede tener elementos repetidos")
    l=[]
n = int(input("Ingrese la cantidad de números enteros que quiere enlistar:"))

for x in range(n):
    valor=int(input("Ingrese el número de la lista y pulse Enter para digitar el siguiente "))
    l.append(valor)

print(l)
print("Ingrese el número que desea verificar su existencia en la lista")
objeto = int(input())

if binary_search(l, objeto) > -1:
    print(f"Sí pertenece y está en la posición {binary_search(l, objeto) + 1}")
else: 
    print("No está en la lista")
