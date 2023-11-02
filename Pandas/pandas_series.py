import numpy as np
import pandas as pd

# Creating a series
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

s = pd.Series(data=my_data)
ss2 = pd.Series(my_data, labels)
s3 = pd.Series(d)
print(ss2)
print(s3)

# The data doesnt necessarily have to a be numeric value
s4 = pd.Series(labels, my_data)
print(s4)

# even functions can be added in this
s5 = pd.Series([sum, print, len])
print(s5)

# USING INDEX:
s1 = pd.Series([1,2,3,4], index= ['USA', 'Germany', 'USSR', 'Japan'])

s2 = pd.Series([1,2,5,4], index= ['USA', 'Germany', 'Italy', 'Japan'])
print(s1)
print(s2)

# prints the data indexed by the word
print(s1['USA'])

#
print(s1 + s2)

#