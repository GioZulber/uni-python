'''
Desarrollar la función signo(n), 
que reciba un número entero y devuelva 1, -1 o 0 según el valor recibido sea positivo, 
negativo o nulo.
'''

def sign(num):
    if(num > 0):
        print(1)
    elif(num < 0):
        print(-1)
    else:
        print(0)
sign(5)