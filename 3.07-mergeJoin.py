# Again, Pandas has high-performance, in-memory joins/merge ops
# it's main interface is pd.merge()     (also, Ser/DF join())

# NOTE: I removed the display() function from this set of notes
#       it wasn't working in standalone iPython, and it obfuscated notes

import pandas as pd
import numpy as np

### Relational Algebra
# The behavior of pd.merge() is a subset of Relational Algebra:
    # def: a set of formal rules for manipulating relational data
    # it forms the conceptual foundation of database operations

##############################
### Categories of Joins
# pd.merge() function implements a number of types of joins:
    #  one-to-one
    # many-to-one
    # many-to-many
# type of join performed is inferred based on the input data


## One-to-one joins:
# join where the Key column in both objects contain exactly the same entries
# behavior: precise match.
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2)
df3
# NOTE: as seen, precise index is discarded in merge, unless you are merging
# specifically using the index (e.g. left_index, right_index keywords used)


## Many-to-one joins:
# join where the Key column in one object contains duplicate entries
# behavior: match all cols, duplicate required data in the resulting table
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
df3
df4
pd.merge(df3, df4)


## Many-to-many joins:
# join where key column in both objects contains duplicate entries
# behavior: match all cols, duplicate required data in the resulting table
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting', 
                              'Engineering', 'Engineering', 'HR', 'HR'],
                              'skills': ['math', 'spreadsheets', 'coding', 
                                         'linux', 'spreadsheets', 'organization']})
pd.merge(df1, df5)

##############################
### Specification of the Merge Key
# default behavior of pd.merge() --- look for matching col names, use as Key
# if col names do not match, must handle:

## The 'on' keyword
# Can explicitly specify the name of the key column using "on" keyword
# can feed either 1 column name or a list of names
print(df1, "\n\n", df2)
pd.merge(df1, df2, on='employee')


## The "left_on" and "right_on" keywords
# May wish to merge two datasets with different column names,
# e.g. same data item is labeled "name" in one dataset and "employee" in another

# Here, "left_on" and "right_on" specify the disparate names:
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
print(df1, '\n\n', df3)
pd.merge(df1, df3, left_on='employee', right_on='name')

# Note the output has a redundant column: can use DataFrame's drop() method
pd.merge(df1, df3, left_on='employee', right_on='name').drop('name', axis=1)


## The "left_index" and "right_index" keywords
# rather than column merge, may make sense to merge on index
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')

# the left_index/right_index keywords act as flags, set to True to merge on index
pd.merge(df1a, df2a, left_index=True, right_index=True)

# for convenience, DataFrames implement join() method,
# and this merge defaults to joining on indices:
df1a.join(df2a)


# To MIX indices and columns, combine the following:
    # left_index    with    right_on
    # right_index   with    left_on
pd.merge(df1a, df3, left_index=True, right_on='name')

# also, these options work for multiple indices/cols, see the documentation

##############################
### Specifying Set Arithmetic for Joins
# So far, have glossed over the set arithmetic used in joins; using default
# This becomes important when values appear in one dataset but not other
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
                    columns=['name', 'drink'])
pd.merge(df6, df7)

# in the prior merge, only Mary is displayed. This is default:
# default behavior: Intersection    aka Inner Join
    # specified by "how" keyword
    # options: 'inner', 'outer', 'left', 'right'

pd.merge(df6, df7, how='inner')     # arg 'inner' is Intersection. Same output
pd.merge(df6, df7, how='outer')     # arg 'outer' is Union. Missing vals=NAs
pd.merge(df6, df7, how='left')


##############################
### Overlapping Column Names: the Suffixes Keyword
# May have 2 input DataFrames with conflicting column names:
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3, 1, 4, 2]})
pd.merge(df8, df9, on='name')

# As output would have conflicting (used) column names, merge automatically
# appends suffix _x and _y

# can specify custom suffixes with the "suffixes" keyword:
pd.merge(df8, df9, on='name', suffixes=['_L', '_R'])


### Example: US States Data
# Following are shell commands to download the data
# !curl -O https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv
# !curl -O https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-areas.csv
# !curl -O https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-abbrevs.csv

# use read_csv() to pull it in:
pop = pd.read_csv('data/state-population.csv')
areas = pd.read_csv('data/state-areas.csv')
abbrevs = pd.read_csv('data/state-abbrevs.csv')

pop.head()
areas.head()
abbrevs.head()
# Or -- print(pop.head(),'\n\n', areas.head(),'\n\n', abbrevs.head())

# Given this, lets rank all US states and territores by 2010 pop density
# Begin with many-to-one merge that gives full sate name within population DF

# merge based on state/region cols of pop, abbreviateion of abbrevs. how=outer
merged = pd.merge(pop, abbrevs, how='outer',
                  left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', 1)     # drop duplicate information
merged.head()

# Since we used the inclusive outer-join, should check for mismatches
# display True/False if field contains >0 NaN vals
merged.isnull().any()
# from the output, "population" and "state" contain null vals. 

# from "population", display head of null entries:
merged[merged['population'].isnull()].head()
    # appears only Puerto Rico before 2000 has nulls 
    # likely these are just not in original data, so no further inv. req'd
    
# from "state", null entries mean there was no corresponding entry in "abbrevs" key
# display regions without the match:
merged.loc[merged['state'].isnull(), 'state/region'].unique()
    # from the output, seems that again Puerto Rico has discrepency, not matched to US as whole
    # fix: fill in appropriate entries

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()
# now returns "False" - fixed the issue


# Now that the data has been scrubbed, can merge the result with "areas" data
# Join on 'state' column for both:
final = pd.merge(merged, areas, on='state', how='left')
final.head()

# check for nulls:
final.isnull().any()

# again, we see nulls, look to see which regions were ignored:
final['state'][final['area (sq. mi)'].isnull()].unique()

# from return, we see area of the entire United States is not present
# since it isn't relevant to ranking of the individual states, we'll drop it
final.dropna(inplace=True)
final.head()

# now the final array is scrubbed to, can go about calculating pop density
# query() --- to filter population statistics:
    # data corresponding to year 2010
    # Total poulations (i.e. NOT those under 18)
data2010 = final.query("year == 2010 & ages == 'total'")
data2010.head()

# now we can get ensity and display in order
# first, re-index data on state, then compute result:
data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']

density.sort_values(ascending=False, inplace=True)
density.head()
density.tail()      # display end of list