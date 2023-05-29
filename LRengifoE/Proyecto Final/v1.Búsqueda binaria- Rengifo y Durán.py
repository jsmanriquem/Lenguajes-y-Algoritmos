#Esta versión 1 del proyecto de búsqueda binaria solicita al usuario una lista ordenada de números y un número que desee conocer si pertenece a la lista. 
#Adicionalmente, el programa indicará el índice del número en el arreglo.

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
        return binary_search(l, objeto, punto_medio + 1, max)
    
    #Ahora, permitimos que se use como módulo y como script. 
    #A continuación, usamos la función input para solicitar al usuario
    #la lista que desee ingresar
if __name__=='__main__':
    l=[]
valor=int(input("Ingresar valor de la lista (ingrese 0 para finalizar):"))


while valor!=0:
    l.append(valor)
    valor=int(input("Ingresar valor de la lista (ingrese 0 para finalizar):"))

    #La función append permite recopilar los fatos ingresados. Es decir  mientras el usuario
    #ingrese valores distintos a 0, el programa "guarda" los datos.
print(l)
print("Ingrese el número que desea comprobar si pertenece a la lista")
objeto = int(input())

#Llamamos a la función binary_search, definida anteriormente para verificar 
#el índice del elemento
if binary_search(l, objeto) > -1:
    print(f"Sí pertenece y está en el índice {binary_search(l, objeto)}")
else: 
    print("No está en la lista")
