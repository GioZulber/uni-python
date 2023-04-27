'''
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. 
El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen con-siderando que se aprueba con nota mayor o igual a 4. 
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar: 
	Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
	Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
	Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
'''

totalAlumns = 0
totalPostponedAlumns = 0
totalAprobbedAlumns = 0
totalDisaprobbedAlumns = 0

print("Ingrese un número de legajo y nota de examen final (-1 en el legajo finalizar)")
id = int(input("Ingrese Legajo : "))
finalNote = int(input("Ingrese Nota final : "))

while id != -1:
    if finalNote >= 1 and finalNote <= 10:
        if finalNote == 1:
            totalPostponedAlumns = totalPostponedAlumns + 1
        elif finalNote >= 4:
            totalAprobbedAlumns = totalAprobbedAlumns + 1
        else: 
            totalDisaprobbedAlumns = totalDisaprobbedAlumns + 1
        totalAlumns = totalAlumns + 1
    else: 
        print("ERROR: ¡La nota introducida es invalida!")
    
    print("Ingrese un número de legajo y nota de examen final (-1 en el legajo finalizar)")
    id = int(input("Ingrese Legajo : "))
    finalNote = int(input("Ingrese Nota final : "))

if totalAlumns > 0:
    print("Cantidad de alumnos aprobados:", totalAprobbedAlumns)
    print("Cantidad de alumnos desaprobados:", totalDisaprobbedAlumns)
    print("Porcentaje de alumnos aplazados:", ( totalPostponedAlumns / totalAlumns ) * 100)
else:
    print("¡No se ingresaron alumnos!")
