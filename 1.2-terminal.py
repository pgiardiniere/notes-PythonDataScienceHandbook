### iPython shortcuts 
# A more specific implementation of the GA linux terminal shortcuts.
    # These shortcuts are not in fact provided by IPython itself, 
    # but through its dependency on the GNU Readline library
# Only recording those which I am not already familiar with

### Navigation
# Ctrl-a    Cursor to beginning of line
# Ctrl-e    Cursor to end of line

### Text cutting / pasting(yank)
# Ctrl-k    Cut from cursor to line end
# Ctrl-u    Cut from cursor to line begin
# Ctrl-y    Yank (paste) text last pulled with either of the above 2

### Reverse-search history:
# Search goes beyond the current terminal session, into all cmdlets run.
# Ctrl-r

# iPython can list docstrings of functions defined in namespace.
def square(a):
    """Returns the square of a."""
    return a ** 2

square?
square??

# then, Ctrl-r <squa>. 
# Hit Ctrl-r again to cycle from most recent occurrence to furthest back
#   Pers note: seems like it has trouble going back to the start? i.e.
#   once you cycle to the first cmd run, it doesn't really respond to queries