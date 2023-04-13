"""
Ejercicio 11:Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero e imprima a cuántos billetes equivale, conside-rando que existen billetes de $1000, $500, $100, $50, $10, $5 y $1. Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
"""

cantidad = int(input("Ingrese una cantidad de dinero: "))

mil = cantidad // 1000
resto = cantidad % 1000
quinientos = resto // 500
resto = resto % 500
cien = resto // 100
resto = resto % 100
cincuenta = resto // 50
resto = resto % 50
diez = resto // 10 
resto = resto % 10
cinco = resto // 5
resto = resto % 5 


print("Imprimiendo...", "\n" , mil,"de 1000$", quinientos, "de 500$", "\n"  , cien ,"de 100$", cincuenta ,"de 50$", "\n" , diez, "de 10$", cinco, "de 5$", "\n",  resto, "de 1$")
