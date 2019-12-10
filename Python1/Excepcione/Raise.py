'''
Created on 28 nov. 2019

@author: Javier Fernández 
'''
raise NameError("Hola DAM")
try:
    raise NameError("Hola DAM")
except NameError:
    print("La excepcion NameError se ha lanzado")
    raise