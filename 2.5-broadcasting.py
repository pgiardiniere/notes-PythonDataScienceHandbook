### Computation on Arrays: Broadcasting
# Broadcasting is another means of vectorizing operations to remove loops
# It's a set of rules for applying binary ufuncs (addition, subt) on arrays of different sizes

# binary ufunc on arrs of same size example
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

# first example of broadcasting - add a scalar to an array (equiv. to above)
a + 5

# second example - add a 1d array to a 2d array:
M = np.ones((3, 3))
M
M + a   # a is streched (i.e. broadcasted) across the second dimension to match M's shape

# third example, more complex. Simultaneous broadcasting of both arrays
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

# 1) If arrays differ in their number of dimensions, the shape of one with fewer is padded with ones on its leading (left) side
# 2) If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dim is stretched to match the other shape
# 3) If in any dimenstion the sizes disagree and neither is equal to 1, an error is raised

# further discourse on these rules found in examples below

### Rule 1) example:
M = np.ones((2, 3))
a = np.arange(3)

M.shape     # returns (3, 3)
a.shape     # returns (3,)

## by rule 1, a has fewer dimensions, so begin padding on left with ones:
# M.shape --> (2, 3)
# a.shape --> (1, 3)

## by rule 2, a has a first dimension which disagrees, so we stretch it to match
# M.shape --> (2, 3)
# a.shape --> (2, 3)

## now that shapes match, the operation is finally performed
M + a   # returns: ([[1., 2., 3.],
        #            [1., 2., 3.]]) 

