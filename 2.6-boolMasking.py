# Comparisons, Masks, and Boolean Logic:

# Masking is useful when you want to extract, modify, count, or just
# manipulate values in an array based on some arbitrary criteria.

import numpy as np
import pandas as pd

# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

# Count rainy days for Seattle in 2014.
rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0   # 1/10mm to inches conversion
inches.shape

plt.hist(inches, 40)
# The histogram plot shows the general shape of data, masking reveals more.


# Masking with Comparison Operator uFuncs:
# <, >, <=, >=, !=, ==

# The returned result is always an array with boolean data type, where
# True == 1, False == 0.

x = np.array([1, 2, 3, 4, 5])
x < 3       # equivalent to np.less(x, 3)
x > 3       # np.greater(x, 3)
x <= 3      # np.less_equal(x, 3)
x >= 3      # np.greater_equal(x, 3)
x != 3      # np.notequal(x, 3)
x == 3      # np.equal(x, 3)

# As before, these work with multi-dimensional arrays.
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
x < 6

# Both of these calls count total True entries on x < 6.
np.count_nonzero(x < 6)
np.sum(x < 6)

# using sum, we can break up along axes as well
np.sum(x < 6, axis=1)

np.any(x > 8)   # any vals > 8, returns bool (True)
np.all(x < 0)   # any vals < 0, returns bool (False)
np.all(x < 10)
np.all(x == 6)
# can also break these up along axes:
np.all(x < 8, axis=1)


# Masking with Bitwise Operator uFuncs:
# &, |, ^, ~

# &     np.bitwise_and
# |     np.bitwise_or
# ^     np.bitwise_xor
# ~     np.bitwise_not

# Recall bitwise operator precedence - parens required.
np.sum((inches > .5) & (inches < 1))
np.sum(inches == 0)
np.sum(inches != 0)
np.sum(inches > 0.5)
np.sum((inches > 0) & (inches < .2))


# Boolean Arrays as Masks:

# In prior section, used aggregates computed directly on Boolean arrays.
# Can also use Boolean arrays as masks in order to select subsets of data

# "Get x such that x < 5."
x[x < 5]

# Make rainy the mask of all rainy days.
# Then make summer the mask of all summer days (June 21st is 172nd day).
rainy = (inches > 0)
days = np.arange(365)
summer = (days > 172) & (days < 262)

np.median(inches[rainy])
np.median(inches[summer])
np.max(inches[summer])
np.median(inches[rainy & ~summer])


# Aside: using keywords "and/or" vs Operators "&/|"

# The keywords 'and/or' operate on the entire object
# The symbols  ' & / |' operate on the bits of the inner int/char/etc.

# using "and" or "or" asks Python to treat the object act a single Bool entity

# NOTE: when dealing specifically with numpy arrays,
# ALWAYS use bitwise operators.
