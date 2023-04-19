'''
Se desea analizar cuántos autos circulan con patente con numeración par y cuántos con numeración impar en un día. 
Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9)  
hasta ingresar -1 e informe cuántos vehículos pasaron con numeración par y cuántos con numeración impar.
'''

patent = int(input("Ingrese un número de patente, ingrese -1 para finalazar el programa."))

evenPatents = 0
oddPatents = 0

while patent != -1: 
    patent = int(input("Ingrese un número de patente, ingrese -1 para finalazar el programa."))
    if patent % 2 == 0: 
        evenPatents += 1 
    else: 
        oddPatents += 1
 
print("Han pasado", evenPatents, "autos con patentes con numeración par.", "\n", 
	  "Han pasado", oddPatents, "autos con patentes con numeración impar.")