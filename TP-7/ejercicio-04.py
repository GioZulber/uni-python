"""
Ejercicio 4:
Escribir una función para contar cuántas veces aparece un valor dentro de la lista. 
La función recibe como parámetros la lista y el valor a buscar, y devuelve un número entero.
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


list = save_in_list(1, 50)


def count(list, value):
    count = 0
    for i in list:
        if i == value:
            count += 1
    return count


print(count(list, 2))
