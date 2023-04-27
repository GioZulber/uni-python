'''
Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene. 
Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa 12345 se debe imprimir 5.
'''

num = int(input("Ingrese un núnmero entero: "))

digits = 0

if(num == 0):
    digits = 1
else:
    while num != 0:
        if num < 0:
            num = num * -1
        num = num // 10	
        digits += 1	
    
print("El número ingresado tiene", digits, "digitos.")
	
	