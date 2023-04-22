'''
El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X <= N. 
Desarrollar un programa para calcular el factorial de un número dado. Deberán rechazarse las entradas inválidas (menores que 0).
'''

num = int(input("Ingrese un número: "))

counter = 1
factorial = 1

while num > 0 and counter <= num: 
    factorial *= counter
    counter += 1
print("----------------------------------------------------")
print("Obtuvimos el siguiente resultado:", factorial)
print("----------------------------------------------------")