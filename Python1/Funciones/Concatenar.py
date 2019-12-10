'''
Created on 21 nov. 2019

@author: Javier Fernández 
'''
def concatenar(*args, sep="--"):
    return sep.joins(args)

print(concatenar("Hey","hola","adios"))
print(concatenar("Punto","si","punto",sep="."))
