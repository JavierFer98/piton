'''
Created on 19 nov. 2019

'''
def muestraInfo(arg1, *valores):
    print("La salida es: ")
    print(arg1)
    for val in valores:
        print(val)
    return
muestraInfo(100)
muestraInfo(90, 48, 36, 78)