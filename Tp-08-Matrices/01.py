"""
	Ejercicio 1:Crear una matriz de 3x4 (3 filas y 4 columnas) con valores obtenidos al azar entre 1 y 10. 
 	Mostrar la matriz por pantalla respetando el formato de 3 filas y 4 columnas.
"""

import random


def createMatriz(rows, columns):
	matriz = []
	for i in range(rows):
		matriz.append([])
		for j in range(columns):
			matriz[i].append(random.randint(1,10))
	return matriz

def printMatriz(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print(matriz[i][j], end=" ")
		print()

def main():
	matriz = createMatriz(3,4)
	printMatriz(matriz)
 
main()