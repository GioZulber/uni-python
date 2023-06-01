'''

# Al iniciar el programa debe aparecer un menu con las opciones de operaciones simples matematicas (suma, resta, multiplicacion y division)
El usuario debe seleccionar una operación y que se ejecute.

-> Ejemplo: 


********************************************************************************
***************************** OPERACIONES BASICAS ******************************
********************************************************************************

=[=-*-=]= [ 1 - suma | 2 - resta | 3 - multiplicación | 4 - division ] =[=-*-=]=

-> Acción : 1

| * | Ingresa un número : 9
| * | Ingresa un otro número : 12

[ OPERACIONES ] El resultado de la operacion entre 9 y 12 es : 21

'''

def getAction():
    print("********************************************************************************")
    print("***************************** OPERACIONES BASICAS ******************************")
    print("********************************************************************************")
    print("\n=[=-*-=]= [ 1 - suma | 2 - resta | 3 - multiplicación | 4 - division ] =[=-*-=]=")
    return int(input("\n-> Acción : "))

def executeAction(action):
    num1 = int(input("\n| * | Ingresa un número : "))
    num2 = int(input("| * | Ingresa otro número : "))

    if action == 1:
        result = num1 + num2
    elif action == 2:
        result = num1 - num2
    elif action == 3:
        result = num1 * num2
    elif action == 4:
        result = num1 / num2
    
    return result

action = getAction()

result = executeAction(action)

print("\n[ OPERACIONES ] El resultado de la operacion fue :", result)
