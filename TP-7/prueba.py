import random
def search(array, num):
    found = False
    for i in range(len(array)):
        if array[i] == num:
            aux = array[i]
            for j in range(i, 0, -1):
                array[j] = array[j - 1]
            array[0] = aux
            found = True
            break  # Se agrega un break para salir del bucle una vez se encuentre el número
    return found, array


def negative(num):
    if num > 0:
        return num
    else:
        return -num


def digitSum(num):
    num = negative(num)
    suma = 0
    while num > 0:
        digit = num % 10
        suma = suma + digit
        num = num // 10
    return suma


def searchedNumbers(values):
    disorder = True
    contador = 0  # Se corrige el nombre de la variable a 'contador'
    while disorder:
        disorder = False
        for i in range(len(values) - 1):
            contador = contador + 1
            print("itera", contador)
            if digitSum(values[i]) > digitSum(values[i + 1]):  # Se corrige el segundo argumento de digitSum
                print("entra PRIMER IF")
                aux = values[i]
                values[i] = values[i + 1]
                values[i + 1] = aux
                disorder = True
            elif digitSum(values[i]) == digitSum(values[i + 1]):  # Se corrige el segundo argumento de digitSum
                print("entra al ELIF")
                if values[i] > values[i + 1]:
                    print("entra SEGUNDO IF DENTRO DEL ELIF")
                    aux = values[i]
                    values[i] = values[i + 1]
                    values[i + 1] = aux
                    disorder = True
    return values


def createList():
    array = []
    for _ in range(20):
        array.append(random.randint(-100, 100))
    return array


array = createList()

num = int(input("Ingrese un numero a buscar: (-1 para terminar) "))

finalList = []

while num != -1:
    found, array = search(array, num)
    print("El numero", num, "se encuentra en la lista?", found)
    print("Lista reorganizable", array)
    finalList.append(num)
    num = int(input("Ingrese un numero a buscar: (-1 para terminar) "))

values = searchedNumbers(finalList)
print("Lista de valores buscados:", values)