'''
Calcular y devolver el Máximo Común Divisor de dos enteros no negativos,
basándose en las siguientes fórmulas matemáticas:
	∑MCD(X,X) = X
	∑MCD(X,Y) = MCD(Y, X)
	∑Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
 Ejemplo: MCD(40, 15) devuelve 5.
'''

def mcd(num1, num2):
    # Si son el mismo numero, devuelvo ese numero
	if num1 == num2:
		return num1
	# Si el primero es menor que el segundo, invierto los numeros
	elif num1 < num2:
		# llamando a la funcion con los numeros invertidos
		mcd(num2, num1)
	elif (num2 == 0):
		# Si el segundo numero es 0, devuelvo el primero
		return num1
	else:
		# Si el segundo numero es mayor que 0, 
  		# llamo a la funcion con los numeros
		return mcd(num1 - num2, num2)
	# Si el segundo numero es mayor que 0,
	while num2 > 0:
		# guardo el primer numero en una variable auxiliar
		aux = num1
		# el primer numero pasa a ser el segundo
		num1 = num2
		# el segundo numero pasa a ser el resto de la division
		num2 = aux % num2		
	return num1 

print(mcd(40, 15))