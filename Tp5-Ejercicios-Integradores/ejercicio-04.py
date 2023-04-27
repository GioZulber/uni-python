'''
Una empresa factura a sus clientes el último día de cada mes. 
Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura, mientras que si paga después del día 20 deberá abonar una multa de $350 o del 10% de su factura, 
lo que resulte mayor. 
Escribir un programa que lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres importes que podría abonar según la fecha de pago.
'''

clientNumber = int(input("Ingrese su número de cliente:"))
invoiceTotal = int(input("Ingrese total de la factura:"))

firstTenDaysOpOne =	invoiceTotal - (invoiceTotal *0.02)
firstTenDaysOpTwo = invoiceTotal - 200

afterTwentyDaysOpOne = invoiceTotal + 350
afterTwentyDaysOpTwo = invoiceTotal + (invoiceTotal * 0.1)

if(firstTenDaysOpOne > firstTenDaysOpTwo and afterTwentyDaysOpOne > afterTwentyDaysOpTwo):
	firstTenDays = firstTenDaysOpTwo
	afterTwentyDays= afterTwentyDaysOpOne
else: 
    firstTenDays = firstTenDaysOpOne
    afterTwentyDays= afterTwentyDaysOpTwo
    

print("Numero de cliente:", clientNumber)
print("----------------------- INFORME -----------------------")
print("Si paga en los primeros 10 dias del mes:", firstTenDays, "\n",
      "Si paga en los siguientes 10 dias:", invoiceTotal, "\n",
      "Si paga despues del dia 29 de mes:", afterTwentyDays,
      	)

