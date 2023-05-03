'''
Calcular y devolver el Máximo Común Divisor de dos enteros no negativos,
basándose en las siguientes fórmulas matemáticas:
	∑MCD(X,X) = X
	∑MCD(X,Y) = MCD(Y, X)
	∑Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
 Ejemplo: MCD(40, 15) devuelve 5.
'''

def mcd(num1, num2):
	if num1 == num2:
		print(num1)
		return num1
	if num1 < num2:	 
		num1, num2 = num2, num1
	if (num2 == 0):
		print(num1)
		return num1
	while num2 > 0:
		num1, num2 = num2, num1 % num2	
	print(num1)	

mcd(40, 15)