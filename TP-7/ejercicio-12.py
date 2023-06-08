"""
Dada una lista ordenada de números llamada A y un nuevo número N, 
desarrollar un programa que agregue el elemento N dentro de la lista A, 
respetando el ordenamiento existente. 
El programa deberá detectar automáticamente si el ordenamiento es ascendente 
o descendente antes de realizar la inserción. 
No se permite añadir el elemento al final y reordenar la lista. 
"""
orderList = [1, 2, 3, 4, 6, 7, 9, 10]
def insertInList (n):
    for i in range(len(orderList)):
        if orderList[i] > n:
            orderList.insert(i, n)
            break
    return orderList

print(insertInList(8))
print(insertInList(5))
