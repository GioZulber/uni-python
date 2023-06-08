"""

# En Python, una definición de función tiene las siguientes características:

1 - La palabra clave def
2 - Un nombre de función
3 - Paréntesis ’()’, y dentro de los paréntesis los parámetros de entrada, aunque los parámetros de entrada sean opcionales.
4 - Algún bloque de código para ejecutar
5 - Una sentencia de retorno (opcional)

"""


# Función sin parámetros o retorno de valores (solo muestra un mensaje en la consola)
def decirHola():
    # El código que se encuentra dentro de la función se ejecuta cuando la función es llamada.
    print("Hola!")

# Si no llamamos a la función, el código que se encuentra dentro de la función no se ejecuta.
decirHola()  # Llamada a la función, 'Hola!' se muestra en la consola


# Función con un parámetro
def holaConNombre(name):
    print("Hola ", name, "!")


# Si la función recibe un parámetro, cuando la llamamos tenemos que pasarle un valor para ese parámetro, en este caso  "Delfi".
# Si no le pasamos un valor, la función no se ejecuta y nos muestra un error ya que no sabe que hacer con el parámetro que le falta.
holaConNombre("Delfi")  # Llamada a la función, 'Hola Delfi!' se muestra en la consola


# Función con múltiples parámetros con una sentencia de retorno
"""
Tenes que pensar que la funcion es como una caja, que puede recibir cosas o no, como tambien puede devolver cosas o no, o ambas.
La funcion nunca va a devolver nada al programa principal si no le decimos explicitamente que lo haga con la sentencia return.
En este caso, la funcion recibe dos parametros, los multiplica y devuelve el resultado.
"""
def multiplica(a, b):
    # Si no colocamos la sentencia return, la funcion no devuelve nada al programa principal.
    return a * b


# Dentro del print estamos llamando a la funcion multiplica, y le estamos pasando dos parametros, 3 y 5.
print(multiplica(3, 5))  # Muestra el resultado de la multiplicacion de 3 y 5, que es 15. Si no ponemos el print, no se muestra nada.
# Si no ponemos el print, la funcion multiplica se ejecuta igual, pero no muestra nada en la consola.


# Función con múltiples parámetros con doble retorno
def mulYdiv(a, b):
    # En este caso la funcion devuelve dos valores, el resultado de la multiplicacion y el resultado de la division.
    # Para devolver dos valores, los separamos con una coma.
    return a * b, a / b


# De esta manera podemos guardar los dos valores que devuelve la funcion en dos variables distintas.
# Respetando el orden en que se devuelven los valores, el primer valor se guarda en la variable multiplicacion y el segundo en la variable division.
(multiplicacion, division) = mulYdiv(4, 2)

print(multiplicacion)  # Muestra el resultado de la multiplicacion de 4 y 2, que es 8.
print(division)  # Muestra el resultado de la division de 4 y 2, que es 2.0.

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