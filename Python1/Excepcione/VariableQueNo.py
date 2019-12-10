'''
Created on 28 nov. 2019

@author: Javier Fernández 
'''
def operacion():
    var2 = 10
    try:
        valor = 8 + var2/5 + 10
    except NameError:
        print("Has usado una variable que no inexitente ", valor)
    else:
        print("El resultado es: ",valor)
    finally:
        print("Fin loco")
operacion()
