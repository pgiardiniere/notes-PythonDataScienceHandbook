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
