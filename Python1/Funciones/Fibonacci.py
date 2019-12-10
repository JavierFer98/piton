'''
Created on 19 nov. 2019

@author: Javier Fernández 
'''
def fibonacci(numero):
    a , b = 0 , 1
    while a <numero:
            print(a, end=' ')
            a , b = b , a+b
    print()
fibonacci(200)
fibo=fibonacci
print(fibo(100))