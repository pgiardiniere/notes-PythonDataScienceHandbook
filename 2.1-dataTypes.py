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
#
#