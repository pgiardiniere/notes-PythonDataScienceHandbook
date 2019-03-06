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
