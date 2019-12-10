'''
Created on 21 nov. 2019

@author: Javier Fernández 
'''
def pruebaAmbito():
    def ambito_local():
        varprueba = "local varprueba"
    def ambito_nonlocal():
        nonlocal varpureba
        varprueba = "nonlocal varprueba"
    def ambito_global():
        global varprueba
        varprueba = "global varprueba"
    varprueba = "test varprueba"
    ambito_local()()
    print("Puesta como local ",varprueba)
    ambito_nonlocal()()
    print("Puesta como nonlocal ",varprueba)
    ambito_global()
    print("Puesta como global ",varprueba)    