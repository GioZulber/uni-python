'''
Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número entero N que representa una cantidad de días. 
Realizar un programa que imprima la nueva fecha que resulta de sumar N días a la fecha dada.
Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3.
'''

day = int(input("Ingrese un día: "))
month = int(input("Ingrese un mes: "))
year = int(input("Ingrese un año: "))

daysIn = int(input("Ingrese una cantidad de días a sumar: "))

while daysIn > 0:
    
	monthDays = 31
 
	if(month >= 1 and month <= 12) and ( day >= 1 and day <= 31):
		if month == 2:
			if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
				monthDays = 29
			else:
				monthDays = 28
		elif month == 4 or month == 6 or month == 9 or  month == 11 :
			monthDays = 30
		
		day += 1
	
		if day > monthDays:
			day = 1
			month += 1
			if 	month > 12:
				month = 1
				year += 1
    
		daysIn -= 1
	else: 
		print("¡ERROR! Ingreso mal los datos.")
		daysIn = 0

print(day,"/",month,"/",year)