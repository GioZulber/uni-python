'''

# En Python las variables locales son las que se definen en una función y que solo permiten su acceso desde ella. 
Las globales se definen en el cuerpo principal del programa y permiten su acceso desde cualquier lugar.

'''

a = 10 # VARIABLE GLOBAL 

def sumarDos(a):
    b = 2 # VARIABLE LOCAL
    print("Hola soy Lucasbra y tengo el pito re chico como luca negro sucio") # Soy Ian 
    return a + b

# print(b) # error -> 'b' is not defined

print(sumarDos(a))