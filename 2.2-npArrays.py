### NumPy array basics
# essentially all data manipulation in python is manip. of np arrays
# esp. when you consider pandas is a newer module, built on the base of np arrays
#
# types of manipulations covered:
    # Attributes of arrays
    # Indexing of arrays
    # Slicing of arrays
    # Reshaping of arrays
    # Concatenation and Splitting of arrays

##############################
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
print("x3.nbytes:", x3.nbytes)      # returns: 240          # generally this will simply be equal to product of size * itemsize

##############################
### Array indexing
# for a 1d array, works just like any other lang & standard python lists:
x1
x1[0]
x1[4]
x1[-2]   # negatives index counting back from end of arr

# for a 2d or greater array, we can feed in a tuple of indeces
x2
x2[0, 0]
x2[2, 0]
x2[2, -1]
x2[0, 0] = 12       # can access and reassign, as expected
x2[0, 0] = 3.14     # however, type must be constant, so this will get SILENTLY truncated as our arrays are int32 types


##############################
### Array slicing
# we can access single array elements with square brackets
# we can slice multiple array elements (or Subarrays) with : inside of square brackets
# for array x:
# x[start:stop:step]
# default values: start=0 stop='size of dimension (length)', step=1

## Slicing 1d subarrays
x = np.arange(10)
x[:5]   # first 5 elements
x[5:]   # elements after 5
x[4:7]
x[::2]
x[1::2]

# interesting note: negative 'step' value swaps the default 'start' and 'stop' values.
# meaning it's an effective shorthand to reverse an array:
x[::-1]
x[5::-2]

## Slicing 2d+ subarrays
x2
x2[:2, :3]      # 2 rows, 3 columns
x2[:3, ::2]     # 3 rows (all), every other column

# subarray dimensions can be reversed together with negative step
x2[::-1, ::-1]


## Accessing array rows and columns:
# get a single row of columns of an array, simply combine indexing and slicing w/ empty slice
x2[:, 0]    # return first column of x2
x2[0, :]    # return first row of x2
x2[0]       # return first row of x2 - functionally identical to above line


## subarrays as no-copy views
# array slices in np are views, not copies, of array data
# an example to demonstrate:
x2                              # return original x2 data
x2_sub = x2[:2, :2]             # create a subarray of x2
x2_sub                          # return contents of subarray
x2_sub[0,0] = 9001              # modify subarray contents
x2                              # return MODIFIED x2 data


## Creating copies of arrays: copy()
# when we DO desire an independent copy to be made of an array/subarray, we use the copy() method
x2                              # return original x2 data
x2_sub_copy = x2[:2, :2].copy() # create a subarray of x2 - independent copy!
x2_sub_copy                     # return contents of subarray
x2_sub_copy[0,0] = 42           # modify subarray contents
x2                              # return ORIGINAL x2 data


##############################
### Reshaping of arrays
# 'reshape()' is most flexible method for doing this
# it attempts to create a no-copy view of initial array, but sometimes must create an independent copy (non-contiguous mem buffers)
grid = np.arange(1, 10).reshape((3, 3))
# this example works b/c the size of both arrays matches

## 1d array >> 2d array
# reshape() method:
x = np.array([1,2,3])
x.reshape((1,3))        # row vector via reshape
x.reshape((3,1))        # column vector via reshape

# 'newaxis' keyword within slice:
x[np.newaxis, :]        # row vector via newaxis
x[:, np.newaxis]        # column vector via newaxis

##############################
### Array Concatenation and Splitting
# Concatenation = joining multiple arrays into one
# routines/methods: np.concatenate, np.vstack, np.hstack
# 
# 
# Splitting     = splitting one array into multiple
