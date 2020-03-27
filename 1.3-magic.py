# iPython Magic Commands:
# Line Magics --- %
# Cell Magics --- %%

# Pasting Things:
%paste
%cpaste

def donothing(x):   # paste this
    return x

%cpaste
# cpaste is made when pasting multiple discrete chunks to be executed in a batch.
# enter '--' on a empty line to quit paste mode.


# Running External Code:
# Use %run to run external files in the interpreter.
# Defined functions persist in your current iPython namespace.
%run
%run <filename>.py
%run?

# Timing Code Execution
# Fun note: the examples below show list comprehensions performance advantage.
%timeit     # Line-magic
%%timeit    # Cell-magic

%timeit L = [n ** 2 for n in range(1000)]

%%timeit
L = []
for n in range(1000): 
    L.append(n ** 2)

# Documentation and More
%magic    # returns the general magic manpages
%lsmagic  # returns all available magics
%timeit?  # returns manual for timeit
