# Up to now, focused on 1D and 2D data in Series/DataFrames (respectively)
# To go to 3D and 4D, PD provides Panel/Panel4D objects to natively handle

# In practice, often circumvent those objects and use hierarchal indexing
    # aka multi-indexing
# This allows for multiple index levels within a single index,
# thus getting more dimensions packed into the Series/DataFrames objects

# As an introduction to the practice, explore creation/use of "MultiIndex"

import pandas as pd
import numpy as np

##############################
### A Multiply Indexed Series
# How to represent 2D data in a 1D Series

## ---------- The wrong way ----------
# Use tuples for keys to make life bad:

index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
pop

# The one nice part, can index or slice on this multiple index:
pop[('California', 2010):('Texas', 2000)]

# BUT, if you want all vals for 2010, need to do some ugly/inefficient work:
pop[[i for i in pop.index if[1] == 2010]]



## ---------- The better way ----------
# Use Pandas Multindex object - essentially an extension of the tuple
# with pre-built operations to keep code clean as efficient as possible

index = pd.MultiIndex.from_tuples(index)
index