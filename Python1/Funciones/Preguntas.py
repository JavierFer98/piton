'''
Created on 21 nov. 2019

@author: Javier Fernández 
'''
def preguntar(mensaje, intentos=4, aviso="Opcion no valida, try again!"):
    while True:
            opcion=input(mensaje)
            if opcion in("s","si","S","SI"):
                return True
            if opcion in("n","no","N","NO"):
                return False
            intentos = intentos-1
            print("Te quedan ",intentos,"intentos")
            if intentos == 0:
                raise ValueError("Respuesta no valida loco")
            print(aviso)
preguntar("De vd quieres salir?")
preguntar("Eres negro siempre o solo a veces?", 2)