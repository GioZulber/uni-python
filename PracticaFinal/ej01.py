"""
Ejercicio 1:Leer los números de legajo de los alumnos de un curso y su nota de examen final. 
El fin de la carga se determina ingresando un -1 como legajo. Se debe validar que la nota ingresada esté entre 1 y 10. 
Terminada la lectura de datos, informar:
 Cantidad de alumnos que aprobaron con nota mayor o igual a 4
 Cantidad de alumnos que desaprobaron el examen. 
 Nota menor a 4
 Promedio de nota y los legajos que superan el promedio
 Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente según el número de legajo. 
Resolver de dos formas: Utilizando dos listas paralelas y utilizando una matriz de dos filas.
"""


# def orderMethod(legajos, notas):
#     disorder = True
    
#     while disorder:
#         disorder = False
#         for i in range(len(legajos)-1):
#             if legajos[i] > legajos[i + 1]:
#                 aux = legajos[i]
#                 legajos[i] = legajos[i + 1]
#                 legajos[i + 1] = aux
#                 aux = notas[i]
#                 notas[i] = notas[i + 1]
#                 notas[i + 1] = aux
#                 disorder = True
#     return legajos, notas


# def main():
#     listaNotas = []
#     listaLegajos = []
#     u = int(input("Legajo: (-1 para terminar) "))
#     while u != -1:
#         nota = int(input("Nota: "))
#         while nota < 1 or nota > 10:
#             nota = int(input("Nota: "))
#         listaNotas.append(nota)
#         listaLegajos.append(u)
#         matriz = createMatriz()
#         u = int(input("Legajo: (-1 para terminar) "))
#     print()
    
#     leg, notas = orderMethod(listaLegajos, listaNotas)
#     print("Legajos ordenados: ", leg)
#     print("Notas ordenadas: ", notas)
    
#     # print(listaLegajos)
#     # print(listaNotas)
#     # print()
#     # print()
#     # print()
# main()


alumnos = []

# Lectura de datos
while True:
    legajo = int(input("Ingrese número de legajo (-1 para finalizar): "))
    if legajo == -1:
        break
    
    nota = int(input("Ingrese la nota del examen final (entre 1 y 10): "))
    while nota < 1 or nota > 10:
        print("Nota inválida. Intente nuevamente.")
        nota = int(input("Ingrese la nota del examen final (entre 1 y 10): "))
    
    alumnos.append([legajo, nota])

# Cálculo de estadísticas
cantidad_aprobados = 0
cantidad_desaprobados = 0
suma_notas = 0

for alumno in alumnos:
    suma_notas += alumno[1]
    if alumno[1] >= 4:
        cantidad_aprobados += 1
    else:
        cantidad_desaprobados += 1

promedio = suma_notas / len(alumnos)

def printMatriz(matriz):
    if matriz != []:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=",")
            print()
    else:
        print(matriz)
        
printMatriz(alumnos)

# Alumnos que superan el promedio
legajos_superiores = [alumno[0] for alumno in alumnos if alumno[1] > promedio]




# Ordenamiento de legajos y calificaciones
matriz_ordenada = sorted(alumnos, key=lambda x: x[0])

# Resultados
print("Cantidad de alumnos que aprobaron:", cantidad_aprobados)
print("Cantidad de alumnos que desaprobaron:", cantidad_desaprobados)
print("Promedio de notas:", promedio)
print("Legajos que superan el promedio:", legajos_superiores)

print("Listado de legajos y calificaciones:")
for alumno in matriz_ordenada:
    print("Legajo:", alumno[0], "- Nota:", alumno[1])
