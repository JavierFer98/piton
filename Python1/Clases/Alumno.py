'''
Created on 26 nov. 2019

@author: Javier Fernández 
'''
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.deportes= []
    
    def addDeportes(self, deporte):
        self.deportes.append(deporte)
        
a1= Alumno("Javier")
a2= Alumno("Diego")
a3= Alumno("Pablo")
a1.addDeportes("Teto")
a2.addDeportes("Crushing")
a3.addDeportes("Meterme picos")

print(a1.nombre)
print(a2.nombre)
print(a3.nombre)
print(a1.deportes)
print(a2.deportes)
print(a3.deportes)