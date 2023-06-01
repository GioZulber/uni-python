"""

# Realizar un programa que determine si un numero es divisible por 11

"""


def digitsArePair(num):
    countDigits = 0
    while num > 0:
        num = num // 10
        countDigits = countDigits + 1

    if countDigits % 2 == 0:
        return True
    else:
        return False


def divisibleOnce(num):
    if digitsArePair(num):
        fTerm = 0
        sTerm = 0
        index = 1
        while num > 0:
            digit = num % 10
            num = num // 10
            if index % 2 == 0:
                sTerm = sTerm + digit
            else:
                fTerm = fTerm + digit

            index = index + 1

        if fTerm == sTerm:
            return True
        else:
            return False


print(divisibleOnce(5841))
