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
# While simple aggregation can provide general idea of the whole dataset,
# often it's more insightful to aggregate conditionally on label/index

# this is implemented in "groupby" operation - so named after SQL command
# more popularly been described (by Hadley Wickham from R-land) as:
    # split, apply, combine

# see text for diagram, essentially 
#   Split - it breaks up DF by specified key into seperate entities
#   Apply - performs (aggregation) function on the new individual groups
#   Combine - merges results into an output array

# in reality, this computation generally runs in a single pass on the input
# where results are updated as it goes


# example:
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key','data'])
df
df.groupby('key')
# NOTE: return is NOT a DataFrame, but DataFrameGroupBy object
    # the DataFrameGroupBy object is a special view of the DataFrame, performs
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
planets.groupby('method')                               # DF GroupBy
planets.groupby('method')['orbital_period']             # Ser GroupBy
planets.groupby('method')['orbital_period'].median()    # aggregate Ser

## Iteration Over Groups:
for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))
    # useful for manual ops, but often prefer "apply" functionality seen later

## Dispatch Methods:
# Through Python class (dispatch tables?), any method not explicitly implemented
# by GroupBy object class will be passed through and called on the groups
planets.groupby('method')['year'].describe().unstack()  # describe() dispatch

##############################
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
    return x['data2'].std() > 4
df
df.groupby('key').std()
df.groupby('key').filter(filter_func)
    # filter_func returns boolean whether group passes filter. Group A drops


## Transformation:
# Aggregation must return a reduced version of data, while Transform
# returns some modified version of the entire dataset
    # i.e. Output table is same shape as the Input    (like math Transf.)

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
# per function name, we've normalized the dataset against data2 (sum of vals)

##############################
### Specifying the Split Key:
# in the examples above, we split the DataFrame on a single column name
# we can define groups in other ways, such as the following:

## A list, array, series, or index w/ the grouping keys::
# The key can be any series or list, so long as LEN matches DF LEN
L = [0, 1, 0, 1, 2, 0]
df
df.groupby(L).sum()

# equivalent to the groupby('key') syntax used, but more verbose. 
    # i.e. for demonstration purposes only. This is what is abstracted away normally
df.groupby(df['key']).sum()


## A dictionary or series mapping index values to group keys::
df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
df2
df2.groupby(mapping).sum()
df2.groupby(mapping).count()


## Any python function
# similar to mapping, can pass any random Python func that will 
# A) take input index value and B) output the group:
df2
df2.groupby(str.lower).mean()   # doesn't mean it's useful though lol


## a list of valid keys
# any of the preceding key choices can be COMBINED to group on multi-index:
df2.groupby([str.lower, mapping]).mean()


## Grouping Example:
# with the little additional knowledge of multi-index key mapping,
# can count discovered planets by method and by decade in easy form:
decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)