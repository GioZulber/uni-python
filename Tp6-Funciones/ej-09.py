"""
Escribir una función que reciba como parámetros un número de día,
un número de mes y un número de año y devuelva la cantidad de días que faltan hasta fin de mes.
Luego desarrollar tres programas para: 
	Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días que faltan hasta fin de año.
 	Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días transcurridos en ese año hasta esa fecha.
 	Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuánto tiempo transcurrió entre ambas, expresando el resultado en años, meses y días.
Los tres programas deben realizar su trabajo a través de la función indicada al comienzo.
"""


def daysLeft(day, month, year):
    if month >= 1 and month <= 12:
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                monthDays = 29
            else:
                monthDays = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            monthDays = 30
        else:
            monthDays = 31
        return monthDays - day
    else:
        print("ERROR! Fecha invalida")


# daysIn = int(input("Ingrese el día: "))
# monthIn = int(input("Ingrese el mes: "))
# yearIn= int(input("Ingrese el año: "))
daysIn = 3
monthIn = 5
yearIn = 2023

totalDays = daysLeft(daysIn, monthIn, yearIn)


def daysLeftToEndYear(month, year, totalDays):
    month += 1
    while month <= 12:
        totalDays += daysLeft(0, month, year)
        month += 1
    # print("Faltan", totalDays, "días para fin de año.")
    return totalDays


# daysLeftToEndYear(monthIn,yearIn, totalDays)
def daysOntheYear(month, year, totalDays):
    month += 1
    while month <= 12:
        totalDays += daysLeft(0, month, year)
        month += 1
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        totalDaysInTheYear = 366
    else:
        totalDaysInTheYear = 365
    daysOfTheYear = totalDaysInTheYear - totalDays
    # print("Total de dias transcurridos en el año contando hoy:", daysOfTheYear)
    return daysOfTheYear


# daysOntheYear(monthIn, yearIn,totalDays)


# daysInTwo = int(input("Ingrese el día: "))
# monthInTwo = int(input("Ingrese el mes: "))
# yearInTwo= int(input("Ingrese el año: "))

daysInTwo = 1
monthInTwo = 5
yearInTwo = 2024


def datesDifference(day1, month1, year1, day2, month2, year2):
    totalDaysDate1 = daysOntheYear(month1, year1, totalDays) + daysLeftToEndYear(
        month1, year1, totalDays
    )
    totalDaysDate2 = daysOntheYear(month2, year2, totalDays) + daysLeftToEndYear(
        month2, year2, totalDays
    )
    # if year1 == year2:
    #     year = 0
    #     if month1 == month2:
    #         month = 0
    #         if day1 < day2:
    #             day = day2 - day1
    #         elif day1 > day2:
    #             day = day1 - day2
    # if year1 < year2:
    #     year = year2 - year1
    #     day = day2 - day1
    #     month = month1
    #     print(year)

    print(
        "La diferencia entre las fechas",
        day1,
        "/",
        month1,
        "/",
        year1,
        "y",
        day2,
        "/",
        month2,
        "/",
        year2,
    )
    print("Es de", day, "dias", month, "meses", "y", year, "años")
    # print(day)
    # elif(day1 > day2):


diff = datesDifference(daysIn, monthIn, yearIn, daysInTwo, monthInTwo, yearInTwo)
