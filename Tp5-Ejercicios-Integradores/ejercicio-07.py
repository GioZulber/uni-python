'''
Leer un número entero e invertir las cifras que contiene. 
Imprimir por pantalla el número invertido. 
Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321.
'''

num = int(input("Ingrese un número: "))


if(num < 0):
	num = num * -1

