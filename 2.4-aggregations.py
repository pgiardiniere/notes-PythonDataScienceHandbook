# Summary Statistics and More:
# mean, median, stdevs, min, max, quantiles, sum, product, etc.

# Summing Values in NumPy Arrays
import numpy as np
L = np.random.random(100)
big_array = np.random.rand(1000000)

sum(L)                  # Python   sum. 1D  arrs only
np.sum(L)               # NP ufunc sum. 2D+ arrs
sum(L) == np.sum(L)

np.sum(big_array)
big_array.sum()
# Generally, we prefer calling from object instance syntax.

# Minimum and Maximum
big_array.min(), big_array.max()

# Multi-Dimensional Aggregates
# For 2D arrays, we often want aggregates organized along rows or columns.
# We can toggle 'axis' argument of methods to perform this.
A = np.random.random((3, 4))
A
A.sum()

# NOTE: Axis controls dimension to collapse, and returns the complement.
A.min(axis=0)   # collapse row --> return min of cols
A.max(axis=1)   # collapse col --> return max of rows

# Most NumPy agg funcs have a NaN-safe equivalents (ignore NaN values).
A.sum; A.nansum


# Partial List of Aggregation Functions:
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


# Example: Get Average Height of US Presidents
# !head -4 data/president_heights.csv
import pandas as pd
data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
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
import seaborn; seaborn.set()
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')