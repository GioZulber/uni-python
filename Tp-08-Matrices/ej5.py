"""
Ejercicio 5:
Desarrollar una función para crear una matriz de MxN. La función recibe M y N por parámetro, 
la rellena con valores al azar entre A y B (también recibidos por parámetro) y retorna la matriz creada. 
Si no hay valores entre A y B o alguna de las dimensiones es negativa se deberá retornar la matriz vacía. 
Desarrollar también un pequeño programa principal para invocar a la función y mostrar la matriz por pantalla.
Además mostrar la suma de cada fila y cada columna.
"""
import random

def createMatriz(rows, columns,  A, B ):
    if A == B or rows <= 0 or columns <= 0:
        return []
    
    matriz = []
    for i in range(rows):
        matriz.append([])
        for j in range(columns):
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
    
def sumRow (matriz):
    sumas = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma = suma + matriz[i][j]
        sumas.append(suma)
    return sumas

def sumColumn(matriz):
    sumas = []
    
    for i in range(len(matriz[0])):
        suma = 0
        for j in range(len(matriz)):
            suma = suma + matriz[j][i]
        sumas.append(suma)
    return sumas

def sums(matriz):
    for i in range(len(matriz)):
        print("Fila ", i, ": ", matriz[i])
        sum = sumRow(matriz, i)
        print("La suma de los elementos de la fila ", i, " es: ", sum)
        for j in range(len(matriz[i])):
            sumC = sumColumn(matriz, j)
            print("La suma de los elementos de la columna ", j, " es: ",sumC) 
    

def __main__():
    M = int(input("Ingrese un numero para darle valor a las filas: "))
    N = int(input("Ingrese un numero para darle valor a las columnas: "))
    A = int(input("Ingrese un numero: "))
    B = int(input("Ingrese un numero: "))
    matriz = createMatriz(M,N, A, B) 
    printMatriz(matriz)
    
    print("Suma de cada una de las filas: ", sumRow(matriz))
    print("Suma de cada una de las columnas: ", sumColumn(matriz))
   
    
    
    
__main__()
    