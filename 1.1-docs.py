### iPython shell itself has access to many resources to assist coder

### Access documentation with ?
# all Python objects contain reference to the 'doc string';
# which by convention includes summary of object and how to use it

# One method of access for the len function:
help(len)
# An iPython extension filling same purpose is:
len?
# Slight difference in formatting of return

# Another example:
L = [1, 2, 3]
help(L.insert)    
L.insert?     

help(L) 
L?   
# Note the difference in output! help(L) is very verbose

# ? also works for functions we define ourselves
def square(a):
    """Return the square of a."""
    return a ** 2
# Docstring declared on first line. By convention, you always use triple quote for docstrings

help(square)
square?

### Accessing Source Code with ??
# again, works for self-defined functions, e.g. square below
square??
# compared directly with square?, we see really the only diff is src code inclusion

# some functions do not display source code, this would be stuff compiled in C or other extension langs
len??
# most built-ins are this way

### Tab autocomplete
# mostly self-explanatory - quite handy

# tab-completion with wildcard character (*)
*Warning?     # prints all objects in namespace ending with Warning
str.*find*?   # prints all str methods containing 'find' anywhere in name
