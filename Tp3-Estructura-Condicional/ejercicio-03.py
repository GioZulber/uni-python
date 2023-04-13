"""
Desarrollar un programa que solicite un número de mes (por ejemplo 4)
y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido y mostrar un mensaje de error en caso de que no lo sea.
"""

mes = int(input("Ingrese el número del mes que quiera: "))

if (mes == 1) : 
	print("El mes que eligio es Enero.")
elif (mes == 2) : 
	print("El mes que eligio es Febrero.")
elif (mes == 3) : 
	print("El mes que eligio es Marzo.")
elif (mes == 4) : 
	print("El mes que eligio es Abril.")
elif (mes == 5) : 
	print("El mes que eligio es Mayo.")
elif (mes == 6) : 
	print("El mes que eligio es Junio.")
elif (mes == 7) : 
	print("El mes que eligio es Julio.")
elif (mes == 8) : 
	print("El mes que eligio es Agosto.")
elif (mes == 9) :
	print("El mes que eligio es Septiembre.")
elif (mes == 10) : 
	print("El mes que eligio es Octubre.")
elif (mes == 11) :
	print("El mes que eligio es Noviembre.")
elif (mes == 12) : 
	print("El mes que eligio es Diciembre.")
else : 
	print("[ERROR] El número es invalido.")
