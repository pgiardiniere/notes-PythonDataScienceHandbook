### Fancy Indexing
# until now, we've used:
    # simple indexing   e.g. arr[0] or arr[:5]
    # boolean masks     e.g. arr[arr > 0]
# can also use fancy indexing, in which we pass arrays of indices in place of scalars
# allows for selecting more complicated subsets of array values

import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
x

# access 3 different elements
[x[3], x[7], x[2]]  # simple indexing
ind = [3, 7, 4]     
x[ind]              # fancy indexing

# with fancy indexing, the shape of retrun arr reflects shape of index arrays, not shape of arr being indexed
ind = np.array([[3, 7], 
                [4, 5]])
x[ind]

# fancy indexing also works in multi-dimensional arrs
X = np.arange(12).reshape((3, 4))
X

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col] 
# values returned located at (0,2)(1,1)(2,3) - this is due to how the Broadcasting rules are applied
# following that logic, we can apply principle to row/column vectors (in addition to the scalars per above)

X[row[:, np.newaxis], col]
# recall row[:, np.newaxis] will translate the existing array to a 2d array of 1 column
# so now the return is a (broadcasted) 3x3 grid 

# same thing with broadcasting, we can apply mathematical operations
row[:, np.newaxis] * col

##############################
### Combined indexing
# if you use Fancy indexing for part of your access arg, you can still use other forms of access in conjunction with it
# e.g. simple indexing, slicing, and masking
X[2, [2, 0, 1]]                             # Simple Indexing
X[1:, [2, 0, 1]]                            # Slicing
mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]                 # Masking

## Example: selecting random points
# Common use of fancy indexing: select subsets of rows in a matrix
# Consider an arbitrary number of data points N for a data set with arbitrary number of dimsnesions D 
# (in this case, a 2d normal distribution)
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
X.shape     # returns (100, 2)

import matplotlib.pyplot as plt
import seaborn; seaborn.set() # for plot styling

plt.scatter(X[:, 0], X[:, 1])

# with fancy indexing, we can easily select 20 random points (ensuring that they're each unique)
indeces = np.random.choice(X.shape[0], 20, replace=False)
indeces
selection = X[indeces]
selection.shape

# to see our selection on the graph, we can plot circles over them
plt.scatter(X[:, 0], X[:, 1], alpha = 0.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', s=200) 

##############################
### Modifying values with Fancy Indexing
# In the following example, we use an array of indeces to modify the data at those indeces
x = np.arange(10)
i = np.array[2, 1, 8, 4]
x[i] = 99
x
# we can use any assignment operators
x[i] -= 10

## multiple operations on a single index: unintended effects!
x = np.zeros(100)
x[[0, 0]] = [4, 6]  # assigns 4, then assigns 6 to index 0. Only 6 will remain
x                   # [6. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# expanding on that idea...
i = [2, 3, 3, 4, 4, 4]
x[i] += 1
x                   # [6. 0. 1. 1. 1. 0. 0. 0. 0. 0.]
# the assignment is repeated multiple times, but not the augmentation of "x[i] = x[i] + 1"

## multiple operations on a single index: the right way
# reset & re-use example above. this time using at()
x = np.zeros(10)
np.add.at(x, i, 1)
x                   # [0. 0. 1. 2. 3. 0. 0. 0. 0. 0.]
# at() does in-place application of the given operator at parameters specified
# reduceat() is not covered here, but similar in application

### example: binning data
np.random.seed(42)
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
# find the appropriate bin for each x
i = np.searchsorted(bins, x)
# add 1 to each of these bins
np.add.at(counts, i, 1)

# count now reflect a number of points within each bin - i.e. a basic histogram
# plot results:
plt.plot(bins, counts, linestyle='steps');


# creating bespoke histograms like this is silly, use plt.hist()
plt.hist(x, bins, histtype='step');

# function creates nearly identical plot to the first one, in one line.
# To compute binning, matplotlib uses np.histogram func, which is similar.
# comparison:
print("NumPy routine:")
%timeit counts, edges = np.histogram(x, bins)

print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)

# the custom routine outperforms, but only b/c this use case is over-simplistic
# try again with larger dataset:
x = np.random.randn(1000000)
print("NumPy routine:")
%timeit counts, edges = np.histogram(x, bins)

print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)