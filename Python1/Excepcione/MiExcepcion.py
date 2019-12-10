'''
Created on 28 nov. 2019

@author: Javier Fernández 
'''
class MiExcepcion(Exception):
    def __int__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)
raise MiExcepcion(5+8)
try:
    raise MiExcepcion(5+8)
except MiExcepcion as e:
    print("La excepcion con valor: ",e.valor)
    raise
        
