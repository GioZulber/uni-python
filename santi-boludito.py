#Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
# El fin de la carga se determina ingresan-do un -1 en el legajo. 
#Informar para cada alumno si aprobó o no el examen con-siderando que se aprueba con nota mayor o igual a 4. 
# Se debe validar que la nota ingresada sea entre 1 y 10. 
#Terminada la carga de datos, informar:∑Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#∑Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
#∑Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

n_legajo = int(input('Inserte el numero de legajo o -1 para fializar = '))
nota_final = int(input('Inserte la nota final = '))


count_aplazos = 0 
count_alumnos_aprobados = 0
count_alumnos_desaprobados = 0
cant_total = 0


while n_legajo != - 1:

    if nota_final >= 1 and nota_final <= 10 :

        if nota_final == 1:
            count_alumnos_desaprobados = count_alumnos_desaprobados + 1
            count_aplazos = count_aplazos + 1
        elif nota_final <= 4:
            count_alumnos_desaprobados = count_alumnos_desaprobados + 1
        elif nota_final > 4 : 
            count_alumnos_aprobados = count_alumnos_aprobados + 1

        cant_total = cant_total + 1
    else : 
         print('numero invalido')


    print(cant_total)
    n_legajo = int(input('inserte el numero de legajo o -1 para fializar = '))
    nota_final = int(input('Inserte la nota final = '))

prom_aplazos =  (cant_total / count_aplazos) * 100

print('la cantidad de alumnos que aprobaron el examen son = ', count_alumnos_aprobados)
print('la cantidad de alumnos que desaprobaron el examen son = ', count_alumnos_desaprobados)
print('el porcentaje de alumos que estan aplazados son = ', prom_aplazos, "%")