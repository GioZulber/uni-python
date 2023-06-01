"""
Ejercicio 2:

Calcular la suma de los números de la lista.
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

list_sum = 0

for i in list:
    list_sum += i

print("La suma total de los elementos de la lista es:", list_sum)
