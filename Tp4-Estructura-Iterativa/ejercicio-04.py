'''
Desarrollar un programa que imprima la suma de los números impares comprendidos entre 42 y 176.
'''

num1 = 42
num2 = 176
counter = 0

while num1 < num2:
    num1  += 1
    if(num1 % 2 != 0):
        counter += num1
print("La suma total de los números impares es:", counter) 
    