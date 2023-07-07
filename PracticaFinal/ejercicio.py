import random
"""
def invertNumber(num):
    number = modulo(num)
    invert = 0
    while number > 0:
        invert = (invert * 10) + (number % 10)
        number = number // 10
    
    return invert

def modulo(num):
    if num < 0:
        num = num * -1
    return num

def main():
    num = int(input("Ingrese un numero: "))
    print(invertNumber(num))

main()
"""

def createArray():
    array = []
    for i in range(30):
        array.append(random.randint(0, 100))
    return array

def orderArray(array):