'''
Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número -1. 
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
Descartar valores que no representan una edad válida. (Se considera válida una edad entre 0 y 100).
'''

num = int(input("Ingrese su edad y la de cada uno de sus amigos. Ingrese -1 para finalizar: "))

counterMajors = 0
counterMinors = 0
majors = 0
minors = 0

while num != -1: 
	if num < 100 and num > 0:
		if(num >= 18):
			majors += num		
			counterMajors += 1	
		else:
			minors += num
			counterMinors +=1
	num = int(input("Ingrese su edad y la de cada uno de sus amigos. Ingrese -1 para finalizar: "))

promMajors	= majors / counterMajors
promMinors = minors / counterMinors

print("Cantidad de mayores de 18 años:", counterMajors, "Promedio de edad:", promMajors, "\n",
    "Cantidad de menores de 18 años:", counterMinors, "Promedio de edad:", promMinors ) 