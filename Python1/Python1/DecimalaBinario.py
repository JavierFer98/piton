'''
Created on 19 nov. 2019

'''
def transformar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(transformar(numero))
