'''
Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. 
¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
'''
#Solucion 1
"""
counter = 1
while counter <= 12: 
	res = 4 * counter
	print("El resultado de 4 X", counter, "es:", res) 
	counter += 1
"""

#Solucion 2

num = int(input("Ingrese un número para ver su tabala de multiplicar."))

counter = 1
while counter <= 12: 
	res = num * counter
	print("El resultado de", num, "X", counter, "es:", res) 
	counter += 1