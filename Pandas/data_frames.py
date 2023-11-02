import numpy as np
import pandas as pd
from numpy.random import randn

# seed keyword makes sure that the random numbers generated here are always the same random numbers
np.random.seed(101)

# the below code line:
# DataFrame(numbers to be filled in the indices, rows, columns)
# Each column is a series here, so namely W, X, Y, Z are series
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# to return the column W, which is a series
print(df['W'])
print(type(df['W']))

# the series can also be printed using the method below, but dont use this
print(df.W)

# to get multiple of series/ columns from the data frame created
print(df[['W', 'Z']])

# creating a new column in the already existing data frame by using already existing columns
df['new'] = df['W'] + df['X']
print(df['new'])
print(df)

# To drop/ omit a column, simply writing the below line wont do, gives a value error
# df.drop('new')

# For this, an additional argument needs to be specified called axis, this specifies whether the series to be dropped is either in the row or the column.

# For deleting a column, axis = 1, and for deleting a row, axis = 0. This is like that because pandas is just built on top of numpy library.
print("After the dropping")
d = df.drop('new', axis=1)
print(d)

# but df will still have the new column we created
print(df)

# for that, we need to input an extra argument called inplace argument to make the changes stay and occur permanently
# now using the below code, the changes made will reflect in the df dataframe itself
df.drop('new', axis=1, inplace=True)
print(df)

df.drop('E', axis=0, inplace=True)
print(df)

# the functions of numpy will work on the data types of this as well
print(df.shape)

# To print columns, we simply write
print(df['X'])

# Method to print rows
print(df.loc['A'])

# can also select oh the basis of the position of the row
print(df.iloc[2])

# to print a selective element in the array, we do this by matrix indices
print(df.iloc[2, 3])

# this is also called selecting the subset of rows and columns
print(df.loc['B', 'Y'])
# or
print(df.loc[['A', 'B'], ['W', 'Y']]) #this is like slicing a 2D array

# *********************************************************************
# CONDITIONAL SELECTION:
print(df)

# returns true for values which are greater than 0
print(df>0)

# this prints the value of the numbers which are greater than 0
print(df[df>0])

# for returning true for the value of W which are > 0
print("\nReturning true for the value of W which are > 0:")
print(df['W']>0)

# so, if we place a condition, say s = d['W'] > 0, and then encapsulate it inside df again, then only the rows for which the condition "s" returns true, will be printed
print(df[df['W']>0])

# print data frames where Z < 0
print("\ndata frames where Z < 0")
print(df[df['Z']<0])

#
print(df[df['W']>0]['Y'])