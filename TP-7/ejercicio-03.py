"""
Ejercicio 3:
Determinar si la lista es capicúa (palíndromo).
Una lista capicúa se lee de igual modo de izquierda a derecha y de derecha a izquierda. 
Por ejemplo, [2, 7, 7, 2] es capicúa, mientras que [2, 7, 5, 2] no lo es.
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


def es_capicua(lista):
    reversed = []
    for i in range(len(lista)):
        reversed.append(lista[len(lista) - i - 1])
    if lista == reversed:
        return True
    else:
        return False


if es_capicua(list):
    print("La lista es capicúa.")
else:
    print("La lista no es capicúa.")
