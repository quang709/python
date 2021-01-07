# bai 10

import random


n = random.randrange(50,1000)
print('n = ' , n)

list_int = random.sample(range(-1000,1000),n)
print('List-int = ',list_int)

list_float =[]
for item in range(n):
    a = float(random.uniform(-1000,1000))
    list_float.append(a)
print('List-float = ',list_float)
