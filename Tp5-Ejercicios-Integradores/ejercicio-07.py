'''
Leer un número entero e invertir las cifras que contiene. 
Imprimir por pantalla el número invertido. 
Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321.
'''

num = int(input("Ingrese un número: "))

negative = False
reverse = 0


if num < 0 :
	negative = True
	num *= -1

while num != 0:	
	last_number = num % 10
	reverse = (reverse * 10) + last_number
	num = num // 10 
 
print("Número invertido", reverse)
