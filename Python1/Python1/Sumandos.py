'''
Created on 7 nov. 2019

'''
sumandos = [2, 3 , 6, 7 ,5 ,7, 8,7, 6,5]
sumandos.append(10)
sumandos.append(68)
sumandos.append(68)

count = 1 
sumandos.sort()
aux = None 
repetidos = {}
    for num in sumandos:
        if num == aux:
            print(num,"esta repetido")
            cont +=1
            repetidos.update({num:count})
        else:
            count = 1
        aux = num
    
