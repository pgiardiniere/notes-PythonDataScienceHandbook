########################################
### Python's 'In' and 'Out' Objects
# iPython In/Out prompts are actually stored in a list and dictionary, respectively.

# Get some In/Out history built:
import math
math.sin(2)
math.cos(2)
## Note: recall you can cd to dir and %run this file, rather than manually import math from iPython
##       also, the two other lines are run in-file, not on iPython prompt, so they do not add to either the In or Out aggregators

### In
# 'In' is a list, tracks all commands in order

### Out
# 'Out' is a dictionary, key = In #, value = output
# Only values which have an output are tracked, hence necessity of dict for key/value maping
# Also note: the Output of 'Out' is not tracked, for pretty obvious reasons

# Out can be used to operate on outputs of prior cmds. Say you ran the import, sin, and cos fn's in a new iPython session
# the following will add the squares of the sin/cos:
Out[2] ** 2 + Out[3] ** 2

########################################
### Underscore Shortcuts & prior outputs
# Standard python shell has 1 shortcut for prior output, the variable '_'


## In iPython, extended as follows:
# _     = 1st prior output
# __    = 2nd prior output
# ___   = 3rd prior output

## e.g.
print(_)
print(__)
print(___)
# again, calling this variable does not iterate/get recorded in the output, for obvious reasons

########################################
### Suppressing Output
# to suppress output, add a semicolon to end of line. Like the following example:
math.sin(2) + math.cos(2);
    # result is computed silently, output displayed neither on screen or in 'Out' dict
    # recall also that semicolons are only used in .py files to executing multiple statements on one line, i.e. rarely.

# common use: suppressing output when plotting information (e.g. with Matplotlib)

########################################
### Related Magic Command - history
%history
# pulls multiple prevoius Inputs at once. Example:
%history -n 1-4
# return more use cases by looking up the documentation with
%history?
