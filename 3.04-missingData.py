# often, datasets of interest are missing key data
# or are otherwise not homogenous. Ch is dedicated to NaN, null, etc.

### Trade-offs in missing data conventions
# Many ways of nhandling missing data in table/DataFrame
# generally they fall into 2 categories:
    # Mask              which indicates missing vals globally
    # Sentinel Value    which indicates missing entry

# masking approach: mask may be an entirely seperate bool arr
# sentinel approach: sentinel val could be some data-specific convention
#                   (e.g.) missing int val  -9999 
#          or a more global convention (e.g. indicating missing float w/ NaN)

# they both have tradeoffs 
    # mask - allocate additional arrs, overhead in storage/computation
    # sent - extra logic in CPU/GPU arithmetic

##############################
### Missing data in Pandas
# PD is constrained by NP, which doesn't have built-in notion of NA vals
# for any non-floating-point data types

# Because of the additional data types Python supports (14 basic int types)
# it can't simply use R's model of adding a bit pattern to specify missing vals
# (also for smaller data types - e.g. 8 bit ints - sacrificing 1 bit means
#  it won't be able to accurrately represent the 'expected' range of nums)

# So, Pandas uses SENTINELS
# specifically, Python's "NaN" and "None" objects


## None: Pythonic missing data
# None is a Python singleton object used for missing data in Python code.
# Because "None" is a Python objects, it must be used in an array of dtype "object"

import numpy as np
import pandas as pd

vals1 = np.array([1, None, 3, 4])
vals1