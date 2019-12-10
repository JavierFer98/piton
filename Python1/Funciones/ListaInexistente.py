'''
Created on 19 nov. 2019

@author: Javier Fernández 
'''
def addLista(n, L=None):
    if L is None:
        L = []
    L.append(n)
    return L

print(addLista(1))
print(addLista(2))
print(addLista(3))