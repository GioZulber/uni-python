"""
Ejercicio 8:Leer una medida en metros e imprimir esta medida expresada en centí-metros, pulgadas, pies y yardas.
"""
medida=int(input("Ingrese una medida en metros: "))

m = 100 #cm
p = 2.54 #cm
pie = 12 #pulgadas
y = 3 #pies


centimetros = medida * m 
pulgada = centimetros / p
res_pie = pulgada / pie
yarda = res_pie / y

print("Ingresó", medida ,"metro/s", "\n",
	  "Centrimetros:", centimetros,"\n",
      "Pulgadas:",  pulgada,"\n",
      "Pies:",  res_pie, "\n",
      "Yardas:", yarda,"\n",
    )


