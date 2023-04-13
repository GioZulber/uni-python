"""
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 
El costo básico del libro es de $500, más $3,20 por página con encuadernación rústica. 
Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $200. 
Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-cuadernación que incrementa el costo en otros $336. 
Desarrollar un programa que calcule el costo de un libro dado el número de páginas.
"""

costo_basico= 500
costo_por_pag= 3.20
tela= 200
encuadernacion_esp = 336

cantidad_de_pag= int(input("Ingrese la cantidad de paginas que contiene el libro para determinar el precio: "))

if (cantidad_de_pag > 300 and cantidad_de_pag <=600) :
	precio_final =  (cantidad_de_pag * 3.20) + costo_basico + tela
	print(precio_final)
elif (cantidad_de_pag > 600) : 
	precio_final = (cantidad_de_pag * 3.20) + costo_basico + encuadernacion_esp + tela 
	print(precio_final)
else : 
	precio_final = (cantidad_de_pag * 3.20) + costo_basico
	print(precio_final)

