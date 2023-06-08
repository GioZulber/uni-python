"""
Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar 
e imprimir el valor mínimo y el lugar que ocupa. 
Tener en cuenta que el mínimo puede estar repetido, 
en cuyo caso deberán mostrarse todas las posiciones en las que se encuentre. 
La carga de datos termina cuando se obtenga un 0 como número al azar,
el que no deberá cargarse en la lista.
"""
import random


def save_in_list():
    array = []
    for i in range(100):
        num = random.randint(0, 100)
        if num == 0:
            break
        array.append(num)
    return array


def min_value(array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
    return min


# Busqueda secuencial
def min_index(array, min):
    index = []
    for i in range(len(array)):
        if array[i] == min:
            index.append(i)
    return index


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


array = save_in_list()
print_array(array)
min = min_value(array)
print("El valor minimo es: ", min)
index = min_index(array, min)
print("El valor minimo se encuentra en las posiciones: ", end="")
print_array(index)
