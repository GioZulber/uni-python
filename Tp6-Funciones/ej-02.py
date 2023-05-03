'''
Dados dos parámetros enteros A y B, obtener A^B (A elevado a la B) mediante multiplicaciones sucesivas, 
utilizando la función del ejercicio anterior para multiplicar. 
Por ejemplo 4^3 = 4 * 4 * 4.
'''

def multiplication(num1, num2):
	res = num1
	counter = 1
	while counter < num2:
		res *= num1
		counter += 1
	print(counter)
	print(res)
 
multiplication(4,3)