'''
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
	Aplica el precio base a la primera docena de unidades.
	Aplica un 10% de descuento a todas las unidades entre 13 y 100.
	Aplica un 25% de descuento a todas las unidades por encima de las 100.Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
El cálculo resultante sería:100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04
'''

'''
Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. 
El fin de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar: 
	Cantidad de ventas realizadas total.
	Cantidad de ventas en las que se aplicó un 10% de descuento.
	Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.
'''

cantProduct=int(input("Ingrese la cantidad solicitada (-1 en cantidad para finalizar):"))
basePrice= int(input("Ingrese el precio base del producto:"))

totalSales = 0
salesWithoutDiscount = 0
salesFirstDiscount= 0

while cantProduct != -1: 
    
	firstDiscount = basePrice - (basePrice * 0.1)
	secondDiscount = basePrice - (basePrice * 0.25)
	
	if cantProduct <= 12 :
		finalPrice = basePrice * 12
		salesWithoutDiscount +=1
	elif cantProduct >= 13 and cantProduct <= 100:
		finalPrice = (basePrice * 12) + (firstDiscount * (cantProduct - 12))
		salesFirstDiscount +=1
	else:
		finalPrice = (basePrice * 12) + (firstDiscount * 88) + (secondDiscount * (cantProduct - 100)) 

	promPricePerUnit = finalPrice / cantProduct 
	print("Valor total de venta:", finalPrice, "Precio promedio por unidad:", promPricePerUnit)
	
	totalSales += 1 
 
	cantProduct=int(input("Ingrese la cantidad solicitada (-1 en cantidad para finalizar):"))
	basePrice= int(input("Ingrese el precio base del producto:"))

print("-----------------------------------------------------------------------------------------")
print(" Cantidad de ventas realizadas:", totalSales, "\n",
      "Cantidad de ventas en las que se aplico un 10% de descuento:", salesFirstDiscount, "\n",
      "Cantidad de ventas sin descuento:", salesWithoutDiscount)
print("-----------------------------------------------------------------------------------------")

