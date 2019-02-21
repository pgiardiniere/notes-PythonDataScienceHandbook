### Python data types vs C
# As python is dynamically typed, we don't assign types to variables on declaration
# We can also switch a variable of type int to String seamlessly
# i.e.: 
# x = 4
# x = 'four'
# works without error, where C would throw an error due to type mismatch


### Python ints are more than ints
# Comparison: Python code and C w/ re. to data types

# /* C code */
# int result = 0;
# for(int i=0; i<100; i++){
#     result += i;
# } 
# note how all data types are explicitly stated

# Python code
result = 0
for i in range(100):
    result += i
# where here all data types are inferred, also allows us to assign 'result' to a string without error

# The standard python implementation is written in C
# SO, all python objects (and everything in Python is an object) is deep down
# just a compound C structure, i.e. the following int:
x = 1000
# ... actually creates a reference to a compound C structure, which when expanded, looks like this:

# struct _longobject {
#     long ob_refcnt;
#     PyTypeObject *ob_type;
#     size_t ob_size;
#     long ob_digit[1];
# };

# So we see the following integer actually contains these things:
    # ob_refcnt, a reference count that helps Python silently handle memory allocation and deallocation
    # ob_type, which encodes the type of the variable
    # ob_size, which specifies the size of the following data members
    # ob_digit, which contains the actual integer value that we expect the Python variable to represent.

# direct quote:
    # Notice the difference here: a C integer is essentially a label for a position in memory 
    # whose bytes encode an integer value. 
    # A Python integer is a pointer to a position in memory containing all the Python object information, 
    # including the bytes that contain the integer value.

### Python lists are more than lists
# consider that EVERY python object must contain this additional reference information in order to allow
# dynamic reassignment of variables.
# now consider a basic Python list, which can contain heterogenous data types
# every index of the list must contain a reference to an object with all the 'boilerplate' stuff discussed
# in the above notes on ints

# it would be much more efficient instead to have an array containing a single type, where each
# position inside the array gets the same information from a general Py Object Header (contained in
# the first position)

# 2 ways of achieving single type arrays:
# 1) built-in 'array' type in python
# 2) NumPy arrays (np.array[])

### 1-built-in method
import array
L = list(range(10))
A = array.array('i', L)
print(A) 
# this is well and good, but numpy achieves the same efficiency, while also containing efficient data operations/methods

### NumPy arrays (np.array[])   --- rest of notes will concern these arrays only
### NumPy Array construction and manipulation
import numpy as np
np.array([1,4,2,5,3])
# recall these must be single-type, and np is inferring type from the data
# if mixed types, an attempt at upcasting will be made (see float ex below)
np.array([3.14, 2, 4])
# to explicitly set type, use 'dtype' keyword
np.array([1, 2, 3, 4], dtype='float32')
# also, unlike lists, we can initialize a multi-dimensional array
# inner lists (i+3) are treated as rows  
np.array([range(i, i+3) for i in [2,4,6]])
# it pulls the value at index i from array, then in the current array position we are constructing,
# it places an array of range of vals from i to i+3. the result is a neat little upwards counting 2d arr

## Creating arrays from scratch:
# np contains some built-in constructor methods that can be useful:
# 
# create len=10 arr filled with 0s
np.zeros(10, dtype=int)
# create a 3x5 arr filled with 1s (floating point type)
np.ones((3,5), dtype=float)
# create a 3x5 arr filled with 3.14s 
np.full((3,5), 3.14)

# create an array filled with linear seq, counting from 0 to 20, stepping by 2s
np.arange(0,20,2)
# create an array of 5 values, evenly spaced, between 0 and 1
np.linspace(0, 1, 5)

# create a 3x3 array of uniformly distributed random values 
# (between 0 and 1)
np.random.random((3,3))
# create a 3x3 array of normally  distributed random values 
# with mean 0 and St.Dev 1
np.random.normal((0, 1, (3,3)))
# create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3,3))
# create a 3x3 identity matrix
np.eye(3)
# create an unintialized array of 3 ints
# (values will be whatever happens to already exist at that mem location)
np.empty(3)

## np standard data types
# np is built in C, so it shares same data types
# you can see a list at the end of the chapter, or refer to C documentation







