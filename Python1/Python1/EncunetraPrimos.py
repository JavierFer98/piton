'''
Created on 19 nov. 2019

'''
print(range(10))
list(range(5))
print("Encunetra los numeros primos")
for n in range(2, 20):
        for x in range(2,n):
            if n % x == 0:
                print(n, "equals" , x, "*", n//x)
                break
        else:
            print(n, " es un numero primo")
