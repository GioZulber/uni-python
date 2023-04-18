'''
Ingresar números, hasta que la suma de los números pares supere 100. Mostrar cuántos números se ingresaron en total.
'''

num = int(input("Ingrese numeros menores a 100:"))

counter = 0
sum = 0
while (sum < 100):
	num = int(input("Ingrese numeros menores a 100:"))
	if num % 2 == 0: 
		sum += num
		
	counter += 1
	
print("Se ingresaron un total de", counter, "números.")