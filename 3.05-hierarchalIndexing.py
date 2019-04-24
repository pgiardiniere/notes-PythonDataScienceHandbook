# Up to now, focused on 1D and 2D data in Series/DataFrames (respectively)
# To go to 3D and 4D, PD provides Panel/Panel4D objects to natively handle

# In practice, often circumvent those objects and use hierarchal indexing
    # aka multi-indexing
# This allows for multiple index levels within a single index,
# thus getting more dimensions packed into the Series/DataFrames objects

# As an introduction to the practice, explore creation/use of "MultiIndex"

import pandas as pd
import numpy as np

##############################
### A Multiply Indexed Series
# How to represent 2D data in a 1D Series

## ---------- The wrong way ----------
# Use tuples for keys to make life bad:

index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
pop

# The one nice part, can index or slice on this multiple index:
pop[('California', 2010):('Texas', 2000)]

# BUT, if you want all vals for 2010, need to do some ugly/inefficient work:
pop[[i for i in pop.index if[1] == 2010]]


## ---------- The better way ----------
# Use Pandas Multindex object - essentially an extension of the tuple
# with pre-built operations to keep code clean as efficient as possible

index = pd.MultiIndex.from_tuples(index)
index

# from output, can observe multiple levels of indexing 
# state names and years in this case, and multiple labels for each data point

# can re-index the series with this MultiIndex to see hierarchal rep. of data
pop = pop.reindex(index)
pop

# first 2 columns of series show multiple index values
# third column shows the data
# first column blank entries are repetitions of the prior (hence, hierarchal)

# now we can use familiar Pandas slicing notation:
pop[:, 2010]


## MultiIndex as extra dimension
# Could easily have stored the data in above example using DataFrame
# Can actually morph it by using unstack()
pop_df = pop.unstack()
pop_df

# stack() does the opposite:
pop_df.stack()

# with MultiIndexing, can go beyond this trivial example to store 3+ dimensions
# in both Series and DataFrame objects

# for example, may want demographic data for each state population
# with multiindex, its simple as just adding another column to the DF
pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df

# also, ufuncs still work with MultiIndexed data
# compute fraction of people under 18 by year:
f_u18 = pop_df['under18'] / pop_df['total']
f_u18.unstack()     # unstack() for formatting. neat!


##############################
### Methods of MultiIndex Creation
# The most straightforward way to construct mutiply indexed Series or DataFrames
# is to pass a list of 2 or more index arrays to the constructor
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])

# Can pass a dictionary with correctly config'd tuples as keys,
# pandas will auto-recognize and use MultiIndex by default
data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)


## Explicit MultiIndex Constructors
# sometimes you need additional flexibility only available via explicit methods
# As example before, can construct from a list of arrays (w/ index vals at each level)
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])

# Can construct it from a list of tuples (giving extended index vals of each point)
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])

# Can construct from Cartesian product of single indices too (saves keystrokes)
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

# Can construct in most direct fashion by passing MultiIndex internal params as args
    # pass "levels" - a list containing available index vals for each level
    # pass "labels" - a list of lists that reference these labels
pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              labels=[[0, 0, 1, 1], [0, 1, 0, 1]])


## MultiIndex Level Names
# Naming handy for larger datasets, to track meaning of index values
# Two ways to name:
    # Can pass the "names" argument to any of above MultiIndex constructors
    # Can set the "names" attribute of the index after the fact
pop
pop.index.names = ['state', 'year']
pop


## MultiIndex for Columns
# In a DataFrame, the rows/cols are completely symmetric
# Just as rows can have multiple levels of indices, cols can too

# following example demonstrates:
# --------- example begin -----------------------

# hierarchal indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                   names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data

# --------- example end   -----------------------

# Note there are 4 dimensions to the data in this DataFrame
    # Subject, Measurement type, Year, Visit Number

# Yet we can still get all relevant information by inputting person name:
health_data['Guido']
    # Yay for hierarchal indexing


##############################
### Indexing and Slicing a MultiIndex
# Indexing/Slicing is designed to be intuitive, just think of added
# indices as additional dimensions


