# At a basic level, Pandas objects can be thought of as enhanced versions of
# NumPy structured arrays in which the rows/cols are ID'd with labels instead of int indices

# Pandas provides many useful tools, methods, and functionality on top of basic data structures,
# but first you must understand the structures (objects)

# three fundamental Pandas data structures:
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

# also like NP array, data can be accessed via associated index:
data[1]
data[1:3]


## 'Series' as a generalized NumPy array
# diff b/w series and np arr:
# presence of index:
    # NP arr has an implicitly defined integer index
    # PD series has an explicitly defined index

# we can make the explicit index a value of any type (not just int):
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data
data['b']

# or make the indeces non-sequential:
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['2', '3', '5', '7'])
data
data[5]


## 'Series' as a specialized dictionary
# It's more accurrate to think of Series as a special Python dictionary
    # dict maps arbitrary keys to arbitrary values
    # series maps typed keys to a set of typed values

# the typing is important: the static typing is why PD arrs are more efficient than dicts
    # NP arrays > Python lists
    # PD Series > Python dicts

# an example to clarify the relationship --- can create PD Series from dict
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population

# can then perform typical dict-style item access on the new PD Series:
population['California']

# additionally, Series supports array-style slicing (while dicts do NOT)
population['California':'Illinois']


## Constructing Series objects
# all constructors so far have been a version of following statement:
pd.Series(data, index='index')

# data can be a NP Array, 'index' defaults to int sequence
pd.Series([2, 4, 6])

# data can be a scalar - behavior is: scaled to fill specified indeces
pd.Series(5, index=[100, 200, 300])

# data can be a dictionary - 'index' defaults to sorted dictionary keys:
pd.Series({2:'a', 1:'b', 3:'c'})
    # NOTE: my iPython terminal is not displaying 1, 2, 3 as book shows.
    #       it shows in the order entered, even when stored in var.

# can set index explicitly for dict if you want, but it's a bit odd to say the least
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])

