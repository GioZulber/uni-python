'''
Realizar un programa para ingresar desde el teclado un conjunto de números. Al finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lectura con -1.
'''
num = int(input("Ingrese un numero, para finalizar ingrese -1. "))

while num != -1: 
	print("El numeor ingresado es:", num)
	num = int(input("Ingrese un numero, para finalizar ingrese -1. "))


