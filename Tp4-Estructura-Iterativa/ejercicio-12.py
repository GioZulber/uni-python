"""
La sucesión de Fibonacci es una sucesión de números enteros 
donde cada término se obtiene como suma de los dos anteriores, 
siendo los dos primeros 0 y 1. Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... 
Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, 
como así también la suma de los mismos.
"""

num = int(input("Sucesion de Fibonacci - Ingrese un número: "))

firstNum = 0
lastNum = 1
counter = 0
while counter < num:
    print("Fibonacci", firstNum)
    acum = firstNum
    firstNum = lastNum
    lastNum = firstNum + acum
    counter += 1
