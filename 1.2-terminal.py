### iPython shortcuts 
# A more specific implementation of the GA linux terminal shortcuts. Per the src:
    # These shortcuts are not in fact provided by IPython itself, 
    # but through its dependency on the GNU Readline library

# Only recording those most-helpful ones which I am not already familiar with

### Navigation
# Ctrl-a    Cursor to beginning of line
# Ctrl-e    Cursor to end of line

### Text cutting / pasting
# Ctrl-k    Cut from cursor to line end
# Ctrl-u    Cut from cursor to line begin
# Ctrl-y    Yank (paste) text last pulled with either of the above 2

### Reverse-search history:
# Ctrl-r
#
# This goes BEYOND the current terminal session, into all cmdlets run

# iPython in particular does a neat trick where it can pull previously defined
# functions in the namespace

#e.g. in a ipython session do:
def square(a):
    """Returns the square of a."""
    return a ** 2

# square?       # comment b/c not valid python
# square??

# then, Ctrl-r <squa>. 
# Hit Ctrl-r again to cycle from most recent occurrence to furthest back
#   Pers note: seems like it has trouble going back to the start? i.e.
#   once you cycle to the first cmd run, it doesn't really respond to queries