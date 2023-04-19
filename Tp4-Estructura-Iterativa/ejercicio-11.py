'''
Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no.
Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad.
'''

num = int(input("-----Ingrese un número para determinar si es primo o no: "))

counter = 1 
divisors = 0
while counter <= num: 
	if num % counter == 0:
		divisors += 1
	counter += 1
	
if (divisors <= 2):
	print("Este numero es primo:", num)
else: 
	print("Este numero no es primo:", num)
     
 
