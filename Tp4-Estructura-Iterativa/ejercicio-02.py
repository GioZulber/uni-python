'''
Realizar un programa para ingresar desde el teclado un conjunto de números e informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar la lectura de datos con -1. 
'''

isPair = False
num = 0

while num != -1:
	num = int(input("Ingrese  de numeros. Para finalizar ingrese -1. "))	
	if ( isPair == False): 
		isPair = True 
		print("La cantidad de elementos ingresada es inpar")

	else: 
		isPair = False
		print("La cantidad de elementos ingresada es par")
