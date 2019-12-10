'''
Created on 5 nov. 2019

'''

mares1 = ['mediterraneo', "cantabrico", "baltico", "adriatico", "tirreno", "egeo"]
todoslosmares = 0
for mar in mares1:
    todoslosmares += 1
print(len(mares1))
for i in range(len(mares1)):
    print(mares1[i])  
mares2 = ["rojo", "muerto", "caspio", "negro", "arábigo", "sulu"]
todoslosmarees = 0
for maar in mares2:
    todoslosmarees += 1
print(len(mares2))
for i in range(len(mares2)):
    print(mares2[i]) 
mares=mares1+mares2
for marr in mares:
    todoslosmares += 1
print(len(mares))
for i in range(len(mares)):
    print(mares[i]) 
print(mares1[0])
print(mares1[1])
print(mares1[2])
print(mares1.index("egeo"))
print(mares2[3])
print(mares2[4])
print(mares2[5])
print(mares2.index("caspio"))
print(mares.index("caspio"))