########################################
### Python's 'In' and 'Out' Objects
### iPython In/Out prompts are actually stored in a list and dictionary, respectively.

# In --- tracks all command inputs in order of execution
# Out -- { Input #, returned val }

# Get some In/Out. Then operate on prior output. Output reuse valuable when doing computationally taxing stuff
import math
math.sin(2)
math.cos(2)

Out[2] ** 2 + Out[3] ** 2

### Underscore Shortcuts & prior outputs
# Standard python shell has 1 shortcut for prior output, the variable '_'

## In iPython, extended as follows:
# _     = 1st prior output
# __    = 2nd prior output
# ___   = 3rd prior output

print(_)
print(__)
print(___)


### Suppressing Output --- add a semicolon to end of line.
# common use: suppressing output when plotting information (e.g. with Matplotlib)
math.sin(2) + math.cos(2);


########################################
### Related Magic Command - history
%history            # log of all In's
%history -n 1-4     # return In's n-m
%history?
