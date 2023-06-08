def busquedabinaria(lista, dato):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos


def metodoSeleccion(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


"Copia de listas"
lista1 = [1, 2, 3]
lista2 = []
for i in range(len(lista1)):
    lista2.append(lista1[i])
