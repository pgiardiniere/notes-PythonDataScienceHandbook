# Recall CH 2, discussed methods to access/set/modify values in NP arrays
# indexing, slicing, masking, fancy indexing, and combinations of them
# arr[2, 1]   arr[:, 1:5]       arr[0, [1,5]]

##############################
### Data Selection in Series
# As discussed, PD Series objects are similar to 1d NP arrays, and Python dicts


## Series as Dictionary
# like dicts, object provides mapping from collection of keys to values
import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data
data['b']

# can also use dict-like Python expressins/methods to examine keys/indices = vals
'a' in data         # evals to "True"
data.keys()         # lists keys + dtype
list(data.items())  # lists key-value mappings in total

# Series objects can be modified with dict-like syntax
# like you can extend dicts by assigning to a new key,
#          can extend Series by assigning a new index value
data['e'] = 1.25
data


## Series as a one-dimensional array
# Series builds on dict-like interface and provides array-style item selection
# like slices, masking, and fancy indexing. Each following:

# slicing by explicit index
data['a':'c']

# slicing by implicit integer index
data[0:2]

# masking
data[(data > 0.3) & (data < 0.8)]

# fancy indexing
data[['a', 'e']]

# NOTE: when splicing with explicit index, the final index is INCLUSIVE
#       when splicing with implicit index, the final index is EXCLUSIVE


## Indexers: loc, iloc, ix
# Slicing and indexing conventions are weird
data[1]     # uses explicit indices     - INCLUSIVE
data[1:3]   # uses implicit indices     - EXCLUSIVE

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data