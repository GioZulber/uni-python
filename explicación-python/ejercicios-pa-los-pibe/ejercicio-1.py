'''

Choperton Marchetti es un alumno de la UADE, que necesita un programa para saber cuantos minutos le tomara llegar a la facultad.
Nos informo que normalmente tarda 1.800 segundos en llegar.
    # El tiempo que tarde dependera de la cantidad de autos:
        * Si la cantidad de autos es mayor o igual a 10.000 tardara en llegar 900 segundos mas.
        * Si la cantidad de autos es menor o igual a 2.500 tardara en llegar 600 segundos menos.
        * También se debe tomar en cuenta si hay accidentes en la autopista, por cada accidente tardara 900 segundos mas en llegar.
    
    -> Realizar un programa que reciba por parametro lo especificado y calcular cuantos minutos le tomara llegar a la UADE.

'''

def getTimeToArrive(cars, accidents):
    time = 1800 # Tiempo promedio

    if cars >= 10000: # 10.000 autos 900 segundos mas
        time = time + 900
    elif cars <= 2500: # 2.500 autos 600 segundos menos
        time = time - 600

    time = time + 900 * accidents # Por cada accidente tardara 900 segundos mas
    time = time / 60 # Dividimos tiempo entre 60 porque necesitamos los minutos

    return time

print("Chopertorn tardara en llegar a la UADE", getTimeToArrive(10000, 2), "minutos")