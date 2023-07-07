"""
Ejercicio 8:
Desarrollar una función que genere la siguiente matriz de NxN, donde N debe ser un número par: 
Observar que el patrón de relleno se realiza por cuadrantes, utilizando números correlativos a partir de 1. 
Escribir también un programa para ingresar N, invocar a la función y mostrar la matriz obtenida.
"""
import random

# Re hcaer
def createMatriz(num):
    matriz = []
    for i in range(num):
        matriz.append([])
        for j in range(num):
            if matriz[i] > 1 and matriz[i] < num:
                matriz[i].append(random.randint(1,10))
            else: 
                
    return matriz

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" , ")
        print()

def __main__():
    num = int(input("Ingrese un numero par: "))
    while num % 2 == 0:
        print("ERROR: El numero ingresado no es par, intente nuevamente.")
        num = int(input("Ingrese un numero par: "))
    
    matriz = createMatriz(num)
    printMatriz(matriz)