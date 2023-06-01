def playerAnimation(isMoving): 
    while isMoving: # Si el valor de isMoving es VERDADERO se ejecuta el codigo dentro del bucle
        print("Ejecutar animación...") # Ejecutar animación del jugador

isMoving = False # Variable que almacena VERDADERO si el jugador se mueve y FALSO si no

playerAnimation(isMoving) # Invocamos a la funcion y le pasamos 'isMoving'

# isMoving es una bandera porque funciona como un interruptor de encendido y apagado
