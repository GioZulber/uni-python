"""
Ejercicio 3:Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales. 
"""

alumno=input("Ingrese su nombre: ")
nota1=int(input("Ingrese la nota del primer parcial: "))
nota2=int(input("Ingrese la nota del segundo parcial: "))

promedio = (nota1 + nota2) / 2

if (promedio > 4):
	print("El promedio del alumno es: ", promedio, "\n"
       "Esta aprobado.")
else: 
	print("El promedio del alumno es: ", promedio, "\n"
       "Esta desaprobado."
	   	)

