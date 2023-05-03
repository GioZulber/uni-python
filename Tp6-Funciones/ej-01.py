'''
Escribir una función que reciba como parámetros dos números enteros. 
Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamente sumas. 
Por ejemplo 4 * 3 = 4 + 4 + 4 .
'''
def multiplication(num1, num2):
	res = 0
	counter = 0
	while counter < num2:
		res += num1
		counter += 1
	print(counter)
	print(res)
 
multiplication(4,3)