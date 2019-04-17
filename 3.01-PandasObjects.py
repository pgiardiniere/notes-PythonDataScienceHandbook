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


##############################
### the Pandas DataFrame object
# If   'Series'    is an analog of 1D array w/ flexible indeces
# Then 'DataFrame' is an analog of 2D array w/ flexible row/col indeces

# i.e. if you think of
    # 2d array as ordered sequence of aligned (sharing index) 1d columns
# then
    # DataFrame as ordered sequence of aligned Series objects

# Demonstration: new Series lisiting area of 5 states mentioned prior
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area

# Can use this in conjunction with "popularion" series from before
states = pd.DataFrame({'population': population, 'area': area})
states

# like Series, DataFrame has an index attribute that gives access to ind labels
states.index

# Additionally, DataFrame has a 'columns' attribute, which is an Index object
# containing column labels
states.columns


## DataFrame as a specialized dictionary
# Similarly, we can think of DataFrame as a specialized dictionary
    # Dictionary maps keys to values
    # DataFrame maps column name to a Series of column data

# demonstrated by asking for 'area' attribute, which returns the Series obj
states['area']

# sticking point! in a 2D NP array, data[0] returns first ROW
#                 in a DataFrame, data['col0'] returns first COLUMN
# thus, we prefer to think of DataFrames as generalized dicts for the most part


## Constructing DataFrame objects

# from a single Series object: (i.e. 1-column DataFrame)
pd.DataFrame(population, columns=['population'])

# from a list of dicts (using a list comprehension to create data)
data = [{'a': i, 'b': 2 * i}
         for i in range(3)]
pd.DataFrame(data)

# **NOTE: if keys in dict are missing, PD fills in with "NaN" vals **
pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

# from a dictionary of Series objects
pd.DataFrame({'population': population, 'area': area})

# from a 2d NP array (if omitting col names, int indeces used for each)
pd.DataFrame(np.random.rand(3, 2), 
             columns=['foo', 'bar'], index=['a', 'b', 'c'])

# from a NP structured array
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A
pd.DataFrame(A)


##############################
### The Pandas Index object
# In both 'Series' and 'Dataframes', we have explicit 'Index' to reference/modify

# Index object is an interesting structure
# can be thought of as either an immutable array or an ordered set 
    # (technically multi-set due to repeated vals)

# Consequences: certain operations available on Index objects
ind = pd.Index([2, 3, 5, 7, 11])
ind


## Index as immutable array
# like array, can use standard Python indexing notation to get vals/slices
ind[1]
ind[::2]

# similar attributes familiar to NP arrs
print(ind.size, ind.shape, ind.ndim, ind.dtype)

# as they are immutable, we cannot modify via normal shorthand
ind[1] = 0      # produces runtime error 'Index does not support mutable operations'


## Index as ordered set
# PD objects are designed to facilitate operations such as joins across datasets
# thus, set arithmetic is often very useful

# Index object follows many conventions used by pythons built-in "set" data structure
# unions, intersections, differences, and other combinations can be computed:
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

indA & indB         # intersection
indA | indB         # union
indA ^ indB         # symmetric difference

# can also equivalently access via object methods if you prefer
indA.intersection(indB)