# The standard python implementation is written in C
# everything in Python is an object. All python objects are compound C structs, e.g.

x = 1000                    # This var...
# struct _longobject {      # ...is really this C struct
#     long ob_refcnt;
#     PyTypeObject *ob_type;
#     size_t ob_size;
#     long ob_digit[1];
# };

# Each varaible's purpose
    # ob_refcnt           # reference count > a component of silent memory allocation/deallocation
    # ob_type             # object type     > holds the Python object type
    # ob_size             # object size     > specifies the size of the data members in bytes
    # ob_digit            # ob_digitwhich contains the actual integer value that we expect the Python variable to represent.

# clearly, arrays of single types are more efficient, as they use a general Py Object Header

#########################
### NumPy Array construction and manipulation
#########################
# recall np arrays are single-type, numpy infers 1 type from the data
import numpy as np

np.array([1, 4, 2, 5, 3])                   # ints      > inference from single type
np.array([3.14, 2, 4])                      # float32   > inference from >1 type --- upcasted to float32
np.array([1, 2, 3, 4], dtype='float32')     # float32   > declare type w/ keyword

# NP has built-in multi-dimensional arrays niceties. (row, col) syntax
np.array([range(i, i+3) for i in [2,4,6]])

# np constructor methods:
np.zeros(10, dtype=int)         # create 1x10 arr   filled with 0s (explicit dtype int)
np.ones((3,5), dtype=float)     # create 3x5 matrix filled with 1s (explicit dtype float)
np.full((3,5), 3.14)            # create 3x5 matrix filled with "3.14"
np.empty(3)                     # create 1x3  arr   filled with uninitialized values. Initially it contains whatever garb already stored there.
np.eye(3)                       # create 3x3 Identity Matrix

np.arange(0, 20, 2)             # arr filled with linear sequence, counting from 0 to 20, stepping by 2s
np.arange(20, 2)

np.linspace(0, 1, 5)            # arr of 5 values, evenly spaced, between 0 and 1

np.random.random((3,3))         # 3x3 arr of uniform distributed random vals, (between 0 and 1)
np.random.normal(0, 1, (3,3))   # 3x3 arr of normal  distributed random vals,  mean 0 and St.Dev 1
np.random.randint(0, 10, (3,3)) # 3x3 arr of uniform distributed random ints,  inside range [0, 10)


## np standard data types
# np is built in C, so it shares same data types
# you can see a list at the end of the chapter, or refer to C documentation

# Special note: Really it shares Python's datatypes, which are built on top of Cs datatypes.
    # np float == Python float   == C Double
    #             Python float32 == C Float