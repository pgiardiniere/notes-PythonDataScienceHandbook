### iPython shell itself has access to many resources to assist coder

### Access documentation with ?
# all Python objects contina reference to the 'doc string';
# which by convention includes summary of object and how to use it

# One method of access for the len function:
help(len)

# The iPython shorthand for this is:
# len?  # Commented as this causes an error.

# Another example:
L = [1, 2, 3]
help(L.insert)    # L.insert?     
help(L) # L?   
# Note the difference in output! help(L) is very verbose

# ? also works for functions we define ourselves
def square(a):
    """Return the square of a."""
    return a ** 2
# Docstring declared on first line. By convention, you always use triple quote for docstrings

help(square)    # square?
# Note the difference in output! now, we see 'square?' as more descriptive

