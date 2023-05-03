'''
Obtener el dígito central de un número entero pasado como parámetro, 
sólo si la cantidad de dígitos es impar. Si la longitud fuera par devolver -1. 
Ejemplo: digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.
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

def extractCentralDigit(num):
    qDigitsNum = num
    qDigits = 0

    while qDigitsNum > 0:
        qDigitsNum = qDigitsNum // 10
        qDigits = qDigits + 1
    
    if qDigits % 2 != 0:
        return extractDigit(num, qDigits // 2)
    else: 
        return -1

print(extractCentralDigit(123456789))