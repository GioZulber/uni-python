"""
Ejercicio 2:

Calcular la suma de los números de la lista.
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

list_sum = 0

for i in list:
    list_sum += i

print("La suma total de los elementos de la lista es:", list_sum)
