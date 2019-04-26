# next few chapters will deal with aggregating data from different sources
# as such, will cover a few tools to help combine these datasets

# here we'll cover concatenation of Series/DataFrame objects with pd.concat
import pandas as pd
import numpy as np

# define a DF constructor for re-use within examples:
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

# example DataFrame:
make_df('ABC', range(3))

# also create a class to allow display of multiple DataFrames side-by-side
# it utilized the _repr_html_ method, iPython uses it to implement rich obj disp
class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)


##############################
### Recall: Concatenation of NumPy arrays
# Concatenation of Series/DF is similar to NP arrs, 
# done via np.concatenate function discussed in "basics of NP arrays" ch
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])

# can also concatenate along a specified axis for multi-dimensional data:
x = [[1, 2],
     [3, 4]]
np.concatenate([x, x], axis=1)


##############################
### Now: Concatenation of Pandas objects
# pd.concat() executes similar syntax, and contains additional options:

# Signature in Pandas v0.18
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)

# Again, simplest use-case is concatenation of just Series of DataFrame objs
# Series:
ser1 = pd.Series(['A', 'B', "C"], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])
# DataFrame:
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
display('df1', 'df2', 'pd.concat([df1, df2])')  # as thought, no display produced

# By default, DataFrames concatenate row-wise (axis=0)
# can specify axis as well:
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
display('df3', 'df4', "pd.concat([df3, df4], axis='col')")  # or axis=1


### Duplicate Indices:
# unlike np.concatenate, pd.concat preserves indices, even if duplicates
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index           # make duplicate indices
display ('x', 'y', 'pd.concat([x, y])')

# Can choose to handle such duplicates a few ways:
# --------------------------------------------------
## Option 1: Catch repeats as an error
# T/F verify indices in result do not overlap, specify "verify_integrity" flag
# Set to True, it will throw an error if indices overlap
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)

## Option 2: Ignore the index
# If the index itself doesn't matter, specify "ignore_index" flag
# Set to True, it will create new integer index for resulting Series:
display('x', 'y', 'pd.concat([x, y], ignore_index=True)')

## option 3: Add MultiIndex keys
# To make a hierarchally indexed Series/DataFrame, specify "keys" option 
# Must add desired keys as args.    This circumvents duplicate indices by adding layer of abstraction
display('x', 'y', "pd.concat([x, y], keys=['x', 'y'])")
# --------------------------------------------------


### Concatenation with Joins
# In examples above, concatenated DFs with shared col names
# If col names are disparate/varied, pd.concat includes methods to join

# create DF with SOME shared columns:
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
display('df5', 'df6', 'pd.concat([df5, df6]')

