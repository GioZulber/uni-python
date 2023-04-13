"""
Ejercicio 5:Tres personas invierten dinero para fundar una empresa (no necesaria-mente en partes iguales). Calcular qué porcentaje invirtió cada una.
"""
inversor1=int(input("Ingrese la cantidad que quiera invertir, persona 1: "))
inversor2=int(input("Ingrese la cantidad que quiera invertir, persona 2: "))
inversor3=int(input("Ingrese la cantidad que quiera invertir, persona 3: "))

total_invertido= inversor1 + inversor2 + inversor3

porcentaje_1 = (inversor1 / total_invertido ) * 100
porcentaje_2 = (inversor2 / total_invertido) * 100
porcentaje_3 = (inversor3 / total_invertido) * 100

print("En un total de:", total_invertido, "\n",
      "El inversor uno puso un: %",porcentaje_1, "\n",
      "El inversor dos puso un: %",porcentaje_2, "\n",
	  "El inversor tres puso un: %",porcentaje_3, "\n",
	)





