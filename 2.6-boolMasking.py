### Comparisons, Masks, and Boolean Logic
# Masking is useful when you want to extract, modify, count, or just
# manipulate values in an array based on some arbitrary criteria

# in Python, Boolean masking is usually most efficient way to achieve this

## example: counting rainy days
# load the daily rainfall statistics for Seattle in 2014:
import numpy as np
import pandas as pd

rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0   # 1/10mm -> inches conversion
inches.shape                # (365, 0) - daily measurement for 1 yr

## omitting matplotlib snippet,
## do not have environment set up for it yet
## wait until ch 4 to revisit

# histogram plot is good to see general shape of data
# but for specific questions (e.g. num rainy days, avg precip on them, etc.)
# we'll use masking to quickly answer

###################################
### Comparison Operators as ufuncs
#
#