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