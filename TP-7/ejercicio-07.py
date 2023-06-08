"""
Ejercicio 7:
Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada.
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


def ordenarLista(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


def busquedaBinaria(lista, value):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == value:
            print(value)
            pos = centro
        elif lista[centro] < value:
            izq = centro + 1
        else:
            der = centro - 1
    return pos


list = save_in_list(1, 50)

listaOrdenada = ordenarLista(list)

print(listaOrdenada)

print(busquedaBinaria(listaOrdenada, 25))
