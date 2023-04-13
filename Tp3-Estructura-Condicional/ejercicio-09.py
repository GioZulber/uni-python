'''
Ejercicio 9:
Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. 
Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad. 
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%.
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (1 si es soltero o 2 si es casado). 
Se debe informar: (reemplazar los 9 por los valores que correspondan)Estado Civil: Soltero/CasadoSueldo básico AntigüedadDescuentos 
Importe   $ 999.99  99 años + 999.99Jubilación   - 999,99Obra Social  - 999,99Sindicato   - 999,99------------Sueldo Neto     999,99
'''

base_salary= int(input("Ingrese su sueldo basico: "))
state= int(input("Ingrese 1 si esta soltero, ingrese 2 si se encuentra casado: "))
seniority= int(input("Ingrese su antiguedad de años en su trabajo: "))

retirement =  base_salary * (11 / 100)
syndicate_and_social =  base_salary * (3 / 100)

discount = retirement + (syndicate_and_social * 2) 

total = base_salary - discount

if state == 1: 
	total = total + ( base_salary * (seniority * 7 ) / 100 )
	print("Su sueldo total es: {}".format(total))
elif state == 2: 
	total = total + ( base_salary * (seniority * 5 ) / 100 )
	print("Su sueldo total es: {}".format(total))
else: 
	print("[ERROR]: INGRESO MAL UN DATO")