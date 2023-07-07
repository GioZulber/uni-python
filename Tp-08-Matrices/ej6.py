"""
Ejercicio 6:
Utilizando la función creada en el ejercicio anterior, desarrollar un programa para crear dos matrices de 3x3 
con valores al azar entre dos números ingresados por teclado. Verificar que el rango sea válido, 
en caso contrario solicitar nuevamente ambos valores. 
Construir una nueva matriz donde cada elemento se obtenga como resultado de sumar los elementos correspondientes en las matrices originales. 
Mostrar todas las matrices y el total obtenido.
"""
import random

def createMatriz(A, B ):
    if A == B:
        return []
    
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append(random.randint(A,B))
    return matriz

def printMatriz(matriz):
    if matriz != []:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=",")
            print()
    else:
        print(matriz)
        

def sumMatriz(matriz1, matriz2):
    
    if len(matriz1) != len(matriz2)  or len(matriz1[0]) != len(matriz2[0]):
        return []
    
    newMatriz = []
    for i in range(len(matriz1)):
        newMatriz.append([])
        for j in range(len(matriz1[i])):
            newMatriz[i].append(matriz1[i][j] + matriz2[i][j])
    
    return newMatriz


def __main__ ():
    A = int(input("Ingrese un numero de valor minimo: "))
    B = int(input("Ingrese un numero de valor maximo: "))
    
    while A > B:
        print("El primer numero debe ser menor al segundo")
        A = int(input("Ingrese un numero: "))
        B = int(input("Ingrese un numero: "))
    
    matriz = createMatriz(A,B)
    print("Matriz 1: ")
    printMatriz(matriz)
    matriz2 = createMatriz(A,B)
    print("Matriz 2: ")
    printMatriz(matriz2)
    print("Suma de las matrices: ")
    suma = sumMatriz(matriz, matriz2)
    printMatriz(suma)

__main__()