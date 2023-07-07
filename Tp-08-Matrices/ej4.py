"""
Ejercicio 4: Indicar las coordenadas del mayor valor encontrado en una matriz de MxN, generada con valores aleatorios entre 100 y 1000.    
"""

import random 

def createMatriz(rows, collumn):
    matriz = []
    for i in range(rows):
        matriz.append([])
        for j in range(collumn):
            matriz[i].append(random.randint(100,1000))
    return matriz


def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" , ")
        print()

def searchMax(matriz): 
    max = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max:
                max = matriz[i][j]
                posR = i
                posC = j
    return max, posR, posC
                
def __main__():
    M = int(input("Ingrese un numero para darle valor a las filas: "))
    N = int(input("Ingrese un numero para darle valor a las columnas: "))
    matriz = createMatriz(M, N)
    printMatriz(matriz)
    mayor, posR, posC   = searchMax(matriz)
    
    print("El mayor valor encontrado en la matriz es: ", mayor, "fue encontrado en la posicion: ", posR, ",", posC)

__main__()