# At a basic level, Pandas objects can be thought of as enhanced versions of
# NumPy structured arrays in which the rows/cols are ID'd with labels instead of int indices

# Pandas provides many useful tools, methods, and functionality on top of basic data structures,
# but first you must understand the structures (objects)

# three fundamental data structures:
    # Series
    # DataFrame
    # Index

import numpy as np
import pandas as pd

##############################
### the Pandas Series object
# a Series is a one-dimensional array of indexed data
# can construct as follows:
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data

# as seen in output, Series wraps both sequence of vals and sequence of indices
# can access with 'values' and 'index' attributes

# 'values' are simply a NumPy array:
data.values

# 'index' is an array-like object of type pd.Index:
data.index

# also like NP array, data can be accessed associated index:
data[1]