import random
randomList = []
n = input("Nhap n = ")
n = int(n)
randomList = random.sample(range(1, 100), n)
max = randomList[0]
for value in randomList:
    if max < value:
        max = value
print("List random:" ,randomList)
print("Max number is:",max)


import random

randomFloatList = []
n = input("Nhap n = ")
n = int(n)
for i in range(0, n):
    x = round(random.uniform(50.50, 500.50), 2)
    randomFloatList.append(x)
min = randomFloatList[0]
for value in randomFloatList:
    if min > value:
        min = value
print("Random Float List:", randomFloatList)
print("Min number is:",min)





