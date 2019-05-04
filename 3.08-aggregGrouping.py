### Aggregation and Grouping
# Now that we've fetched data in PD, time to explore the aggregation funcs
# sum(), mean(), median(), min(), max(), "groupby"s, etc.

import numpy as np
import pandas as pd

# omitting display function - muddies up the notes for not much gain

### Planets Data
# Will use Planets dataset, available via Seaborn pkg
# it has info on planets astronomers have discovered around other stars
import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape
planets.head()

##############################
### Simple Aggregation in Pandas
# Pandas Series aggregations behave similarly to the NumPy Arrays covered
# i.e. aggregates return a single value on them
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser
ser.sum()
ser.mean()

# for DataFrames, by default aggregates return results for each column
df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df
df.mean()
# specify "axis" argument to receive row info (i.e. columns as to-be-aggregated)
df.mean(axis=1)


# In addition to the other aggregators covered in CH-2.4 (np Aggregation)
# describe() method will return common summary statistics:
# describe() planets, and drop rows with missing data
planets.dropna().describe()

# A brief list of some built-in PD aggregations for Series/DataFrames:
    # count()               Total number of items
    # first(), last()       First, last item
    # mean(), median()      Mean, median
    # min(), max()          min, max
    # std(), var()          standard deviation, variance
    # mad()                 mean absolute deviation
    # prod()                product of all
    # sum()                 sum of all


##############################
### GroupBy: Split, Apply, Combine
# While simple aggregation can provide general idea of the dataset,
# often it's more insightful to aggregate conditionally on label/index

# this is implemented in "groupby" operation - so named after SQL command
# more popularly been described (by Hadley Wickham from R-land) as:
    # split, apply, combine

# see text for diagram, essentially 
#   Split - it breaks up DF depending on value of key into seperate entities
#   Apply - performs a function on the new individual groups
#   Combine - merges results into an output array

# in reality, this computation generally runs in a single pass on the input
# where results are updated as it goes


# example:
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key','data'])
df
df.groupby('key')
# NOTE: return is NOT a DataFrame, but DataFrameGroupBy object

# the DataFrameGroupBy object is a special view of the DataFrame, which performs
# NO computation until aggregation is Applied   ("lazy evaluation" approach)

# to produce result, Apply an aggregate, and see resulting Combine outputted
df.groupby('key').sum()


### The GroupBy Object
# ... is a flexible abstraction, can usually treat it as a collection of DFs
# with additional operations
    # Basics:   Column Indexing, Iteration over groups, dispatch methods
    # More:     Aggregate, Filter, Transform, Apply

## Column Indexing:
# GroupBy object supports col indexing same way as DataFrame, returns GroupBy
planets.groupby('method')
planets.groupby('method')['orbital_period']
planets.groupby('method')['orbital_period'].median()

## Iteration Over Groups:
for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))
    # useful for manual ops, often prefer "apply" functionality covered soon

## Dispatch Methods:
# Through Python class shenanigans, any method not explicitly implemented
# by GroupBy object class will be passed through and called on the groups
    # which, again, are Series/DF objects

# e.g. describe() method of DataFrames to perform set of aggs foreach group
planets.groupby('method')['year'].describe().unstack()


### More GroupBy: Aggegate, Filter, Transform, Apply
# setup new DataFrame:
rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                   columns = ['key', 'data1', 'data2'])
df

## Aggregate():
# aggregate() allows for strings & funcs in lists to allow multiple aggregates
df.groupby('key').aggregate(['min', np.median, max])
# aggregate() accepts dictionaries - map column names to desired operations:
df.groupby('key').aggregate({'data1': 'min', 
                             'data2': 'max'})

## Filtering:
# Filtering operation allows you to drop data based on group properties
def filter_func(x):
    return x ['data2'].std() > 4
df
df.groupby('key').std()
df.groupby('key').filter(filter_func)
    # filter_func returns boolean whether group passes filter. Group A drops


## Transformation:
# Aggregation must return a reduced version of data, while Transform
# can return some modified version of the full data to recombine
# output is same-shape as the input

# common use: center data by subtracting group-wise mean:
df.groupby('key').transform(lambda x: x - x.mean())


## The apply() method:
# apply() lets you apply an arbitrary function to the group results
def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x

df
df.groupby('key').apply(norm_by_data2)