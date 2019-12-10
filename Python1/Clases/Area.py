'''
Created on 26 nov. 2019

@author: Javier Fernández 
'''
from logging.config import BaseConfigurator
def area(self, base, altura):
    s = base * altura
    return s 

class Figura:
    def __init__(self, nombre):
        self.nombre=nombre
    superficie = area
    
    def mensaje(self):
        return
    
