"""
Ejercicio 9:Una inmobiliaria paga a sus vendedores un salario de $50000, más una comisión de $5000 por cada venta realizada, más el 5% del valor de las ventas. Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas. 
"""
vendedor=input("Ingrese el numero de vendedor:")
num_ventas=int(input("Ingrese el numero de ventas realizadas:"))
valor_total_ventas=int(input("Ingrese el valor total de las ventas:")) 

salario= 50000
comision_por_venta= 5000

comision= (comision_por_venta * num_ventas) + (valor_total_ventas * 0.05)

salario_final= comision + salario

print("El salario final del vendedor", vendedor, "es: $", salario_final)
