'''

# Pochito Tegli es un hincha más de Independiente que esta desesperado por recaudar fondos para salvar a su club.
Nos pidio un programa para que la gente que quiera aporte.
    # Se debe ingresar una cantidad en bucle de plata en pesos (cambio dolar a 47).
    # Nos llevamos un 15% de cada donación.
    # Tener en cuenta que cada 5 transacciones la dirigencia del club se roba un 45% de la recaucación total hasta ese momento.
    # El bucle terminara cuando la cantidad de plata recaudada alcance el millon de dolares.

    -> Informar:
        # Con cuanta plata nos quedamos nosotros en total
        # Cuanto se robo la dirigencia en cada aportación


'''

def collection():
    counter = 0
    money = 0
    systemMoney = 0

    while money >= 0 and money / 47 <= 1000000:
        moneyInput = int(input("[ SISTEMA ] Ingrese la cantidad de dinero a aportar : "))

        money = money + moneyInput * 0.85
        systemMoney = systemMoney + moneyInput * 0.15
        counter = counter + 1

        if counter == 5:
            leadershipRobbery = money * 0.45
            money = money - leadershipRobbery
            print("[ SISTEMA ] La dirigencia se robo:", leadershipRobbery * 0.45, "$ | Quedan: ", money, "$")
            counter = 0
    
    return money, systemMoney

(money, systemMoney) = collection()

print("[ SISTEMA ] La recaudación total fue de: ", money, "$ | Nuestra ganancia: ", systemMoney, "$")