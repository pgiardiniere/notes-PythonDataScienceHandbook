import numpy as np

# Recall how to explicitly set dtype on a normal np array.
x = np.zeros(4, dtype=int)

# With np's Structured Arrays, we have multiple datatypes in one.
data = np.zeros(4, dtype={'names': ('name', 'age', 'weight'),
                          'formats': ('U10', 'i4', 'f8')})
print(data.dtype)

# U10 = 'unicode string, max length 10
# i4  = '4-byte (32 bit) integer'
# f8  = '8-byte (64 bit) float'

# Now we can put lists containing data items on 4 people into a structured arr.
data['name'] = ['Alice', 'Bob', 'Cathy', 'Doug']
data['age'] = [25, 45, 37, 19]
data['weight'] = [55.0, 85.5, 68.0, 61.5]
print(data)

# with structured arrays, we can refer to vals by index or name
data['name']        # get all names
data[0]             # get first row
data[-1]['name']    # get name from last row

# Return name of people less than 30 years old (by masking).
data[data['age'] < 30]['name']

# While nice, you'd generally prefer Pandas for these types of datasets.


# Methods to Create Structured Arrays:

# Dictionary method...
np.dtype({'names': ('name', 'age', 'weight'),
          'formats': ('U10', 'i4', 'f8')})  # Python types
np.dtype({'names': ('name', 'age', 'weight'),
          'formats': ((np.str_, 10), int, np.float32)})  # NumPy types

# List of Tuples method...
np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])

# Unnamed data, types in comma-seperated string method...
np.dtype('S10,i4,f8')


# NOTE: Shortened string format codes
# first char:       specifies ordering convention for significant bits
#   <   little endian
#   >   big endian

# second char:      specifies the type of data
#   b   Byte                    np.dtype('b')
#   i   signed integer          np.dtype('i4')  == np.int32
#   u   unsigned integer        np.dtype('u1')  == np.uint8
#   f   floating point          np.dtype('f8')  == np.int64
#   c   complex floating point  np.dtype('c16') == np.complex128
#   S   String                  np.dtype('S5')
#   a   String                  np.dtype('S5')
#   U   Unicode string          np.dtype('U')   == np.str_
#   V   Raw data (void)         np.dtype('V')   == np.void

# third char: specifies size of object in bytes


# More Advanced Compound Types:
"""Know this:
np dtype maps directly to a C struct, meaning the buffer containing
array content can be accessed directly by a C program.
"""
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
X[0]
X['mat'][0]


# RecordArrays:
# np.recarray is almost identical to structured arrays, with one addition:
# fields can be accessed as attributes rather than as dictionary keys

# from prior:
data['age']

# but now:
data_rec = data.view(np.recarray)
data_rec.age

# drawback being: extra overhead involved in accessing fields
# %timeit data['age']
# %timeit data_rec['age']
# %timeit data.age

# again, know that Pandas will be the generally preferred lib
# for compound data types / structured arrays
