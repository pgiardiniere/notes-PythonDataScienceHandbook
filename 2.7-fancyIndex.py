# Recall:
# Simple Indexing   e.g. arr[0] or arr[:5]
# Boolean Masks     e.g. arr[arr > 0]

# Now add in fancy indexing - pass arrays of indices in place of scalars

import numpy as np
rand = np.random.RandomState(42)
x = rand.randint(100, size=10)

# Access same 3 elements via Simple indexing and Fancy indexing
[x[3], x[7], x[2]]
ind = [3, 7, 4]
x[ind]

# As you'd expect, returned arr shape correlates 1-1 with index arr
ind = np.array([[3, 7],
                [4, 5]])
x[ind]

# Fancing indexing on a 2D array with 1D lists
X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

X[row, col]                 # Returned vals located at indices (0,2)(1,1)(2,3)
X[row[:, np.newaxis], col]  # Transpose rows, now return is 3x3 grid

# same thing with broadcasting, we can apply mathematical operations
row[:, np.newaxis] * col


# Combined Indexing:

# May perform simple/sliced access, masked access, and fancy in same call.
X[2, [2, 0, 1]]
X[1:, [2, 0, 1]]
mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]

# Example: Selecting Random Points

# Common use of fancy indexing: select subsets of rows in a matrix
# Consider arbitrary data points N, on arbitrary num of dimensions D
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
X.shape

import matplotlib.pyplot as plt
import seaborn; seaborn.set()

plt.scatter(X[:, 0], X[:, 1])

# with fancy indexing, we can easily select 20 random points
indeces = np.random.choice(X.shape[0], 20, replace=False)
indeces
selection = X[indeces]
selection.shape

# to see our selection on the graph, we can plot circles over them
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', s=200)


# Modifying Values with Fancy Indexing:
x = np.arange(10)
i = np.array[2, 1, 8, 4]
x[i] = 99
x[i] -= 10

# Multiple operations on a single index occurs sequentially!
x = np.zeros(100)
x[[0, 0]] = [4, 6]

# Here, assignment is repeated, but not the incrementation
i = [2, 3, 3, 4, 4, 4]
x[i] += 1
x


# Multiple operations on a single index: The Right Way.
# reset & re-use example above. this time using at()
x = np.zeros(10)
np.add.at(x, i, 1)

# at() does in-place application of the given operator at parameters specified
# reduceat() is not covered here, but similar in application

# Example: Computing a histogram and binning data.
np.random.seed(42)
x = np.random.randn(100)

bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
# find the appropriate bin for each x
i = np.searchsorted(bins, x)
# add 1 to each of these bins
np.add.at(counts, i, 1)
plt.plot(bins, counts, linestyle='steps');


# Of course, instead of bespoke histograms we'd use plt.hist() irl.
plt.hist(x, bins, histtype='step');

# hist() creates nearly identical plot to the first one, in one line.
# comparison of matplotlib and bespoke processes:
print("NumPy routine:")
%timeit counts, edges = np.histogram(x, bins)

print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)

# The custom routine outperforms, but only b/c this use case is small.
x = np.random.randn(1000000)
print("NumPy routine:")
%timeit counts, edges = np.histogram(x, bins)

print("Custom routine:")
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)
