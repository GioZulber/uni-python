"""
Ejercicio 12:Escribir un programa para convertir un número binario de 4 cifras en un número decimal. El número binario se ingresa como un solo número entero de cuatro dígitos.Procedimiento: Para convertir un número binario a decimal es necesario multiplicar el valor de cada dígito por el número 2 elevado a un expo-nente. Este exponente se obtiene de la posición que ocupa el dígito dentro del número, comenzando desde la derecha con la posición 0. To-dos estos resultados se suman para obtener el valor final. Ejemplo: 
Convertir 1011 a decimal:
13 02 11 10 = 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 11
"""

numero=int(input("Ingrese un numero binario de cuatro digitos: "))

cuarto_digito = numero % 10
numero_restante= numero // 10
tercero_digito = numero_restante % 10
numero_restante = numero_restante // 10
segundo_digito = numero_restante % 10

primer_digito = numero_restante // 10

numero_binario = (primer_digito * 2**3) + (segundo_digito * 2**2) + (tercero_digito * 2**1) + (cuarto_digito * 2**0)



print(primer_digito, segundo_digito,tercero_digito, cuarto_digito )

print("Numero decimal: ",numero_binario)