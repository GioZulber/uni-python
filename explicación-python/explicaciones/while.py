'''

# Se utilizan generalmente para ejecutar repetidamente un mismo bloque de código.
1 - Se evalúa la condición.
2 - Si la condición es verdadera, se ejecuta el cuerpo del bucle.
3 - La condición se evalúa de nuevo:
    - Si la condición se sigue cumpliendo, se repite este proceso.
    - Si la condición es falsa, el bucle termina.

'''

counter = 9
limit = 12

while counter <= limit:
    print(counter)
    counter = counter + 1