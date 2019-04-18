# Recall material on NP Universal Functions from Ch2
# PD builds on ufuncs functionality a few ways:

# first, for unary operations (negation / trig funcs), ufuncs preserve
# index and column labels in the output

# second, for binary operations (addition / multiplication) PD aligns
# indices when passing objects to the ufunc

# the automatic handling of these makes error-prone NP ufuncs, PD-bulletproof
# additionally, there are operations when crossing Series/DataFrame structs

##############################
### Ufuncs: Index Preservation
# As PD designed to work with NP, NP Ufuncs work on PD Series/DataFrame
import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
ser = pd.Series(rnd.randint(0, 10, 4))
ser

df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])
df

# applying a NP ufunc on either of these objects, 
# result with be another PD object with the indeces preserved:
np.exp(ser)

np.sin(df * np.pi / 4)

##############################
### UFuncs: Index Alignment
## Index Alignment in Series

# suppose we are combining two differnce data sources, want top 3 us states
# by area, and top 3 by population
area = pd.Series({'Alaska': 1723337, 'Texas': 695662, 
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')

# now, divide to compute population density
population / area
# we see the resulting array contains the Union of indeces of two input arrs
    # we can verify that using standard Python set arithmetic on the indices
area.index | population.index

# any item for which one or the other doesn't have an entry is marked "NaN"
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A + B

# if NaN vals isn't desired, fill val can be modified using object methods
# in place of the operators (with attribute "fill_value" used)
A.add(B, fill_value=0)


## Index Alignment in DataFrame
# similar alignment on both columns AND indices when using DataFrames:
A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list('AB'))
A
B = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=list('BAC'))
B
A + B
# note that indices are aligned correctly irrespective of order in objects,
# and indices in the result are sorted

# as before, can use object method with "fill_value" attribute to replace NaN
# here, we fill with the mean of all values stored in "A" instead of 0
fill = A.stack().mean()
A.add(B, fill_value=fill)


# Table: Python operators and equivalent PD Object methods:
#   +   add()
#   -   sub(), subtract()
#   *   mul(), multiply() 
#   /   truediv(), div(), divide()
#   //  floordiv()
#   %   mod()
#   **  pow()


##############################
### Ufuncs: Operations Between DataFrame and Series
# index & col alignment is similar when crossing DF and Series

# Remember: as DF is to Series in Pandas
#           1D arr is to 2d Arr in NumPy

# Find difference between a two-dimensional array and one of its rows:
A = rng.randint(10, size=(3, 4))
A
A - A[0]

# Per NP broadcasting rules, subtraction b/w 2D arr and row is done row-wise

# In Pandas, convention similarly operates row-wise by default:
df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]

# to operate column-wise, use object methods and specify "axis" keywork
df.subtract(df['R'], axis=0)

# as before, indices are automatically aligned between 2 elements:
halfrow = df.iloc[0, ::2]
halfrow
df - halfrow

# as mentioned, automatic preservation + alignment of indices/cols means
# operations on data in Pandas will maintain data context
# more seamlessly than NP arrs