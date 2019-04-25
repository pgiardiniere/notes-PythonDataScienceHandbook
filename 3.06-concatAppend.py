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