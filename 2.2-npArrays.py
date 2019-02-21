### NumPy array basics
# essentially all data manipulation in python is manip. of np arrays
# esp. when you consider pandas is a newer module, built on the base of np arrays
#
# types of manipulations covered:
    # Attributes of arrays
    # Indexing of arrays
    # Slicing of arrays
    # Reshaping of arrays
    # Joining and Splitting of arrays

### NumPy Array Attributes:
# using 3 arrays for examples, a 1d, 2d, and 3d array
# using a set seed for reference
import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

# attributes each array contains:
    # ndim      number of dimensions
    # shape     size of each dimension
    # size      total size of array
    
    # dtype     data type of array    
    # itemsize  size (bytes) of an arbitrary array element
    # nbytes    size (bytes) of the entire array

print("x3 ndim: ", x3.ndim)         # returns: 3
print("x3 shape:", x3.shape)        # returns: (3, 4, 5)
print("x3 size:", x3.size)          # returns: 60
print("x3 dtype:", x3.dtype)        # returns: int32
print("x3 itemsize:", x3.itemsize)  # returns: 4
print("x3.nbytes:", x3.nbytes)      # returns: 240          # also note, this is product of size * itemsize, makes sense

