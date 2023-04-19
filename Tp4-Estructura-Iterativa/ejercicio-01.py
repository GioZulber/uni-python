'''
Realizar un programa para ingresar desde el teclado un conjunto de números. 
Al finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lectura con -1.
'''
num = int(input("Ingrese un numero, para finalizar ingrese -1. "))

isFirtsNumber = False

while num != -1: 
	if(isFirtsNumber == False): 
		isFirtsNumber = num 
	lastNum = num
	num = int(input("Ingrese un numero, para finalizar ingrese -1. "))
print("El primer número ingresado es:", isFirtsNumber, "El ultimo número ingresado es:",lastNum)

