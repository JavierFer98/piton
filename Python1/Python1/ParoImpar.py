'''
Created on 19 nov. 2019

'''
numero = 0
while numero < 100:
    if numero == 100:
        break
    if numero % 2 == 0:
        print("El numero ", numero, " es PAR")
    else:
        print("El numero ", numero, " es IMPAR")
    numero = numero + 1
    continue
else:
    print("Se sale del bucle cuando el numero sea 100")
