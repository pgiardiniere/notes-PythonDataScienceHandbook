# The standard python implementation is written in C
# everything in Python is an object. All python objects are compound C structs

# i.e. the following variable:
x = 1000
# has the following expanded C structure:
# struct _longobject {
#     long ob_refcnt;
#     PyTypeObject *ob_type;
#     size_t ob_size;
#     long ob_digit[1];
# };

# Each varaible's purpose
    ob_refcnt           # reference count > a component of silent memory allocation/deallocation
    ob_type             # object type     > holds the Python object type
    ob_size             # object size     > specifies the size of the data members in bytes
    ob_digit            # ob_digitwhich contains the actual integer value that we expect the Python variable to represent.


# now consider a Python list, which can contain heterogenous data types
# necessarily, each position contains an arbitrary Python object, so each index contains header data

# arrays of single types are more efficient, as we can then use a general Py Object Header
# (contained in the first position) which all subsequent indeces reference.

# 2 ways of achieving single type arrays:
    # Built-in 'array' type in python       not used
    # NumPy arrays (np.array[])             quite useful

# crappy, built-in way ::
import array
L = list(range(10))
A = array.array('i', L)
print(A) 

#########################
### NumPy Array construction and manipulation
#########################
# recall np arrays are single-type, numpy infers 1 type from the data
import numpy as np
np.array([1,4,2,5,3])

# If mixed types deteced, upcasting attempt is made (e.g. floats + ints == floats)
np.array([3.14, 2, 4])

# to explicitly set type, use 'dtype' keyword
np.array([1, 2, 3, 4], dtype='float32')

# also, unlike lists, we can initialize a multi-dimensional array
# inner lists (i+3) are treated as rows  
np.array([range(i, i+3) for i in [2,4,6]])
# it pulls the value at index i from array, then in the current (new) array position,
# it nests an array with the range of vals from i to i+3. Creates upwards counting 2d arr


### Creating arrays from scratch:
# np contains some pre-built constructor methods that can be useful:

# create len=10 arr filled with 0s
np.zeros(10, dtype=int)

# create a 3x5 arr filled with 1s (floating point type)
np.ones((3,5), dtype=float)

# create a 3x5 arr filled with "3.14"
np.full((3,5), 3.14)

# create an array filled with linear seq, counting from 0 to 20, stepping by 2s
np.arange(0, 20, 2)

# create an array of 5 values, evenly spaced, between 0 and 1
np.linspace(0, 1, 5)

# create a 3x3 array of uniformly distributed random values (between 0 and 1)
np.random.random((3,3))

# create a 3x3 array of normally  distributed random values with mean 0 and St.Dev 1
np.random.normal(0, 1, (3,3))

# create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3,3))

# create a 3x3 identity matrix
np.eye(3)

# create an unintialized array of 3 ints (vals will be whatever already exists at mem location)
np.empty(3)

## np standard data types
# np is built in C, so it shares same data types
# you can see a list at the end of the chapter, or refer to C documentation

