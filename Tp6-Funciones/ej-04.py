'''
Devolver True si el número entero recibido como primer parámetro es múltiplo del segundo, 
o False en caso contrario. 
Ejemplo: esmultiplo(40, 8) devuelve True y esmultiplo(50, 3) devuelve False.
'''
def isMultiplo(num, divider):
    if(num % divider == 0):
        print(True)
    else:
        print(False)
        
isMultiplo(50, 3)