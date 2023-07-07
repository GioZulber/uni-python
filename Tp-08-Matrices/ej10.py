"""
Ejercicio 10:
Ingresar valores desde el teclado en una matriz de MxN y mostrar la matriz creada. 
Ordenar cada una de las filas utilizando los distintos métodos de ordenamiento estudiados. 
Mostrar nuevamente la matriz.
"""
import random

def createMatriz(N, M):
    matriz = []
    for i in range(N):
        matriz.append([])
        for j in range(M):
            # num = int(input("Ingrese un numero: "))
            matriz[i].append(random.randint(0, 50))
    return matriz

def printMatriz(matriz):
    if matriz != []:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=",")
            print()
    else:
        print(matriz)
        
        
#  Metodo de burbujeo
def orderRows(matriz):
    for i in range(len(matriz)):
        disorder = True
        while disorder:
            disorder = False
            for j in range(len(matriz[i]) -1):
                if matriz[i][j] > matriz[i][j+1]:
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[i][j+1]
                    matriz[i][j+1] = aux
                    disorder = True
    return matriz


# Metodo de insercion

"""
def orderRows(matriz):
    for i in range(len(matriz)):
        for j in range(1, len(matriz[i])):
            aux = matriz[i][j]
            k = j - 1
            while k >= 0 and matriz[i][k] > aux:
                matriz[i][k+1] = matriz[i][k]
                k = k - 1
            matriz[i][k+1] = aux
    return matriz
"""
    


def main():
    N = int(input("Ingrese un numero para darle valor a las filas: "))
    M = int(input("Ingrese un numero para darle valor a las columnas: "))
    
    matriz = createMatriz(N, M)
    
    print("Matriz sin ordenar")
    printMatriz(matriz)
    
    print("Matriz ordenada")
    printMatriz(orderRows(matriz))
main()