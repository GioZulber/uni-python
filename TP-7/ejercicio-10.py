"""
Eliminar de una lista de números enteros los valores que se 
encuentren en una segunda lista. 
Imprimir la lista original, la lista de valores a eliminar y 
la lista resultante. 
Ambas listas deben rellenarse con números al azar. La cantidad 
y el rango de los valores los decide el programador. 
"""

import random


def generate_list(n):
    array = []
    while len(array) < n:
        num = random.randint(0, 20)
        array.append(num)
    return array


original_list = generate_list(10)
print("LISTA ORIGINAL -->", original_list)


def generate_second_list(n):
    array = []
    while len(array) < n:
        num = random.randint(0, 20)
        array.append(num)
    return array


second_list = generate_second_list(20)
print("SEGUNDA LISTA -->", second_list)


def delete_duplicated(orginal, second):
    result_list = []
    list_eliminated = []
    for i in orginal:
        if i in second:
            list_eliminated.append(i)
        else:
            result_list.append(i)
    return result_list, list_eliminated


(result_list, list_eliminated) = delete_duplicated(original_list, second_list)

print("LISTA ELIMINADA -->", list_eliminated)
print("LISTA RESULTANTE -->", result_list)