## Multiply-indexed Series
pop

# can access single elements by indexing w/ multiple terms:
pop['California', 2000]

# MultiIndex also supports 'partial indexing' or indexing on just 1 level
# result is another Series, lower-level indices maintained:
pop['California']

# Partial slicing is available, so long as the MultiIndex is sorted
pop.loc['California':'New York']

# with sorted indices, partial indexing can also be performed on lower levels 
# by passing empty slice in the first index:
pop[:, 2000]

# other types of indexing/selection work too, such as boolean masks:
pop[pop > 22000000]

# and fancy indexing:
pop[['California', 'Texas']]


## Multiply-Indexed DataFrames
# from before: the example health data DataFrame
health_data

# remember columns are primary in DataFrame, 
# So syntax for multiply-indexed Series objects applies to columns now.
health_data['Guido', 'HR']

# As with single-index case, can use loc, iloc, ix indexers (see 3.02 for notes)
health_data.iloc[:2, :2]

# each index in loc or iloc can be passed a tuple of multiple indices
health_data.iloc[:, ('Bob', 'HR')]

# CANNOT create additional slices within index tuples
# health_data.loc[(:, 1), (:, 'HR')]      # throws an error    

# 2 ways around this, first, Python has built-in slice() method
# Better yet, Pandas has an IndexSlice object built to handle this situation
idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, 'HR']]


##############################
### Rearranging Multi-Indices
# Many operations will preserve all information in the dataset, but rearrange
# see: stack(), unstack() used before
# can more finely control re-arrangement of data b/w hierarchal inds/cols


## Sorted and Unsorted Indices
# Again, many MultiIndex slicing operations WILL fail if the index isn't sorted

# ex: Create multiply indexed data (indices are not lexographically sorted)
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data

# attempt to take a partial slice, results in error
try:
    data['a':'b']
except KeyError as e:
    print(type(e))
    print(e)
# error thrown & caught due to MultiIndex being unsorted

# simple Pandas convenience routines to sort:
    # sort_index()
    # sortlevel()
data = data.sort_index()
data
data['a':'b']       


## Stacking and Unstacking Indices
# can convert datasets from stacked multi-index to 2D representations
# in addition to prior use of unstack(), can optionally specify level to use:
pop
pop.unstack(level=0)    # Years  are now Columns
pop.unstack(level=1)    # States are now Columns

# stack() is the inverse of unstack, see example:
pop.unstack().stack()   # note output identical to pop


## Index setting and resetting
# Another way to rearrange hierarchal data is to turn index labels into cols
# reset_index()

# call reset_index() on pop dict: results in a DataFrame with new columns
# 'state' and 'year' - they contain the info formerly in the index
    # for clarity, specified data 'name' for column representation
pop_flat = pop.reset_index(name='population')
pop_flat
    # Often, raw input data will appear in formats like this.

# It's useful to get  practice building MultiIndex from the column values
# set_index() method of DataFrame - returns multiply-indexed DF:
pop_flat.set_index(['state', 'year'])


##############################
### Data Aggregations on Multi-Indices
# As seen, PD has built-in data aggreagation methods
    # e.g. mean(), sum(), max()

# For hierarchally stored data, can pass "level" parameter to specify
# the subset of data the aggregate is computed on
health_data

# To average the measurements taken in the 2 visits per year,
# name index level to explore (i.e. "year")
data_mean = health_data.mean(level='year')
data_mean

# can also take the mean among column levels too, use "axis" keyword
data_mean.mean(axis=1, level='type')

# this returns the average Heart Rate and Temperature 
# from all subjects, in all visits, each year.
    # will see similar functionality from "GroupBy" in Ch 3.08


##############################
### Aside: Panel Data
# Pandas has a few other fundamental data structures not yet discussesd
    # pd.Panel      object      Three-dimensional data
    # pd.Panel4D    object      Four-dimensional data

# Generally speaking, they carry a bit too much weight to be useful
# Can achieve representations of the same data using multi-indexing

# They will prove useful in some edge-cases, but focus on Series/DataFrames first
# (with MultiIndexing where appropriate)