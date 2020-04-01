# For arrs of same size, ufunc add works intuitively.
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

# Adding a scalar to an array, has similarly intuitive definition.
a + 5

# Broadcasting: Add a 1d array to a 2d array.
# Note that len(M[0]) == len(a)
M = np.ones((3, 3))
M + a
# 'a' is Broadcasted - 'a' is added for each inner array.

# Broadcasting: Add a 1d array to a 1d array, on seperate axes.
# Result is a 3x3 Matrix
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]     # form into 2d array of 1 column
a + b


# Rules of Broadcasting:

# If arrays differ in their number of dimensions, the array with fewer
#    dimensions is padded with ones on its leading (left) side.

# If the shape of the two arrays does not match in any dimension, the array
#    with size=1 in the mismatched dimension is stretched to match.

# If the shape of the two arrays does not match in any dimension, and the
#    and size!=1 for either arr in mismatched dimension, error thrown.


# Demonstrates rules 1, 2
M = np.ones((2, 3))
a = np.arange(3)

M.shape     # returns (3, 3)
a.shape     # returns (3,)
M + a

# by rule 1, a has fewer dimensions, so begin padding on left with ones:
# M.shape --> (2, 3)
# a.shape --> (1, 3)

# by rule 2, 'a' has a first dimension which disagrees, so it is stretched
# M.shape --> (2, 3)
# a.shape --> (2, 3)

# Operation: ([[1., 2., 3.],
#              [1., 2., 3.]])


# Broadcasting ex2:
a = np.arange(3).reshape((3, 1))
b = np.arange(3)

a.shape     # returns (3, 1)
b.shape     # returns (3,)

# by Rule 1, we pad shape of b with ones (on the left!):
# a.shape --> (3, 1)
# b.shape --> (1, 3)

# by Rule 2, we upgrade each of these ones to match the corresponding size:
# a.shape --> (3, 3)
# b.shape --> (3, 3)

# The result matches, and shapes are compatible.
a + b


# Broadcasting ex3: (demonstrates incompatible shapes, rule 3)
M = np.ones((3, 2))
a = np.arange(3)

M.shape     # returns: (3, 2)
a.shape     # returns: (3,)

# by Rule 1, we pad shape of a with ones:
# M.shape --> (3, 2)
# a.shape --> (1, 3)

# by Rule 2, first dimension of 'a' is stretched to match M
# M.shape --> (3, 2)
# a.shape --> (3, 3)

# But we can't stretch M, as the dimension which doesn't match is != 1


# in this case, we could define an add for 'a' and M by padding a's shape
# with ones on the RIGHT, rather than left.
a[:, np.newaxis].shape
M + a[:, np.newaxis]

# NOTE: broadcasting behavior applies to all ufuncs, not just addition.


# Broadcasting in Practice:


# Centering an Array:
# Center an array of 10 observations, each containing 3 values.
X = np.random.random((10, 3))

Xmean = X.mean(0)       # Compute mean on first axis
X_centered = X - Xmean
X_centered.mean(0)      # Centered mean ~~= 0


# Plotting a 2D Function:
# We can display images based on two-dimensional functions.
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

# %matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()
