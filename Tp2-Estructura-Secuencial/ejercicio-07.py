"""
Ejercicio 7:Una persona invierte su capital en un banco y desea saber cuánto dinero ganará en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará en seis meses si deja su dinero invertido?
"""
inversion=int(input("Ingrese la cantidad a invertir: "))

mes_1 = inversion * 0.02
mes_2 = (inversion + mes_1) * 0.02
mes_3 =(inversion + mes_2) * 0.02
mes_4 = (inversion + mes_3) * 0.02
mes_5 = (inversion + mes_4) * 0.02
mes_6 = (inversion + mes_5) * 0.02

total= inversion + mes_6

print( "Inversion inicial:", inversion, "\n" 
      "Ganancia el primer mes:",  mes_1, "\n",
      "Ganancia en 6 meses:",  mes_6, "\n",   
      "Total: $",total   
	  )