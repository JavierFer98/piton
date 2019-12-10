'''
Created on 19 nov. 2019

@author: Javier Fernández 
'''
def fibonacci(numero):
    lista = []
    a , b = 0 , 1
    while a < numero:
        lista.append(a)
        a , b = b , a+b
    return lista
print(fibonacci(1000))
fibonacccci = fibonacci(100)
print(fibonacccci)