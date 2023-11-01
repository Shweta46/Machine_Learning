import numpy as np

# To generate a random number from uniform distribution between 0 and 1 with a given dimension array
a1 = np.random.rand(2)
print(a1)

a2 = np.random.rand(1)
print(a2)

# Generate random number from standard normal distribution
a = np.random.randn(5,5)
print(a)
b = np.random.randn(3,2)
print(b)

c = np.random.randint(1, 100)
print(c)

d = np.random.randint(1, 100, 100)
print(d)

arr = np.arange(30) #returns evenly spaced integers in the given interval
print(arr)

ranarr = np.random.randint(0, 50, 10) #gives random integers within the given range
print(ranarr)

e = arr.reshape(5, 6)
print(e)

f = ranarr.max()
print(f)

g = ranarr.argmax() #returns the index of the maximum element in the array
print(g)

h = ranarr.argmin() #returns the index of the minimum element in the array
print(h)

i = arr.shape
print(i)

j = arr.reshape(1, 30)
print(j)

k = arr.reshape(1, 30).shape
print(k)

l = arr.reshape(30, 1)
print(l)

m = arr.reshape(30,1).shape
print(m)