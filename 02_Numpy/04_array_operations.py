import numpy as we
# learning

arr = we.array([2,5,4,6,7,8,9,3,1,10])

print(arr.min())
print(arr.max())
print(arr.sum())
print(arr.mean())
print(arr.std())
print(we.sort(arr))
print(arr>5)
print(arr[arr>5])

brr = arr
print(brr)
brr[0] = 12
print(brr)

print(arr)

crr = arr.copy()
crr[2] = 14
print(crr)
print(arr)
'''
#now practising
m = we.array([55,72,91,34,87,65,49,100])
print(m.max())
print(m.min())
print(m.mean())
print(m[m>70])
print(we.sort(m))
print(m.sum())
'''