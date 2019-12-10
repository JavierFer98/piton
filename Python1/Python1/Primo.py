'''
Created on 19 nov. 2019

'''
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j=num/i
            print ('%d es igual a %d * %d ' % (num,i,j))
            break
    else:
        print(num, "es un numero primo")
    