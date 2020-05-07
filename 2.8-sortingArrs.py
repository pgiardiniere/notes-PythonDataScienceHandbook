# Basic NP array sorting algorithms in this chapter
# Insertion, Selection, Merge, Quicksort, etc.

# Selection Sort:
import numpy as np


def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])


# Random sort, obviously horrendous.
def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x


# NumPy's Sort Methods:
# Python has built-in sort() & sorted() for Lists, but NumPy's are better

# np.sort() uses Quicksort by default.
# Mergesort and Heapsort also available by specification.
x = np.array([2, 1, 4, 3, 5])
np.sort(x)      # Does not modify your object data.
x.sort()        # Modifies object data.

# argsort() method returns the indices of sorted elements
x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
x[i]                # construct sorted array via fancy indexing


# Sort 2D arrays along rows or columns using axis.
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
np.sort(X, axis=0)
np.sort(X, axis=1)
# This treats each row/column as an independent array.


# Partial sorts: Partitioning

# np.partition()
# Splits array into 2 parts, with first K indeces as the smallest vals
x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)

# can also partition along axes of multi-dimensional arrays
np.partition(X, 2, axis=1)

# np.argpartition()
# See definition of argsort(), is the same for partition().


# Example: k-Nearest Neighbors:

# create random set of 10 points on 2d plane
X = rand.rand(10, 2)

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
plt.scatter(X[:, 0], X[:, 1], s=100);

# compute distance between each pair of points (demonstrates broadcasting)
#       where distance = squared difference of each dimension
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1) 
# confirm point - (self) == 0
dist_sq.diagonal()

nearest = np.argsort(dist_sq, axis=1)
nearest

# first column simply validates that the nearest 'neighbor' is actually the same point, so we can ignore that

# this is more work than necessary though, argpart will do the heavy lifting for us if we're just interested in nearest $k$ neighbors
# we would partition row so the smallest $k + 1$ neighbor is in first column of the array
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

plt.scatter(X[:, 0], X[:, 1], s=100)
# draw lines from each point to its two nearest neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]
        # plot a line from X[i] to X[j]
        # use zip magic to make it work
        plt.plot(*zip(X[j], X[i]), color='black')

# note: for VERY large nearest neighbor searches, you may instead opt for "Scikit-learn" lib for tree-based / approximate algs 
# for even greater efficiency