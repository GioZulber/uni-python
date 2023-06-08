"""
Cargar dos listas de números A y B con N números al azar entre 1 y 100,
donde N se ingresa por teclado. 
Mostrar ambas listas por pantalla. Luego construir e imprimir tres nuevas listas C, D y E que contengan:
	La concatenación de los valores pares de A con los impares de B. 
	(valores pares o valores impares se refiere 
	a los elementos propiamente dichos y no a sus posiciones).
	La concatenación de los valores impares de A con el 
	reverso de los valores pares de B.
	La intercalación de los elementos de A y B.
"""

import random

def charge_list(n):
    first_list = []
    second_list = []
    for i in range(n):
        first_list.append(random.randint(1, 100))
        second_list.append(random.randint(1, 100))
    return first_list, second_list

n = int(input("Ingrese la cantidad de elementos de las listas: "))

first_list, second_list = charge_list(n)

print("LISTA A: ", first_list)
print("LISTA B: ", second_list)
print()

def concat_list (a, b):
    c = []
    d = []
    e = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            c.append(a[i])
        else:
            d.append(a[i])
    for i in range(len(b)):
        if b[i] % 2 != 0:
            c.append(b[i])
        else:
            d.append(b[len(b) - i - 1])
    for i in range(len(a) + len(b)):
        if i < len(a):
            e.append(a[i])
        if i < len(b):
            e.append(b[i])
       
            
    return c, d, e

c, d, e = concat_list(first_list, second_list)

print("Valores pares de A con los impares de B: ", c)
print("Valores impares de A con el reverso de los valores pares de B: ", d)
print("Intercalación de los elementos de A y B: ", e)

            

    
    
