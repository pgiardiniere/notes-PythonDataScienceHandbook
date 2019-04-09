### iPython Magic commands
# prefixed by either % or %% operators

### single % 
# named Line Magics
# operates on a single line of input

### double %%
# named Cell Magics
# operates on multiple lines of input

##############################
### Line Magics: examples

### Pasting stuff:
%paste
%cpaste

# used for pasting code into the interpreter
# e.g. copying this entire block causes an error
#   actually, I didn't have a problem with that... but %paste is still handy I guess?
def donothing(x):
    return x

%cpaste
# cpaste is handy if you want to paste more than one chunk to be executed in a batch
# enter '--' on a line alone to signal you are done pasting

### Running external code
%run

# used for running external files in the interpreter, AND keeping defined functions in the iPython namespace
# in your iPython kernel, cd to the dir this file is stored in.
%run <filename>.py
# then your defined functions in the file are available for use in the iPython session
   # This is useful for working interactively in a scratch space to quickly iterate on ideas in an existing file,
   # without accidentally screwing up the existing logic in-file.

# see more options with '%run?'

### Timing code exec
%timeit
%%timeit

# useful code to test each:
%timeit L = [n ** 2 for n in range(1000)]

%%timeit
L = []
for n in range(1000): 
    L.append(n ** 2)

# Fun note: the example above shows list comprehensions are faster than traditional method for this task

### Documentation & extras
%magic    # returns manual for EVERY magic - super long
%lsmagic  # returns all available magics
%timeit?  # returns manual for timeit     MUCH more useful than %magic for whatever you're using
