### Controlling Exceptions - %xmode
# %xmode is shorthand for 'exception mode'
# With it we can control amt of info printed from exceptions

# see following code:
def func1(a, b):
    return a / b

def func2(x):
    a = x
    b = x - 1
    return func1(a,b)

func2(1)
# ... it will throw division by 0 error (at Default %xmode)

# %xmode has 3 options:
# Plain, Context, Verbose
# Plain     least output
# Default   middle output - default option
# Verbose   most ouput

# in iPython, run 
%xmode Plain
func2(1)
%xmode Verbose
func2(1)

##############################
### Debugging
# standard python interactive debugger is 'pdb' - Python Debugger (points for creativity there)
# the ipython interactive debugger is 'ipdb' - Interactive Python Debugger (again, props)
# refer to online docs if you want to learn ALL the ways of launching them. Here, only covered is 1 magic, the following...

### Convenient debugging with %debug
%debug
# call AFTER hitting an exception to open an interactive debugging prompt (ipdb) - right at point of exception
#
# can navigate thru stack with 'up', 'down'
# can print vals of variables & run other python commands in the ipdb session
# exit with 'quit', or 'exit'

# can also set debugging to run automatically on hitting exception with '%pdb on'

# try the following:
%xmode plain
%pdb on
func2(1)
ipdb > print(b)
ipdb > exit


### %run magic revisit
# if you want to debug an external script / file, we use %run -d
%run -d
# will run the file, but you use 'next' cmd to step through lines of code (rather than automatic execution)

############################################################
### Debugging commands: partial list
##############################
# Command 	    Description
# list 	        Show the current location in the file
# h(elp) 	    Show a list of commands, or find help on a specific command
# q(uit) 	    Quit the debugger and the program
# c(ontinue) 	Quit the debugger, continue in the program
# n(ext) 	    Go to the next step of the program
# <enter> 	    Repeat the previous command
# p(rint) 	    Print variables
# s(tep) 	    Step into a subroutine
# r(eturn) 	    Return out of a subroutine