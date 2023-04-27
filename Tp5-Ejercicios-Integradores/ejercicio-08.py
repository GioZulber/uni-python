'''
Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3). Por cada empleado se lee su legajo, categoría y salario. 
Se solicita elaborar un informe que contenga:
 	Importe total de salarios pagados por la empresa.
	Cantidad de empleados que ganan más de $200000.
	Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
	Legajo del empleado que más gana.
	Sueldo más bajo.
	Importe total de sueldos por cada categoría.
	Salario promedio
'''

legajo = int(input("Ingrese su número de legajo:"))
category = int(input("Ingrese su categoria(1, 2 o 3):"))
salary = int(input("Ingrese su salario: ")) 

totalEmployees = 0
employeesOverTwoHundred = 0
employeesLessFifty = 0

totalCategotyOne = 0
totalCategotyTwo = 0
totalCategotyThree = 0

legajoUpperSalary = legajo
upperSalary = salary
lowerSalary = salary
totalSalarys = 0

while legajo != -1: 
 
	if salary < lowerSalary: 
		lowerSalary = salary
	elif salary > upperSalary:
		legajoUpperSalary = legajo
		upperSalary = salary
	
	if salary > 200000:
		employeesOverTwoHundred += 1
		totalCategotyOne += salary
	elif salary < 50000: 
		employeesLessFifty += 1
		totalCategotyThree += salary
	else: 
		totalCategotyTwo += salary
	
	totalSalarys += salary 
	totalEmployees += 1	
	promSalary = totalSalarys / totalEmployees 
	
	legajo = int(input("Ingrese su número de legajo:"))
	category = int(input("Ingrese su categoria(1, 2 o 3):"))
	salary = int(input("Ingrese su salario: ")) 



print("--------- INFORME ---------")
print("Importe total de salarios pagados por la empresa:", totalSalarys)
print("Cantidad de empleados que ganan más de $200000:", employeesOverTwoHundred)
print("Cantidad de empleados que ganan menos de $50000:", employeesLessFifty)
print("Legajo del empleado con el sueldo mas alto:", legajoUpperSalary)
print("Salario mas bajo:", lowerSalary)
print("Imprte de sueldo categoria 1:", totalCategotyOne )
print("Imprte de sueldo categoria 2:", totalCategotyTwo )
print("Imprte de sueldo categoria 3:", totalCategotyThree )
print("Salario promedio:", promSalary)
print("--------- INFORME ---------")