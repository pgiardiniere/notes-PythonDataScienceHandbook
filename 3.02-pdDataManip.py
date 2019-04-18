# Recall CH 2, discussed methods to access/set/modify values in NP arrays
# indexing, slicing, masking, fancy indexing, and combinations of them
# arr[2, 1]   arr[:, 1:5]       arr[0, [1,5]]

##############################
### Data Selection in Series
# As discussed, PD Series objects are similar to 1d NP arrays, 
# and Python dicts


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
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data
# uses explicit indices - INCLUSIVE
data[1]
# uses implicit indices - EXCLUSIVE
data[1:3]

# so, explicit index when indexing
# and implicit index when slicing

# because of this confusion, PD provides special "indexer" attributes
# they explicitly expose indexing schemes. NOT methods, just attributes

# "loc"  allows indexing and slicing that always refs EXPLICIT index
data.loc[1]
data.loc[1:3]

# "iloc" allows indexing and slicing that always refs IMPLICIT index
data.iloc[1]
data.iloc[1:3]

# "ix" is hybrid, and for "Series"    objects is = to standard []-based indexing
# it makes more sense w/  "DataFrame" objects

# generally speaking, "explicit is better than implicit" in Python
# since "loc" and "iloc" explicitly denote their nature, can help iron out confusion

##############################
### Data Selection in DataFrame
# As discussed, PD DataFrame objects are similar to 2d NP arrays, 
# and like dictionary of Series structures sharing the same index


## DataFrame as a Dictionary
# recreate the example of populations and states:
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois':149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data

# the individual Series that make up the columns of the DataFrame 
# can be accessed via dict-style indexing of col name
data['area']

# equivalently, can use attribute-style access with col-names as strings
data.area

# proof of equivalence:
data.area is data['area']   # evals to "True"

# though the shorthand attr. is useful, does not work for all cases
# if col names are NOT strings, or conflict with DataFrame methods, it fails
# e.g. data.pop --- DataFrame has a pop() method 
data.pop is data['pop']     # evals to "False"

# like "Series" objects discussed earlier, dict-style syntax 
# can be used to modify the object. e.g. Add a new column:
data['density'] = data['pop'] / data['area']
data


## DataFrame as two-dimensional array
# Can view DataFrame as enhanced 2d arr, many familiar arr-like methods/routines

# examine raw underlying data using 'values' attribute:
data.values

# transpose full DataFrame to swap rows and columns:
data.T

# indexing is Dictionary-style, not NP-array-style. 
    # Passing a single  index  to an array    accesses a row:
data.values[0]
    # Passing a single "index" to a DataFrame accesses a column:
data['area']

# to get array-style indexing, use another convention
# it's same ones used earlier:
# loc, iloc, ix

# using iloc indexer, can index the underlying array as if an NP arr (i.e. implicit style)
    # DataFrame index and column labels are maintained in result:
data.iloc[:3, :2]

# using loc indexer, can index the underlying array 9n array-like style w/ explicit index/col names
    # DataFrame index and column labels are maintained in result:
data.loc[:'Illinois', :'pop']

# using ix indexer, can get a hybrid of the two approaches:
data.ix[:3, :'pop']

# NOTE: ix is still subject to the implicit/explicit confusion in prior note section

# using these 3 indexers, can use the familiar NP-style data access patterns
# loc indexer, for example, can combine masking & fancy indexing:
data.loc[data.density > 100, ['pop', 'density']]

# any indexing conventions may be used to set/modify vals like NP
data.iloc[0, 2] = 90
data

# (author recommends practicing to gain fluency/memorize these shorthand techniques)


## Additional indexing conventions
# A few sticking points which can be useful

# 'indexing' refers to Columns, 
# 'slicing' refers to rows
data['Florida':'Illinois']  # slice
data[1:3]                   # slice by row number, rather than index

# direct masking operations are also interpreted row-wise (not col-wise)
data[data.density > 100]

# these 2 conventions are syntactically similar to NP arrs, and quite useful,
# but are at odds with PD conventions