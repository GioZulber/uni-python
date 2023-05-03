'''
Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.
'''
def column(num):
    res = "*"
    counter = 0
    while counter < num:
        print(res)
        counter += 1

column(5)