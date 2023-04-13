"""
Ejercicio 4:Escribir un programa que permita
ingresar la edad de una persona en años y la convierta a días, 
imprimiendo el resultado. 
Considerar que to-dos los años tienen 365 días.
"""

edad_ingresada=int(input("Ingrese su edad: "))


#Ponemos los dias que tiene un año
año= 365

total_de_dias= edad_ingresada * año

print("Su edad es igual a:", total_de_dias, "dias")