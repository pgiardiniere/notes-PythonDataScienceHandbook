### Comparisons, Masks, and Boolean Logic
# Masking is useful when you want to extract, modify, count, or just
# manipulate values in an array based on some arbitrary criteria

# in Python, Boolean masking is usually most efficient way to achieve this

## example: counting rainy days
# load the daily rainfall statistics for Seattle in 2014:
import numpy as np
import pandas as pd

rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0   # 1/10mm -> inches conversion
inches.shape                # (365, 0) - daily measurement for 1 yr

## omitting matplotlib snippet,
## do not have environment set up for it yet
## wait until ch 4 to revisit

# histogram plot is good to see general shape of data
# but for specific questions (e.g. num rainy days, avg precip on them, etc.)
# we'll use masking to quickly answer

###################################
### Comparison Operators as ufuncs
# Before, we covered basic arithmetic operators as ufuncs: +, -, *, /
# Now, we can add comparson operators to that list:
# <, >, <=, >=, !=, ==

# the result these return is always an array with boolean data type

x = np.array([1, 2, 3, 4, 5])
x < 3       # equivalent to np.less(x, 3)
x > 3       # equiavlent to np.greater(x, 3)
x <= 3      # equiavlent to np.less_equal(x, 3)
x >= 3      # equiavlent to np.greater_equal(x, 3)
x != 3      # equiavlent to np.notequal(x, 3)
x == 3      # equiavlent to np.equal(x, 3)

# also like before, these work with multi-dimensional arrays. 2D ex below:
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
x
x < 6

## Working with Boolean Arrays
# As is typical, True evaluates to 1, False evaluates to 0
# so both of these methods count total True entries:
np.count_nonzero(x < 6)
np.sum(x < 6)
# using sum, we can break up along axes as well
np.sum(x < 6, axis=1)   # num vals < 6 in each row

np.any(x > 8)   # any vals > 8, returns bool (True)
np.all(x < 0)   # any vals < 0, returns bool (False)
np.all(x < 10)
np.all(x == 6)
# can also break these up along axes:
np.all(x < 8, axis=1)

## Boolean Operators