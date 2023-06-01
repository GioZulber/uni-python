"""
Ejercicio 3:
Determinar si la lista es capicúa (palíndromo).
Una lista capicúa se lee de igual modo de izquierda a derecha y de derecha a izquierda. 
Por ejemplo, [2, 7, 7, 2] es capicúa, mientras que [2, 7, 5, 2] no lo es.
"""


def save_in_list(num, A, B):
    array = []

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


num = int(input("Ingrese un numero: "))

list = save_in_list(num, 1, 50)


def es_capicua(lista):
    reversed = []
    list = lista.copy()
    for i in range(len(lista)):
        last_digit = lista.pop()
        reversed.append(last_digit)
    if list == reversed:
        return True
    else:
        return False


if es_capicua(list):
    print("La lista es capicúa.")
else:
    print("La lista no es capicúa.")
