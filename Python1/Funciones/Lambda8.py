'''
Created on 21 nov. 2019

@author: Javier Fernández 
'''
oper1 = lambda x, func: x + func(x)
print(oper1(2,lambda x: x * x))
print(oper1(2,lambda x: x + 3))
