# Access documentation with '?':
# All Python objects contain reference to their respecive docstrings.
# The docstring is simply a brief description of what the object/method does.
len?
help(len)   # standard Python interface

L = [1, 2, 3]
L.insert?     
L?   

# The ? operator also works for functions we define ourselves.
def square(a):
    """Return the square of a."""   # Always create docstring on 1st line with """.
    return a ** 2

help(square)
square?

# Accessing Source Code with '??':
# In addition to the docstring, ?? yields source code if available.
square??

# Objects without source code are usually implemented in C or another language.
len??

# Tab autocompletion work with wildcard character (*).
*Warning?     # print all objects in namespace ending with Warning.
str.*find*?   # print all str methods containing 'find' anywhere in name.
