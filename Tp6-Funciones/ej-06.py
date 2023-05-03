'''
Escribir la función comparar(a, b) que reciba como parámetros dos números enteros y 
devuelva 1 si el primero es mayor que el segundo, 
0 si son iguales o -1 si el primero es menor que el segundo. 
En este ejercicio debe aprovecharse la fun-ción del ejercicio anterior. 
Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) devuelve -1.
'''
def compare(num1, num2):
    if(num1 > num2):
        print(1)
    elif(num1 < num2):
        print(-1)
    else:
        print(0)
compare(10, 5)