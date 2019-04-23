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

# for example, may want demographic data foreach state population
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

# Can construct in most direct fashion by passing MultiIndex internal attributes
    # pass "levels" - a list containing available index vals for each level
    # pass "labels" - a list of lists that reference these labels
pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              labels=[[0, 0, 1, 1], [0, 1, 0, 1]])


## MultiIndex Level Names