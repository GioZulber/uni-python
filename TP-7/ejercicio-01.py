"""
Ejercicio 1:
Escribir una función para ingresar desde el teclado una serie de números entre A y B y guardarlos en una lista. 
En caso de ingresar un valor fuera de rango la función mostrará un mensaje de error y solicitará un nuevo número. 
Para finalizar la carga se deberá ingresar -1. La función recibe como parámetros los valores de A y B, 
y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.
"""


def save_in_list(A, B):
    array = []
    aux = 0
    if A > B:
        aux = A
        A = B
        B = aux

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


print(save_in_list(10, 50))
