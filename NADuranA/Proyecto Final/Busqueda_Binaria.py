## Definamos la funcion de busqueda binaria
def busqueda_binaria(lista, n, objetivo):

	## se define el inicio
	i = 0

	## se escriben las variables que definen el rango de busqueda
	## y se inician con las condiciones de la lista
	izq = 0
	der = n - 1

	## se repite sobre la lista
	while i < n:
		## buscando el punto medio
		punto_medio = (izq + der) // 2

		## se compara el punto medio con el elemento objetivo
		if lista[punto_medio] == objetivo:
			## si esta entonces es verdadero
			return True
		elif lista[punto_medio] <objetivo:
			## ajustando el area de busqueda a la derecha
			izq = punto_medio + 1
		else:
			## ajustando el area de busqueda a la izquierda
			der = punto_medio - 1
		i += 1
	return False


if __name__ == '__main__': #permitimos que se pueda usar como un módulo
	## iniciando el proceso para que el usuario provea una lista 
	lista =  list(input("inserte la lista de numeros ordenados en la que desea buscar: "))
	n = len(lista)
	elemento_objetivo=input("Por favor escriba el numero el cual desea comprobar que esta en la lista:")
	# se hace que el usuario pida buscar el elemento

	if busqueda_binaria(lista, n, elemento_objetivo):
		print(elemento_objetivo, "is found")
	else:
		print(elemento_objetivo, "is not found")
