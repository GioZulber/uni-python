'''
Ingresar números, hasta que la suma de los números pares supere 100. Mostrar cuántos números se ingresaron en total.
'''

counter = 0
acum = 0
while (acum < 100):
	num = int(input("Ingrese numeros menores a 100:"))
	if num % 2 == 0: 
		acum += num
		
	counter += 1
	
print("Se ingresaron un total de", counter, "números.")
