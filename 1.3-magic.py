### iPython Magic commands
# prefixed by either % or %% operators(right term?)

### single % 
# named Line Magics
# operates on a single line of input

### double %%
# named Cell Magics
# operates on multiple lines of input

##############################
### Line Magics: examples

### Pasting stuff:
#  %paste
#  %cpaste

# used for pasting code into the interpreter
# e.g. copying this entire block causes an error
#   actually, I didn't have a problem with that... but %paste is still handy I guess?
def donothing(x):
   return x
#
# %cpaste
# cpaste is handy if you want to paste more than one chunk to be executed in a batch
# enter '--' on a line alone to signal you are done pasting

### Running external code
# %run

# used for running external files in the interpreter, AND keeping defined functions in the iPython namespace
# in your iPython kernel, cd (or import os and use that, if you want to be slower!) to the dir this file is stored in.
# I have created a file called 'mySquare.py' 
# then use the magic!

# %run mySquare.py

# then your defined functions in the file are available for use in the iPython session
# square(4)

# see more options with '%run?'

### Timing code exec
# %timeit

##############################
### Cell Magics: examples