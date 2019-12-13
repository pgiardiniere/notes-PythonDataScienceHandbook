### Computation on Arrays: Broadcasting
# Broadcasting is another means of vectorizing operations to remove loops
# It's a set of rules for applying binary ufuncs (addition, subt) on arrays of different sizes

# binary ufunc on arrs of same size example
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

# ex1: add a scalar to an array (equiv. to above)
a + 5

# ex2: add a 1d array to a 2d array:
M = np.ones((3, 3))
M
M + a   # a is streched (i.e. broadcasted) across the second dimension to match M's shape

# ex3: Simultaneous broadcasting of both arrays
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]     # form into 2d array of 1 column
a
b
a + b
# refer to the chapter for a figure (and appendix code) on this broadcast
# summary: broadcast BOTH arrays into common shape (a 3x3), then perform the addition

##############################
### Rules of broadcasting:
# In brief:

# 1) If arrays differ in their number of dimensions, the shape of one with 
#    fewer dimensions is padded with ones on its leading (left) side
# 2) If the shape of the two arrays does not match in any dimension, the array 
#    with shape equal to 1 in that dim is stretched to match the other shape
# 3) If in any dimenstion the sizes disagree and neither is equal to 1, 
#    an error is raised

# examples below to demonstrate:

# ------------------------------
### Broadcasting ex1: (demonstrates rules 1, 2)
M = np.ones((2, 3))
a = np.arange(3)

M.shape     # returns (3, 3)
a.shape     # returns (3,)

## by rule 1, a has fewer dimensions, so begin padding on left with ones:
# M.shape --> (2, 3)
# a.shape --> (1, 3)

## by rule 2, 'a' has a first dimension which disagrees, so we stretch it to match
# M.shape --> (2, 3)
# a.shape --> (2, 3)

## now that shapes match, the operation is finally performed
M + a   # returns: ([[1., 2., 3.],
        #            [1., 2., 3.]]) 

# ------------------------------
### Broadcasting ex2:
a = np.arange(3).reshape((3, 1))
b = np.arange(3)

a.shape     # returns (3, 1)
b.shape     # returns (3,)

## by Rule 1, we pad shape of b with ones (on the left!):
# a.shape --> (3, 1)
# b.shape --> (1, 3)

## by Rule 2, we upgrade each of these ones to match the corresponding size of the other:
# a.shape --> (3, 3)
# b.shape --> (3, 3)

## the result matches, and shapes are compatible. operation can run without error
a + b

# ------------------------------
### Broadcasting ex3: (demonstrates incompatible shapes, rule 3)
M = np.ones((3, 2))
a = np.arange(3)

M.shape     # returns: (3, 2)
a.shape     # returns: (3,)

## by Rule 1, we pad shape of a with ones:
# M.shape --> (3, 2)
# a.shape --> (1, 3)

## by Rule 2, first dimension of 'a' is stretched to match M
# M.shape --> (3, 2)
# a.shape --> (3, 3)

# But we can't stretch M, as the dimension which doesn't match is != 1
# if the rules allowed stretching arrays in that way there would be amgiguous cases
# so, we hit rule 3, "operands could not be broadcast together with shapes (3,2) (3,)"
# M + A

# in this particular case, we could make 'a' and M compatible by adding a's shape
# with ones on the RIGHT, rather than left. We can pad on the right manually by adding a newaxis:
a[:, np.newaxis].shape  # returns (3, 1)
M + a[:, np.newaxis]

# note this applies to all ufuncs, not just addition. used only for simplicity.


##############################
### Broadcasting in Practice

## Centering an array:
# say you have an array of 10 observations, each containing 3 values
X = np.random.random((10, 3))
X
# compute the mean using 'mean' aggregate across first dimension
Xmean = X.mean(0)
# center the x array by subtracting the mean
X_centered = X - Xmean
# as a double check, by taking mean of centered array, it should be near-0
X_centered.mean(0)


## Plotting a 2d function
# can display images based on two-dimensional functions
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

# %matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()