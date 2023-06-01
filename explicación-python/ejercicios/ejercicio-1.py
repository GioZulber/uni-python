'''

Realizar una funcion que imprima una columna de '*' teniendo en cuenta un largo y ancho introducidos por input.

-> Ejemplo: si se introduce / largo : 2 - ancho : 3 /

***
***

'''

def drawColumn(height, width):
    while height > 0:
        currentWidth = width
        row = ""
        while currentWidth > 0:
            row = row + "*"
            currentWidth = currentWidth - 1
        print(row)
        height = height - 1

drawColumn(4, 4)