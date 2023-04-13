"""
Ejercicio 10:Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.
"""

# Omgresamos los segundos
ingresado=int(input("Ingrese la cantidad de segundos: "))


# Declaramos las variables con sus respectivos datos
dias= 86400
horas= 3600
minutos= 60

# Obtenemos los dias
res_dias = ingresado // dias
# Obtenemos el resto de la division anterior 
dias_resto = ingresado % dias
# Obtenemos las horas
res_horas = dias_resto // horas
# Obtenemos el resto de la division anterior 
horas_resto = dias_resto % horas
# Obtenemos los minutos 
res_minutos = horas_resto // minutos
#Obtenemos los segundos
res_segundos = horas_resto % minutos


print(ingresado, "segundos equivalen a", res_dias, "días", res_horas,"horas", res_minutos, "minutos y ", res_segundos, "segundos")