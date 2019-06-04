# numexpr is a package which allows for direct-access to C-speed operations without 
# intermediate object generation. Pandas methods eval() and query() are dependent on it

# this chapter covers the pandas eval() and query() operations, as per usual,
# the basics, good rules-of-thumb, and coventions generally followed.


### Motivating query() and eval() --- Compound Expressions (and numexpr demonstration):
# Recall Vectorized operations in NP and PD:
import numpy as np
rng = np.random.RandomState(42)
x = rng.rand(1000000)
y = rng.rand(1000000)
%timeit x + y           # recall anaconda/ipython magics

%timeit np.fromiter((xi + yi for xi, yi in zip(x, y)), dtype=x.dtype, count=len(x))

# however, our vectorized ops are less efficient for compound expressions:
mask = (x > 0.5) & (y < 0.5)
# this is because NP evals each subexpression seperately, roughly, doing this...
tmp1 = (x > 0.5)
tmp2 = (y < 0.5)
mask = tmp1 & tmp2
# ... allocating our intermediate steps in memory, introducing the same inefficiency as before

import numexpr
mask_numexpr = numexpr.evaluate('(x > 0.5) & (y < 0.5)')
np.allclose(mask, mask_numexpr)


### pandas.eval() for Efficient Operations
# eval() in PD uses string expressions to compute operations using DataFrames, efficiently.
import pandas as pd
nrows, ncols = 100000, 100
rng = np.random.RandomState(42)
df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows, ncols))
                      for i in range(4))

%timeit df1 + df2 + df3 + df4

%timeit pd.eval('df1 + df2 + df3 + df4')


### Operations supported by pd.eval()
# demonstration of supported ops as of PD v0.16 in pd.eval()
df1, df2, df3, df4, df5 = (pd.Dataframe(rng.randint(0, 1000, (100, 3)))
                           for i in range(5))

## Arithmetic Operators
# All arithmetic operators are supported
result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
np.allclose(result1, result2)

## Comparison Operators
# all comparison operators, including chained expressions:
result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
result2 = pd.eval('df1 < df2 <= df3 != df4')
np.allclose(result1, result2)

## Bitwise Operators
# supports the & and | bitwise operators
result1 = (df1 < 0.5) & (df2 < 0.5) | (df3 < df4)
result2 = pd.eval('(df1 < 0.5) & (df2 < 0.5) | (df3 < df4)')
np.allclose(result1, result2)

# also supports the use of literal "and" and "or" in Bool expressions
result3 = pd.eval('(df1 < 0.5) and (df2 < 0.5) or (df3 < df4)')
np.allclose(result1, result3)

## Other Attributes and Indices
# pd.eval() supports access to:
    # object attributes     via     obj.attr    syntax
    # index  attributes     via     obj[index]  syntax
result1 = df2.T[0] + df3.iloc[1]
result2 = pd.eval('df2.T[0] + df3.iloc[1]')
np.allclose(result1, result2)

## Other Operations
# otherwise not mentioned ops [function calls, conditional statements, loops]
# are all NOT implemented within pd.eval() - you would need full numexpr lib

### DataFrame.eval() for Column-Wise Operations
# pd.eval() is top-level, DFs have their own eval() which is similar
# benefit: columns can be referred to by name
df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
df.head()
