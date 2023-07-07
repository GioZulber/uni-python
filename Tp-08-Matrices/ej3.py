"""
Ejercicio 3: Generar una matriz de MxN con valores al azar comprendidos entre A y B. 
Mostrar la suma de los valores ubicados sobre la diagonal principal. Los valores de A y B también se ingresan por teclado.
"""
import random


def createMatriz(M, N, A, B):
    matriz = []
    for i in range(M):
        matriz.append([])
        for j in range(N):
            matriz[i].append(random.randint(A,B))
    return matriz

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=",")
        print()

def sumDiagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j: 
                suma = suma + matriz[i][j]
    return suma


def main():
    M = int(input("Ingrese un numero para darle valor a las filas: "))
    N = int(input("Ingrese un numero para darle valor a las columnas: "))
    A = int(input("Ingrese un numero: "))
    B = int(input("Ingrese un numero: "))
    matriz = createMatriz(M, N, A, B)
    printMatriz(matriz)
    suma = sumDiagonal(matriz)
    print("La suma de los elementos ubicados en la diagonal principal de la matriz es: ", suma)
    
main()