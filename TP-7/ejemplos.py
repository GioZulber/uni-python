def changeMethod(array):
    disorder = True
    while disorder:
        disorder = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                aux = array[i]
                array[i] = array[i + 1]
                array[i + 1] = aux
                disorder = True
    return array
print(changeMethod([9,6,32,4,1,3,7,8]))

def InsertMethod(array):
    for i in range(1, len(array)):
        aux = array[i]
        j = i
        while j > 0 and array[j - 1] > aux:
            array[j] = array[j - 1]
            j = j-1
        array[j ] = aux
    return array

print(InsertMethod([9,6,32,4,1,3,7,8]))

def changeMethod(legajos, notas):
    disorder = True
    while disorder:
        disorder = False
        for i in range(len(legajos) - 1):
            if notas[i] > notas[i + 1]:
                aux = notas[i]
                notas[i] = notas[i + 1]
                notas[i + 1] = aux
                aux = legajos[i]
                legajos[i] = legajos[i + 1]
                legajos[i + 1] = aux
                disorder = True
    return legajos, notas



listaNotas = []
listaLegajos = []

u = int(input("Legajo: (-1 para terminar) "))
while u != -1:
    nota = int(input("Nota: "))
    listaNotas.append(nota)
    listaLegajos.append(u)
    u = int(input("Legajo: (-1 para terminar) "))
changeMethod(listaLegajos,listaNotas)
print()
for i in range(len(listaLegajos)):
    print(listaLegajos[i], ":", listaNotas[i], sep="")
