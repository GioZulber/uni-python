'''

Realizar un programa que reciba por input numeros positivos, si recibe numeros negativos o un 0 debe solicitar otro número.

'''


'''
# -> WHILE

def inputValue():
    num = int(input("[ SISTEMA ] Ingrese un número : "))
    while num <= 0:
        num = int(input("[ SISTEMA ] Ingrese un número : "))
    return num
'''

# -> RECURSIVIDAD

def inputValue():
    num = int(input("[ SISTEMA ] Ingrese un número : "))
    if num <= 0:
       num = inputValue()
    return num

num = inputValue()

print(num)
