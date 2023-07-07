"""
Ejercicio 9: 
Generar una matriz cuadrada de NxN con números al azar entre 0 y 99. 
Luego crear una lista que contenga la suma de cada una de las filas de la matriz,sin valores repetidos. 
Es decir que si dos filas suman igual, el valor debe estar una sola vez en la lista.
Mostrar por pantalla la matriz y la lista. Esta última debe ordenarse de menor a mayor.
"""
import random

def createMatriz(N):

    
    matriz = []
    for i in range(N):
        matriz.append([])
        for j in range(N):
            matriz[i].append(random.randint(0,99))
    return matriz

def printMatriz(matriz):
    if matriz != []:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=",")
            print()
    else:
        print(matriz)
    
def sumRow (matriz):
    sumas = []
    for i in range(len(matriz)):
        suma = 0
        isRepeated = False
        for j in range(len(matriz[i])): 
            suma = suma + matriz[i][j]
        k = 0
        while k < len(sumas):
            if sumas[k] == suma:
                isRepeated = True
            k = k + 1
        if isRepeated == False:
            sumas.append(suma)                
    return sumas
    
def orderList(matriz):
    lista = sumRow(matriz)
    disorder = True
    while disorder:
        disorder = False
        for i in range(len(lista) -1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                disorder = True
    return lista
     
def main ():
    N = int(input("Ingrese un numero para darle valor a las columnas: "))
    matriz = createMatriz(N) 
    printMatriz(matriz)
    
    print("Suma de cada una de las filas, en una lista ordenada: ", orderList(matriz))

main()
    