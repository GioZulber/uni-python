'''
Realizar un programa para ingresar desde el teclado un conjunto de números y mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos con un valor -1.
'''
numIn=int(input("Ingrese un conjunto de números: "))

if(numIn > 0) : 
		numMajor = numIn
		numMinor = numIn 
		while numIn != -1:
			if(numIn > numMajor):
				numMajor = numIn
			elif(numIn < numMinor): 
				numMinor = numIn
			numIn=int(input("Ingrese un conjunto de números: "))    
		print("Numero mayor: ", numMajor, "Menor: ", numMinor)

