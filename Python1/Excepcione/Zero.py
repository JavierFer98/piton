'''
Created on 28 nov. 2019

@author: Javier Fernández 
'''
print(5/0)
raise ZeroDivisionError('5/0')
try:
    raise ZeroDivisionError(5/0)
except ZeroDivisionError:
    print("Se lanzo la excepcion")
    raise