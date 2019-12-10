'''
Created on 5 nov. 2019

'''
mares1 = ['mediterraneo', "cantabrico", "baltico", "adriatico", "tirreno", "egeo"]
mares2 = ["rojo", "muerto", "caspio", "negro", "arábigo", "sulu"]
mares = mares1 + mares2
mares[11:12] = ["del norte", "alabran"]
for i in range(len(mares)):
    print(mares[i])
mares.append('baltico')
for i in range(len(mares)):
    print(mares[i])
print(mares[11])
del mares[5]
for i in range(len(mares)):
    print(mares[i])
    todoslosmares = 0
for mar in mares:
    todoslosmares += 1
print(len(mares))
mares1.sort()
print(mares1, "Ordenado")
mares2.sort()
print(mares2,  "Ordenado")