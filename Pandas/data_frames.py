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

# ************************************************************************
# ADDING A NEW COLUMN:

# creating a new column in the already existing data frame by using already existing columns
df['new'] = df['W'] + df['X']
print(df['new'])
print(df)

# To drop/ omit a column, simply writing the below line wont do, gives a value error
# df.drop('new')

# For this, an additional argument needs to be specified called axis, this specifies whether the series to be dropped is either in the row or the column.

# For deleting a column, axis = 1, and for deleting a row, axis = 0. This is like that because pandas is just built on top of numpy library.
print("\nAfter the dropping")
d = df.drop('new', axis=1)
print(d)

# but df will still have the new column we created
print(df)

# for that, we need to input an extra argument called inplace argument to make the changes stay and occur permanently
# now using the below code, the changes made will reflect in the df dataframe itself
df.drop('new', axis=1, inplace=True)
print(df)

# df.drop('E', axis=0, inplace=True)
print(df)

# the functions of numpy will work on the data types of this as well
print(df.shape)

# To print columns, we simply write
print(df['X'])

# Method to print rows
print("\nMethod for printing rows (Here, only row A is printed):\n")

print(df.loc['A'])

# can also select oh the basis of the position of the row
print("\nSelect oh the basis of the position of the row rather than name:\n")
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
print(df > 0)

# this prints the value of the numbers which are greater than 0
print(df[df > 0])

# for returning true for the value of W which are > 0
print("\nReturning true for the value of W which are > 0:")
print(df['W'] > 0)

# so, if we place a condition, say s = d['W'] > 0, and then encapsulate it inside df again, then only the rows for which the condition "s" returns true, will be printed
print(df[df['W'] > 0])

# print data frames where Z < 0
print("\nData frames which return True for the condition  Z < 0")
print(df[df['Z'] < 0])

df1 = df[df['W'] > 0]
print(df1)

# prints the subset of W the columns of which has value greater than 0
print(df1['X'])

# this can be done in one single step as well
print(df[df['W'] > 0]['Y'])
# or printing multiple columns here
print(df[df['W'] > 0][['X', 'Y']])

# OR breaking this down to multiple steps
s = df['W'] > 0
result = df[s]
columns = ['Y', 'X']
print(result[columns])

# MULTIPLE CONDITIONS: So instead of just giving one condition, that W> 0, we can give multiple conditions. To use multiple conditions, use "&" instead of "and".
print("\nMultiple conditions:")
print(df[(df['W'] > 0) & (df['Y'] > 0)])

# RESETTING THE INDEXING TO NORMAL 1, 2, 3,...:
# Here, the previous index of the df is reset to a column, and the actual index is just plain 0,1,2,...etc.
df.reset_index()

# **********************************************************************
# ADDITION OF NEW COLUMN:

newind = 'CA NY WY OR CO'.split()
print(newind)

df['States'] = newind
print(df)

# ***********************************************************************
# RESETTING THE INDEX'
print("\nSetting the index to states")
print(df.set_index('States'))
# the above code doesnt make the change permanent on df, we need to use the keyword of "inplace" like we used in the "drop" function above
print(df)

# To make changes:
df.set_index('States', inplace= True)
print(df)
# this removes the previous from the df altogether

# **********************************************************************
# MULTI INDEX AND INDEX HIERARCHY;
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
h1 = zip(outside, inside)
print('\nh1', h1)

h2 = list(h1)

print('\nh2', h2)

hier_index = list(zip(outside, inside))
print("\nList with zip:", hier_index)

# takes a list and creates a multi-index from it
hier_index = pd.MultiIndex.from_tuples(hier_index)
print('\n hier_index', hier_index)

print("\nOutside:", outside)

# this creates a multi index data frame, which columns as A and B
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print("\nData frames having multi levels of an index or has an index hierarchy:", df)

print("\nTo only print the row G1:")
g1 = df.loc['G1']
print("\nG1\n", g1)

print("\nPrinting only the row 1 of row G1:")
g2_1 = df.loc['G1'].loc[1]
print("\nG2 of 1:\n", g2_1)

# Giving the indices names\
print("\nGiving indices names:")
# using this, both indices have names now
n = df.index.names = ['Groups', 'Num']
print(df)

a1 = df.loc['G2']
print("\na1\n", a1)

a2 = df.loc['G2'].loc[2]['B']
print("\nAccessing elements:\n", a1)

# The above things can be done by the following code lines as well, that is multi level indexing
o = df.xs('G1')
print('\nMulti-level indexing using xs method.\no\n', o)

# o1 = df.xs(['G1', 1])
# print('\no1\n', o1)

print("\nIf we want all values of 1 index in G1 as well as in G2, then:")
# level is the name of the index you want to print or choose (we have two indices here, groups and num)
o2 = df.xs(1, level='Num')
print('o2\n', o2)