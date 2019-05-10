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

# as always, regexs are quite powerful when dealing with strings:
# get first name from each element:
monte.str.extract('([A-Za-z]+)', expand=False)
monte.str.findall(r'^[^AEIOU].*[^aeiou]$')


## Miscellaneous methods:
# the following are other convenient operations for strings:
get()           # Index each element
slice()         # Slice each element
slice_replace() # replace slice in each element with passed value
join()          # Join strings in element of series with passed seperator
cat()           # String concatenation
repeat()        # repeat values
normalize()     # Return Unicode form of string
pad()           # Add whitespace to left|right|both sides of string
wrap()          # Split long strings into lines under a passed width
get_dummies()   # extract dummy variables as a dataframe


## Vectorized item access and slicing
get()
slice() 
# both are enablers for vectorized element access from each array
# example:
str.slice(0, 3)

df.str.slice(0, 3)  # these 2 statements are equivalent,
df.stf[0:3]         # 2nd being the Python standard indexing syntax

# get and slice allow access to elements of arrs returned by split()
# e.g. Pull last name::
monte.str.split().str.get(-1)


## Indicator Variables
# get_dummies() is useful when data has a column containing coded indicator
# Example dataset: contains following encoding:
    # A = "born in America" 
    # B = "born in the United Kingdom"
    # C = "likes cheese"
    # D = "likes spam"
full_monte = pd.DataFrame({'name': monte,
                           'info': ['B|C|D', 'B|D', 'A|C',
                                    'B|D', 'B|C', 'B|C|D']})
full_monte
full_monte['info'].str.get_dummies('|')

##############################
### Example: Recipe Database
# Data GET (gunzip cmdlet - Linux only. Win - use 7zip | ubuntuvm)
  # !curl -O http://openrecipes.s3.amazonaws.com/recipeitems-latest.json.gz
    # NOTE: per Issue 218 on the projects github page https://github.com/fictivekin/openrecipes/issues/218
    # the daily json exports are failing and will not be reinstated
    # must use link for the last known working export:
    # https://s3.amazonaws.com/openrecipes/20170107-061401-recipeitems.json.gz

  # !gunzip recipeitems-latest.json.gz
    # NOTE: ipython doesn't have gunzip module, so had to go boot up the old
    # ubuntuvm machine for curl to work. 

# Attempt to read in values:
try:
    recipes = pd.read_json('recipeitems-latest.json')
except ValueError as e:
    print("ValueError:", e)

# exception thrown mentions 'trailing data' - due to using file in which
# each line is itself valid json, but the file itself is not. Verify true:
with open('recipeitems-latest.json') as f:
    line = f.readline()
pd.read_json(line).shape

# read the entire file into a Python array
with open('recipeitems-latest.json', 'r') as f:
    ############ NOTE: initial import of the .json failed - troubleshoot later
    