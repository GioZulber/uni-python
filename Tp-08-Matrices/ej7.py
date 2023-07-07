"""
Ejercicio 7:
Ingresar un número entero positivo, el que debe ser múltiplo de 4. Luego crear una matriz que contenga 4 elementos por fila, 
hasta completar la cantidad de elementos indicada. Mostrar la matriz e informar cuántas filas se crearon. 
La matriz se rellena con números al azar. 
"""
import random

def createMatriz(num):
    matriz = []
    for i in range(num):
        matriz.append([])
        for j in range(4):
            matriz[i].append(random.randint(1,100))
    return matriz

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" , ")
        print()

def __main__ ():
    a = int(input("Ingrese un numero entero positivo, el que debe ser multiplo de 4: "))
    while a % 4 != 0:
        print("ERROR: El numero ingresado no es multiplo de 4, intente nuevamente.")
        a = int(input("Ingrese un numero entero positivo, el que debe ser multiplo de 4: "))
    
    matriz = createMatriz(a)
    print("La matriz es: ")
    printMatriz(matriz)
    print()
    print("Se crearon ", a, " filas")

__main__()