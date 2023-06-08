"""
Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos 
repetidos. El valor de N se ingresa por teclado. 
Resolver este problema utilizando dos estrategias distintas:
	Impidiendo el agregado de elementos repetidos
	Eliminando los duplicados luego de generar la lista. 
Asegurarse que la cantidad final de elementos sea la solicitada.
"""
import random


# Estrategia 1
def save_in_list(n):
    array = []
    while len(array) < n:
        num = random.randint(0, 100)
        if num not in array:
            array.append(num)
    return array


# Estrategia 2
def save_in_list2(n):
    array = []
    while len(array) < n:
        num = random.randint(0, 100)
        array.append(num)
    return list(array)


def delete_duplicated(array):
    list = []
    for i in array:
        if i not in list:
            list.append(i)
    return list


n = int(input("Ingrese la cantidad de elementos: "))

arrayNoRepeats = save_in_list(n)
print(len(arrayNoRepeats))
print(arrayNoRepeats)

generateList = save_in_list2(n)
arrayNoRepeats2 = delete_duplicated(generateList)

print(len(arrayNoRepeats2))
