"""
Ejercicio 6:
Escribir una función para devolver una lista con todas las posiciones que ocupa un valor pasado como parámetro, utilizando búsqueda secuencial en una lista desordenada. 
La función debe devolver una lista vacía si el elemento no se encuentra en la lista original.
"""


def save_in_list(A, B):
    array = []
    aux = 0
    if A > B:
        aux = A
        A = B
        B = aux

    num = int(input("Ingrese un numero: "))

    while num != -1:
        if num >= A and num <= B:
            array.append(num)
            num = int(input("Ingrese un numero: "))
        else:
            print(
                "[ERROR] El numero ingresado no esta en el rango. Intente nuevamente."
            )
            num = int(input("Ingrese un numero: "))
    return array


def search(list, value):
    positions = []
    for i in range(len(list)):
        if list[i] == value:
            positions.append(i)
    return positions


list = save_in_list(1, 50)

print(search(list, 5))
