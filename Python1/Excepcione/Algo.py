'''
Created on 28 nov. 2019

@author: Javier Fernández 
'''
def prueba():
    try:
        text = input("Teclea: ")
    except KeyboardInterrupt:
        print("Se ha pulsao cntrl+c")
    else:
        print("Has tecleado {}".format(text))
    finally:
        print("Fin")
        
prueba()