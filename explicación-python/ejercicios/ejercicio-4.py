'''

# Realizar una función que reciba un numero por parametro y retorne el mayor digito de este

-> Ejemplo: si recibe '12345678' retorna '8'

'''

def getHigherDigit(num):
    higherDigit = num % 10
    num = num // 10

    while num > 0:
        digit = num % 10
        num = num // 10

        if digit > higherDigit:
            higherDigit = digit
    
    return higherDigit


print(getHigherDigit(12345678))