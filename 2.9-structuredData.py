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
### Ways of creating Structured Arrays:
# Dictionary method
np.dtype({'names':('name', 'age', 'weight'),
          'formats':('U10', 'i4', 'f8')})

# We can specify numerical types with Python types or NP dtype S
np.dtype({'names':('name', 'age', 'weight'),
          'formats':((np.str_, 10), int, np.float32)})

# Compound types can be specified as list of tuples
np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])

# Finally, we can specify types without names in comma-seperated string
np.dtype('S10,i4,f8')

###################################
### shortened string format codes note:

## first char:          specifies ordering convention for significant bits
#   <   little endian       
#   >   big endian

## second char: specifies the type of data
#   b   Byte                    np.dtype('b')
#   i   signed integer          np.dtype('i4')  == np.int32
#   u   unsigned integer        np.dtype('u1')  == np.uint8
#   f   floating point          np.dtype('f8')  == np.int64
#   c   complex floating point  np.dtype('c16') == np.complex128
#   S   String                  np.dtype('S5')
#   a   String                  np.dtype('S5')
#   U   Unicode string          np.dtype('U')   == np.str_
#   V   Raw data (void)         np.dtype('V')   == np.void

## third char: specifies size of object in bytes

# ex: <f8   -little end. float point of 8 bytes

###################################
### More Advanced compound types
# 1st example: data type of 'mat' (matrix) component
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
X[0]
X['mat'][0]
# this is a useful idea when creating Python interfaces to C / Fortran libs which manipulate structured data
# (recall this NP dtype maps directly to a C structure def)

## RecordArrays
# np.recarray is almost identical to structured arrays, with one addition:
# fields can be accessed as attributes rather than as dictionary keys

# from prior:
data['age']

# but now:
data_rec = data.view(np.recarray)
data_rec.age

# drawback being: extra overhead involved in accessing fields
