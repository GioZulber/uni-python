'''

Luca Valente es un negro que necesita realizarse un tratamiento de blanquiamianto. 
Cada 10% de blanqueamiento necesita los siguientes ingredientes: 1.5kg de FE, 0.5kg de ESPERANZA y 2.5kg de SUERTE
    # El programa pide el ingreso de la cantidad de ingredientes y determina que % del blanqueamiento se puede lograr.
    # Si sobra se debe mostrar la cantidad sobrante de cada ingrediente.
    # Si no se llega al 100% se debe mostrar la cantidad faltante de cada ingrediente.

'''

def getProgress(faith, hope, luck):
    progress = 0

    if (faith >= 1.5 and hope >= 0.5 and luck >= 0.5) and progress != 100:
        while faith > 0 and hope > 0 and luck > 0:
            faith = faith - 1.5
            hope = hope - 0.5
            luck = luck - 2.5
            progress = progress + 10

    return progress, faith, hope, luck

def getMissing(faith, hope, luck):
    FULL_FAITH = 15
    FULL_HOPE = 5
    FULL_LUCK = 25

    missingFaith = FULL_FAITH - faith
    missingHope = FULL_HOPE - hope
    missingLuck = FULL_LUCK - luck

    return missingFaith, missingHope, missingLuck


faith = float(input("[ SISTEMA ] Introduzca la cantidad de FE : "))
hope = float(input("[ SISTEMA ] Introduzca la cantidad de ESPERANZA : "))
luck = float(input("[ SISTEMA ] Introduzca la cantidad de SUERTE : "))

(progress, excessFaith, excessHope, excessLuck) = getProgress(faith, hope, luck)

print("\n[ SISTEMA ] Se alcanzo un", progress, "'%' de blanqueamiento")

if excessFaith > 0 or excessHope > 0 or excessLuck > 0:
    print("[ SISTEMA ] Sobrante : FE -", excessFaith, "KG | ESPERANZA -", excessHope, "KG | SUERTE -", excessLuck, "KG")

if progress != 100:
    (missingFaith, missingHope, missingLuck) = getMissing(faith, hope, luck)

    print("[ SISTEMA ] Faltante : FE -", missingFaith, "KG | ESPERANZA -", missingHope, "KG | SUERTE -", missingLuck, "KG")