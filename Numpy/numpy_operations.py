import numpy as np
arr = np.arange(0, 46)

print(arr+arr)

print(arr*arr)

print(arr**3)

# Universal array functions

a = np.sqrt(arr)
print(a)

b = np.exp(arr)
print(b)

c = np.max(arr)
print(c)

d = np.sin(arr)
print(d)

# e = np.log(arr)
# print(e)

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr1 = np.reshape(2,5)
print(arr1)