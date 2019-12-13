### Aggregations: Min, Max, everything in between
# In brief, about to cover typical stuff like means, stdevs, sums, products
# median, min, max, quantiles, etc.

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

## Multi-dimensional aggregates
# in 2D arrays, we often want aggregates organized along row or column
M = np.random.random((3, 4))
M
M.sum()         # returns sum of entire array

# we can specify an additional arg 'axis' to specify where aggregation takes place
# the axis keyword specifies which array dimension will be collapsed, NOT returned
M.min(axis=0)   # returns min of each corresponding column (collapse along x)
M.max(axis=1)   # returns max of each corresponding row    (collapse along y)


## Other aggregation functions
# NOTE most NumPy agg funcs have a NaN-safe alternative
# np.sum() ~~ np.nansum()

# the following (incomplete) list of aggregates will be touched frequently:
np.sum
np.prod
np.mean
np.std
np.var          # compute variance (max-min)
np.min
np.max 
np.argmin       # return index of min value
np.argmax       # return index of max value
np.median
np.percentile
np.any          # evaluate whether any elements are true
np.all          # evaluate whether all elements are true


## example: what is avg height of the US presidents
# NOTE I copied over the 'data' directory from the book into notes dir, can complete example work

# !head -4 data/president_heights.csv
import pandas as pd
data = pd.read_csv('data/president_heights.csv')    # reads csv into memory
heights = np.array(data['height(cm)'])              # takes 'heights' column from csv var
print(heights)

heights.mean()
heights.std()
heights.min()
heights.max()

np.percentile(heights, 25)
np.median(heights)
np.percentile(heights, 75)

## we can also visualize with Matplotlib
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()   # set plot style
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')