"""
Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o si debe recuperar. 
Informar un error si el valor de alguna nota no está entre 0 y 10.∑Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.∑
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.∑Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""
primerParcial = int(input("Ingrese la nota del primer parcial: "))
segundoParcial = int(input("Ingrese la nota del segundo parcial: "))

promocion = (primerParcial + segundoParcial) / 2

if (promocion >= 7):
	print("El alumno promociono la materia con: ",promocion, "\n"
       "Felicidades.")
elif (promocion < 7 and primerParcial >= 4 and  segundoParcial >= 4 ): 
	print("El alumno no promociono: ",promocion, "\n"
       "Debera rendir el final.")
else : 
	print("El alumno debera recuperar la materia.")
