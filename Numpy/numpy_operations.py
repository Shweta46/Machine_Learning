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


# using numpy, creating an array is done by this method
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr1 = arr1.reshape(2,5)
print(arr1)


# to create an array using numpy from a list of lists
my = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
my = np.array(my)
print(my)