### Introducing Pandas String Operations
# Before, covered NP / PD generalized arithmetic operations. A refresher:
import numpy as np
x = np.array([2, 3, 5, 7, 11, 13])
x * 2

# Vectorization of operations simplifies the syntax (not concerned with LENs)
# NP lacks this for arrays of strings though, forced to construct loop:
data = ['peter', 'Paul', 'MARY', 'gUIDO']
[s.capitalize() for s in data]
# As such, it fails for any arrs with NAs
data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
[s.capitalize() for s in data]

# Pandas has vectorized string operations though
import pandas as pd
names = pd.Series(data)
names
names.str.capitalize()  # tab-complete str<> to list ALL vectorized str methods

##############################
### Tables of Pandas String Methods
# setup new data Series:
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])

# many Pandas vectorized string methods are mirrored by overall Python str methods
## List of PD Methods similar to Python string methods:
# len()
# ljust()
# rjust()
#
#
#
#
#
#
