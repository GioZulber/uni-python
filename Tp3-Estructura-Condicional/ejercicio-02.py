"""
Leer un número entero e imprimir un mensaje indicando si es par o impar.
"""

number = int(input("Ingrese un número: "))

if(number % 2 == 0) : 
    print(number, "es un número par.")
else: 
    print(number, "es un número inpar.")
    