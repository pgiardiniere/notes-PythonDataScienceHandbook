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
# Because "None" is a Python object, must be in arr of data type "object"

import numpy as np
import pandas as pd

vals1 = np.array([1, None, 3, 4])
vals1       # dtype="object"

# per the given input data, the most fitting common type representation
# NP inferred is Python Objects

# unfortunately, this means we can't use vectorized ops, everything must be done at Python level
# see ex. for timing diff in "Object" vs "int" NP arr summing
for dtype in ['object', 'int']:
    print("dtype =", dtype)
    %timeit np.arange(1E6, dtype=dtype).sum()
    print()

# also, inclusion of Python objects means aggregations often produce errors
vals1.sum()     # type error. Undefined result summing int and "None"


## NaN: Numerical missing data
# NaN (acronym for "Not a Number") is a special float-point value
# recognized by all systems using standard IEEE float-point representation
vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype     # dtype="float64"

# ANY operation performed with a NaN float will be a new NaN
1 + np.nan
0 * np.nan

# so now, aggregates over vals are well defined but not always useful
vals2.sum(), vals2.min(), vals2.max()   # all NaN

# can use special aggregations to ignore missing values
np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)

# NOTE: there is NO NaN val for ints, strings, or other types


## "NaN" and "None" in Pandas
# Pandas is built to handle both interchangeable, converting b/w when needed
pd.Series([1, np.nan, 2, None])     # makes "None" "NaN"

# PD attempts to upcast type without available sentinel value if "NA" vals present
# example: Ints > Floats
x = pd.Series(range(2), dtype=int)
x               # dtype "int32"
x[0] = None     # converted to "NaN"
x               # dtype "float64"

# ---------------------------
# Pandas upcasting conventions:
# Typeclass     Conversion when storing NAs     NA sentinel value

# floating      No change                       np.nan
# object        No change                       None or np.nan
# integer       Cast to float64                 np.nan
# boolean       Cast to object                  None or np.nan

# ---------------------------

# NOTE: in Pandas, strings are always stored with "object" dtype


##############################
### Operating on Null Values
# 