### Aggregations: Min, Max, everything in between
# In brief, about to cover typical stuff like means, stdevs, sums, products
# medain, min, max, quantiles, etc.
# 

## Summing vals in arr
import numpy as np
L = np.random.random(100)
sum(L)      # standard python sum
np.sum(L)   # numpy sum - executes in Compiled mode, much faster
# note, the results of these 2 operations are not strictly equivalent
# also, np.sum() is aware of of multi-dimensional arrs, where sum() is not

# can compare times b/w these with %timeit --- also latter does feel faster too
big_array = np.random.rand(1000000)
sum(big_array)
np.sum(big_array)

## Minimum and Maximum
# min(), np.min()
# max(), np.max()
min(big_array), max(big_array)
np.min(big_array), np.max(big_array)

# again can compare exact with timeit, or judge feel by repeated execution

# also note, we can use methods from the array object itself as an alternate syntax
# personally, find it marginally more readable
big_array.min(), big_array.max(), big_array.sum()

### Multi-dimensional aggregates
# in 2D arrays, we often want aggregates organized along row or column
M = np.random.random((3, 4))
M
M.sum()         # returns sum of entire array

# we can specify an additional arg 'axis' to specify where aggregation takes place
M.min(axis=0)   # returns min of each corresponding column
M.max(axis=1)   # returns max of each corresponding row
