import numpy as np

# Bracket indexing and selection

arr = np.arange(0, 11)
print(arr)
print(arr[8])
print(arr[1:5])
print(arr[0:5])

# This sets the value within the given index range
arr[0:5] = 100
print(arr)

arr = np.arange(0, 11)
print(arr)

# to just print a portion of the array
slice_of_arr = arr[0:6]
print(slice_of_arr)

# To make every element of the slice above 99, we can use the below code line
slice_of_arr[:] = 99
print(slice_of_arr)

# this change in the slice also reflects in the original array we took the slice from
print(arr)

# the above steps show that the data is not copied but is the fragmented view of the original data. So when you change the view, the original data will also be affected.

# To copy the data to a new array, you have to be explicit.
arr_copy = arr.copy()
print(arr_copy)

# ************************************************************************
# INDEXING A 2D ARRAY:

arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
print(arr_2d)
print(arr_2d[1])

# Slicing of the array
print(arr_2d[:2, 2:])

# Shaping only the bottom row
print(arr_2d[2, :])

# ***********************************************************************
# FANCY INDEXING:

arr2d = np.zeros((10, 10))
print(arr2d)
arr_length = arr2d.shape[1]
print(arr_length)

for i in range(arr_length):
    arr2d[i] = i * 2
print(arr2d)

# Can print the specific rows of the matrix, and that too, out of order
print(arr2d[[2, 4, 6, 8]])
print(arr2d[[6, 4, 2, 7]])
print(arr2d)

arr = np.arange(1, 11)
print(arr)

print(arr>4)

# To print only those numbers which satisfy this condition
bool_arr = arr > 4
print(arr[bool_arr])

x = 7
print(arr > x)
