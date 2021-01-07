import numpy as np
_a = [ [1, 2, 3], [4, 5, 6] ]
a = np.array(_a)
print(a)



print(type(a))




# create matrix a
a = np.array([(1, 2, 3), (4, 5, 6)])
print("create matrix a",a)
# [[1 2 3]
#  [4 5 6]]

# create matrix b
b = np.array([(0, 5, 25), (4, 9, 9)])
print("create matrix b",b)
# [[0 5 25]
#  [4 9  9]]

# sum of a and b
c = a + b
print(" a+b",c)

# [[ 1  7 28]
#  [ 8 14 15]]


d = a*b
print("a*b",d)




