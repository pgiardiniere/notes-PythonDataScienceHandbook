### Controlling Exceptions - %xmode
# %xmode is shorthand for 'exception mode'. Controls verbosity of exception output

def func1(a, b):
    return a / b

def func2(x):
    a = x
    b = x - 1
    return func1(a,b)

# func2(1) throws a 0 division error

%xmode Plain
func2(1)
%xmode Default
func2(1)
%xmode Verbose
func2(1)


### Debugging
#  pdb  python interactive debugger  - Python Debugger
# ipdb ipython interactive debugger  - Interactive Python Debugger

# refer to online docs if you want to learn other ways of launching debug sessions.
%debug
# call AFTER hitting an exception to open an interactive debugging prompt (ipdb) - right at point of exception

# can navigate thru stack with up/down arrow keys
# can print vals of variables & run other python commands in the ipdb session
# exit with 'exit' or 'quit'

# can also set debugging to run automatically on hitting exception with '%pdb on'

# try the following:
%xmode plain
%pdb on
func2(1)
ipdb > print(b)
ipdb > exit


# Debug external files:
%run -d 
# Executes in interactive mode __from the beginning__.  use next' to step through each line.


### Debugging commands: partial list
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