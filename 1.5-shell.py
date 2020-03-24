# Run shell commands with preceding !
!ls

# iPython namespace and shell commands
# you can assign iPython variables to shell cmd output like so:
directory = !ls
print(directory)    
type(directory)     # type returned is "IPython.utils.text.SList" > an iPython exclusive

# Automagics: list
# use the following magics WITHOUT leading '%' operator.
    # cd, ls, cp, cat, env, man, mkdir, more, mv, pwd, rm, rmdir

# Note:
!cd
%cd
# are doing two different things.

!cd     # will execute in a temporary subshell, net result is NO directory movement
%cd     # executes in current shell session.