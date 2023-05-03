'''
Extraer un dígito de un número. 
La función recibe como parámetros dos números enteros, 
uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener.
La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. 
Tener en cuenta que el número puede ser positivo o negativo. 
Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
'''

def extractDigit(num, index): 
    i = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        if index == i:
            return digit
        else: 
            i = i + 1
    return -1

print(extractDigit(12345, 10))