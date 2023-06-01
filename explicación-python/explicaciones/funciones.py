'''

# En Python, una definición de función tiene las siguientes características:

1 - La palabra clave def
2 - Un nombre de función
3 - Paréntesis ’()’, y dentro de los paréntesis los parámetros de entrada, aunque los parámetros de entrada sean opcionales.
4 - Dos puntos ’:’
5 - Algún bloque de código para ejecutar
6 - Una sentencia de retorno (opcional)

'''

# función sin parámetros o retorno de valores
def decirHola():
  print("Hola!")

decirHola()  # llamada a la función, 'Hola!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
  print("Hola " + name + "!")

holaConNombre("Mansete")  # llamada a la función, 'Hola Mansete!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(a, b):
  return a * b

print(multiplica(3, 5))  # muestra 15 en la consola

# función con múltiples parámetros con doble retorno
def mulYdiv(a, b):
  return a * b, a / b

(multiplicacion, division) = mulYdiv(4, 2)

print(multiplicacion)
print(division)
