'''
Created on 21 nov. 2019

@author: Javier Fernández 
'''
oper1 = lambda x, *,y=0, z=0  : x + y + z
print(oper1(1, y=4, z=9))
print(oper1(3))
