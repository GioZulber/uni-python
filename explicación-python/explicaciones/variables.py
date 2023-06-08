'''

# En Python las variables locales son las que se definen en una función y que solo permiten su acceso desde ella. 
Las globales se definen en el cuerpo principal del programa y permiten su acceso desde cualquier lugar.

'''

a = 10 # VARIABLE GLOBAL 

def sumarDos(a):
    b = 2 # VARIABLE LOCAL
    return a + b

# Si hacemos print(b) nos da error -> 'b' is not defined, porque b es una variable local de la funcion sumarDos y no podemos acceder a ella desde afuera de la funcion.
print(sumarDos(a)) # Ejecutamos la funcion sumarDos y le pasamos como parametro la variable global a, que vale 10.