'''
Leer 10 números enteros e imprimir su promedio, el mayor valor leído y en qué posición se encontraba. 
Si se ingresó más de una vez sólo debe informar la primera.
'''

num = int(input("Ingrese un número:"))

numMajor= 0
# pos=0  

counter = 1
counterProm = 0
while counter < 10: 
	num = int(input("Ingrese un número: "))
	if(num > numMajor):
		pos= counter
		numMajor = num
		counterProm =+ num 
		counter +=1
	else: 
		counterProm =+ num 
		counter +=1
		
prom = counterProm / 10
print("El promedio de los numeros ingresados es:", prom, "El mayor valor leido:", numMajor, "Este se encontraba en la posicion:", pos )