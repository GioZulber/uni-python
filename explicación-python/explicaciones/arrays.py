# Creación de una lista, en este caso vacía.
lista = []
# Creación de una lista con valores iniciales.
lista2 = [1, 2, 3, 4, 5]

"""
Para recorrer una lista podemos usar un ciclo for, que nos permite ejecutar un bloque de código para cada elemento de la lista.
En este caso, el bloque de código que se ejecuta es un print, que muestra en la consola cada elemento de la lista.
"""
# Recorrer una lista
# Para cada elemento de la lista2, que es una lista de numeros, se va a ejecutar el bloque de codigo que se encuentra dentro del ciclo for.
for elemento in lista2:
     # Muestra en la consola cada elemento de la lista.
	print(elemento) # Va a mostrar en consola: 1, 2, 3, 4, 5
 
# Recorrer una lista con un ciclo for y un rango de valores
# El range va a contar la cantidad de veces que se ejecuta el ciclo for, en este caso 5 veces.
# El range funciona como un contador, en este caso va a contar desde 0 hasta 4, porque el ultimo valor no se incluye ya que el indice de las listas comienza desde el 0.
# Es decir si quiero el numero 3 de la lista, tengo que pedir el indice 2.
# Por mas que no le pasemos un valor inicial, el range comienza desde 0.
for i in range(0, 5):
    # Muestra en la consola el numero 3, que es el elemento que se encuentra en el indice 2 de la lista.
	print(lista2[2]) # Va a mostrar en consola: 3
    # # Muestra en la consola el indice de cada elemento de la lista.
	print(lista2[i]) # Va a mostrar en consola: 1, 2, 3, 4, 5
 
# Esto es lo mismo que el ejemplo anterior, pero en este caso el range comienza desde el indice 2 y termina en el indice 4.
for i in range(2, 5):
	print(lista2[i]) # Va a mostrar en consola: 3, 4, 5

"""
	En el caso anterior le estamos pasando la cantidad de elementos que tiene la lista de forma manual, pero si no sabemos cuantos elementos tiene la lista podemos usar la funcion len.
	Esta funcion len() nos devuelve la cantidad de elementos que tiene la lista.
"""
largoDeLaLista = len(lista2)
print(largoDeLaLista) # Va a mostrar en consola: 5

# Recorrer una lista con un ciclo for y la funcion len
for i in range(len(lista2)):
    #Lo que hace el [i] es mostrar cada elemento que se encuentra en el indice i de la lista. Empieza en el indice 0 y termina en el indice 4.
    print(lista2[i]) # Va a mostrar en consola: 1, 2, 3, 4, 5


# Vamos a agregar elementos a lista con un ciclo for y la funcion append
for i in range(0, 5):
    lista.append(i) # Va a agregar a la lista los numeros del 0 al 4.
    print(lista) # Va a mostrar en consola: [0, 1, 2, 3, 4]