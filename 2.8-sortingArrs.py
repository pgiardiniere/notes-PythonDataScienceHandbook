### Sorting Arrays
# covering the basic NP array sorting algorithms in this chapter
# insertion sorts, selection sorts, merge sorts, quick sorts, bubble sorts, etc.

# selection sort implementation:
import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])

# recall from cs401 - this requires N loops for list of N vals, so it's slow
# but very simple to write. (also see author's notes on Big-O notation used to
# describe algorithm scaling. a refreshing no-nonsense take)

# bogosort - now with less efficiency!
def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

# shuffle the entire array every time it isn't sorted, until it happens
# that the shuffle() method produces a sorted array
# average scaling of O[N * N!]

##############################
### NumPy built-in sort methods
# python has a general built-in sort() and sorted() for lists, but NumPy's are better

# np.sort()
# by default, uses a quicksort algorithm -- O[N log N] efficiency
# mergesort and heapsort available by specifying

# to return sorted version without modifying input arr:
x = np.array([2, 1, 4, 3, 5])
np.sort(x)
# to sort array in-place, you would instead use sort() method of arrays
x.sort()

# argsort() method returns the indices of sorted elements
x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
i   # returns [1 0 3 2 4]
# we can then construct the sorted array via fancy indexing
x[i]

## Sorting along rows or columns
# again, we can use the "axis" argument to specify rows/columns of multi-dimensional arrays
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
X

np.sort(X, axis=0)  # sort each column of X
np.sort(X, axis=1)  # sort each row of X
# this treats each row/column as an independent array - relationships b/w the two are lost

##############################
### Partial sorts: Partitioning
# np.partition()
# splits the array into 2 parts, where the first K indeces are the smallest vals in arr (interior of partitions is arbitrary order!)
# parameters: arr, K (num of smallest indeces to shift forward)
x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)

# can also partition along axes of multi-dimensional arrays
np.partition(X, 2, axis=1)

# np.argpartition() extends the idea of np.argsort() - i.e. np.argpartition() returns the indeces of of the partition (see example)

## Example: k-Nearest Neighbors:
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