### NumPy Array Attributes:
# using 3 arrays for examples, a 1d, 2d, and 3d array
# using a set seed for reference
import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

# attributes each numpy array contains:
    # ndim      number of dimensions
    # shape     size of each dimension
    # size      total size of array
    # dtype     data type of array    
    # itemsize  size (bytes) of an arbitrary array element
    # nbytes    size (bytes) of the entire array

# print each respective example of array attribute:
print("x3 ndim    ", x3.ndim)      # 3
print("x3 shape   ", x3.shape)     # (3, 4, 5)
print("x3 size    ", x3.size)      # 60
print("x3 dtype   ", x3.dtype)     # int32
print("x3 itemsize", x3.itemsize)  # 4
print("x3.nbytes  ", x3.nbytes)    # 240          # generally == size * itemsize

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
x2[0, 0] = 3.14     # Typing note - this decimal get truncated. 3 inserted.


##############################
### Array slicing
# we can access single array elements with square brackets
# we can slice multiple array element (or Subarrays) with : inside of square brackets

# e.g. for an array 'x'
    # x[start:stop:step]

# default values: 
    # start = 0 
    # stop  = length (arr.size)
    # step  = 1

## Slicing 1d subarrays
x = np.arange(10)
x[:5]   # elements [0, 5)
x[5:]   # elements [5, x.size)
x[4:7]  # elements 
x[::2]  # elements [0, x.size) step by 2s     (all even nums)
x[1::2] # elements [1, x.size) step by 2s     (all odd  nums)

# negative step value swaps the default 'start' and 'stop' values.
# it's certainly a method to reverse an array. 
x[::-1]
x[5::-2]    # (imo, this just obscures index positions - i.e. whether they're inclusive or exclusive)

## Slicing 2d+ subarrays
x2
x2[:2, :3]      # [0, 2) rows   [0, 3)       cols
x2[:3, ::2]     # [0, 3) rows   [0, x2.size) cols,  step by 2   (so, 0th and 2nd cols)

# subarray dimensions can be reversed together with negative step
x2[::-1, ::-1]


## Accessing array rows and columns:
# How to get a col from set of columns as an array?
x2[:, 0]    # return first col
x2[0, :]    # return first row
x2[0]       # return first row     - terse syntax


## array slices in np are views, not copies, of array data
x2
x2_sub = x2[:2, :2]             # create a view of x2
x2_sub
x2_sub[0,0] = 9001
x2                              # altered x2 by modifying x2_sub

## We instead make copies of arrays using copy()
x2
x2_sub_copy = x2[:2, :2].copy() # create a full-copy of x2
x2_sub_copy
x2_sub_copy[0,0] = 42
x2                              # No alteration of original x2


##############################
### Array Reshaping w/ np.reshape()
# Attemps no-copy view of initial array.     But may create full-copy (if non-contiguous mem buffers)

# must always ensure arr.size == arr.reshape().shape[0] * arr.reshape.shape[1]
# i.e. the reshaped array dimension (assumeing an m x n matrix), we must have arr.size = mn

grid = np.arange(1, 10).reshape((3, 3))

## 1d array >> 2d array
# reshape() method:
x = np.array([1,2,3])
x.reshape((1,3))        # row vector via reshape
x.reshape((3,1))        # column vector via reshape

# 'newaxis' keyword within slice:
x[np.newaxis, :]        # row vector via newaxis
x[:, np.newaxis]        # column vector via newaxis

# The docs for newaxis reveal it's just an alias for None (see: np.newaxis?).  We can express instead as
x[None, :]        # row vector via newaxis
x[:, None]        # column vector via newaxis

##############################
### Array Concatenation and Splitting
## Concatenation methods: np.concatenate(), np.vstack(), np.hstack()

# np.concatenate( (a1, a2, ...), axis=0, out=None )     # method signature
# np.concatenate() REQUIRES a1.ndim == a2.ndim

# np.concatenate() for 1d arrays:
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate((x, y))      # returns: [1, 2, 3, 3, 2, 1]
z = np.array([99, 99, 99])
np.concatenate([x, y, z])   # returns: [1, 2, 3, 3, 2, 1, 99, 99, 99]

# np.concatenate() for 2d arrays:
grid = np.array([[1, 2, 3], [4, 5, 6]])     # create  2x3 matrix
np.concatenate([grid, grid])                # returns 4x3 matrix
np.concatenate([grid, grid], axis=1)        # returns 2x6 matrix


## Mixed dimension arrays, must use np.vstack() and np.hstack()
# vstack() ex:
x    = np.array( [9, 8, 7] )
grid = np.array([[6, 5, 4],
                 [3, 2, 1]])
np.vstack([x, grid])

# hstack() ex:
y = np.array([[99],
              [99]])
np.hstack([grid, y])

# also see :: np.dstack()  --- stacks arrays along the third axis


## Splitting
# routines/methods: np.split, np.vsplit, np.hsplit
# np.split() ex:
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])    # x1=[1, 2, 3] x2=[99, 99] x3=[3, 2, 1]

grid = np.arange(16).reshape((4, 4))

upper, lower =  np.split(grid, [2], axis=0)
upper, lower =  np.vsplit(grid, [2])

left, right = np.split(grid, [2], axis=1)
left, right = np.hsplit(grid, [2])

# also see :: np.dsplit()  --- splits arrays for axis=2
