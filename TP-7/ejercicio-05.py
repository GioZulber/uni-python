"""
Ejercicio 5:
Desarrollar una función que reciba la lista como parámetro 
y devuelva una nueva lista con los mismos elementos de la primera, pero en orden inverso. 
Por ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5].
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


def reverse_list(list):
    reversed = []
    for i in range(len(list)):
        reversed.append(list[len(list) - i - 1])
    return reversed


reversed = reverse_list(list)

print("La lista original es:", list)
print("La lista invertida es:", reversed)
