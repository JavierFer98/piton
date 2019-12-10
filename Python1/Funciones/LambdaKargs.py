'''
Created on 21 nov. 2019

@author: Javier Fernández 
'''
oper1 = lambda **kwargs: sum(kwargs.values())
print(oper1(uno=1, dos=2,tres=3,cuatro=4))
