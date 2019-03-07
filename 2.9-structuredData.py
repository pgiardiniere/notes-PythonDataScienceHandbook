### NumPy Structured Arrays & Record Arrays
# Sometimes data can not be represented as a homogenous array of values
# In these situations, NP Structured Arrays & Record Arrays are useful
    # Note: there is significant overlap of functionality with Pandas "Dataframe S", 
    # which is generally more useful when going beyond simple operations. See CH 3

# recall NP arrays default to a single type, makes tracking multiple categories of data sucky
import numpy as np
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

# also recall we can manually set dtype
x = np.zeros(4, dtype=int)

# So, can use compound data type specification to make a structured array, with custom names and types. 
# This is the Dictionary method of declaration:
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                         'formats':('U10', 'i4', 'f8')})
print(data.dtype)

# U10 = 'unicode string, max length 10
# i4  = '4-byte (32 bit) integer'
# f8  = '8-byte (64 bit) float'

# now we can feed our initial disparate lists into the structured array
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

# with structured arrays, we can refer to vals by index OR name (if both, seems index comes first)
data['name']        # get all names
data[0]             # get first row
data[-1]['name']    # get name from last row

# can combine this with our knowledge of masking to do filtering:
# return names of those with age under 30
data[data['age'] < 30]['name']

# if you want to go beyond this in complexity, Pandas will be the more powerful utility 

###################################
### Other methods of creating Structured Arrays:
