"""
Ejercicio 6: 
Una remisería requiere un programa que calcule el precio de un viaje a partir de la cantidad de kilómetros que desea recorrer el usuario. 
Para eso cuenta con la siguiente tarifa:∑Viaje mínimo $250. 
Sólo se cobra cuando el importe por kilómetro no alcanza este mínimo. 
Si recorre entre 0 y 10 km: $30 por km∑Si recorre 10 km o más: $20 por km
"""

km = int(input("Ingrese la cantidad de kilometros que desea recorrer: "))
min = 250
price1 = km * 30
price2 = km * 20
if price1 > min and price2 > min:
    if km >= 0 and km < 10:
        print("El precio es:", price1)
    elif km >= 10:
        print("El precio es:", price2)
else:
    print("El precio es:", min)
