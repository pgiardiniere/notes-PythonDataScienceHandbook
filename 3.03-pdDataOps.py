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