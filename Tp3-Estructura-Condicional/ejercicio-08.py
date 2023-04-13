'''
Ejercicio 8:
Leer tres números correspondientes al día, mes y año de una fecha e imprimir un mensaje 
indicando si la fecha es válida o no.
'''

days = int(input('Ingrese el número dia de la fecha que quiera:'))
month = int(input('Ingrese el número de mes que quiera:'))
year = int(input('Ingrese el número de año que quiera:'))

if ((days > 31 and month > 12 and year < 0) or (month == 2 and days <= 28) or (month % 2 == 0 and month != 2 and  days > 30)) :  
    print('La fecha ingresada es valida {}/{}/{}'.format(days, month, year))     
else: 
    print('La fecha ingresada es invalida: {}/{}/{}'.format(days, month, year))
 