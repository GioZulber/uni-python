"""
Ejercicio 2:Generar una matriz cuadrada de NxN. Informar cuál es la suma de los elementos ubicados en el triángulo superior de la misma.
"""
import random

def createMatriz(N):
    matriz = []
    for i in range(N):
        matriz.append([])
        for j in range(N):
            matriz[i].append(random.randint(1,10))
    return matriz

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def sumaTrianguloSuperior(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # print("valor de i: ", i, "valor de j: ", j)
            if i < j:
                suma = suma + matriz[i][j]
    return suma

def main():
    N = int(input("Ingrese un numero: "))
    matriz = createMatriz(N)
    printMatriz(matriz)
    suma = sumaTrianguloSuperior(matriz)
    print("La suma de los elementos ubicados en el triangulo superior de la matriz es: ", suma)

main()
