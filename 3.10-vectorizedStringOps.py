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


## List of PD Methods similar to Python string methods:
    # many Pandas vectorized string methods are mirrored by overall
    # Python str methods

    # len()     lower()
    # ljust()   upper()
    # rjust()   find()
    # center()  rfind()
    # etc... see ch for full list. most are self-explanatory

# str.lower()       returns series of strings:
monte.str.lower()
# str.len()         returns length of string in Int:
monte.str.len()
# str.startswith()  returns Bool
monte.str.startswith('T')
# str.split()       returns list for each element
monte.str.split()


## Methods using regular expressions
    # these methods accept regular expressions, and mirror API conventions 
    # of Python's built-in "re" module

# Method        Description
# -------------------------
match()         # call re.match() on each element.      return Bool
extract()       # call re.match() on each element.      return match strs
findall()       # call re.findall() on each el.
replace()       # replace occurrences of pattern with other str
contains()      # call re.search() on each el.          return bool
count()         # count occurrences of pattern
split()         # equiv. to str.split(), but with regexs
rsplit()        # equiv. to str.rsplit, but with regexs
# -------------------------

# as always, regexs are quite powerful operators when dealing with strings:
# get first name from each element:
monte.str.extract('([A-Za-z]+)', expand=False)