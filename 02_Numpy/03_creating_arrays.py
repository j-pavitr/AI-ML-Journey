import numpy as g
'''arr = g.zeros((3,4))
print(arr)
print(arr.shape)

arr1 = g.ones((2,5))
print(arr1)
print(arr1.shape)

arr2 = g.arange(1,11)
print(arr2)
print(arr2.shape)

arr3 =  g.arange(0,20,2)
print(arr3)
print(arr3.shape)

arr4 = g.linspace(1,10,5)
print(arr4)
print(arr4.shape)

arr5 =  g.arange(1,13)
print(arr5)
mat = arr5.reshape(3,4)
print(mat)
mat1 = arr5.reshape(4,3)
print(mat1)
'''
n = g.arange(1,17)
print(n.reshape(4,4))
print(n.reshape(4,4).shape)
print(n.reshape(4,4)[:,0])
print(n.reshape(4,4)[-1])
print(n.reshape(4,4)[1:3,1:3])