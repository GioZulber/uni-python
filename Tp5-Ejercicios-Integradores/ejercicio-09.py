'''
Ingresar un número N y validar que sea positivo.
Luego:a.Mostrar los primeros números impares, hasta alcanzar el número ingresado.b.Informar la suma de esos números impares.
Ejemplo:
∑Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
∑Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
∑Si se ingresa -5, se debe pedir otro número.
'''
n = int(input("Ingrese un número: "))

counter = 1
suma = 0
while n < 0: 
	print("¡ERROR! Ingreso un número negativo.")
	n = int(input("Ingrese un número: "))

while counter <= n:
	suma += counter
	print(counter)
	counter += 2

print("La suma es:", suma)