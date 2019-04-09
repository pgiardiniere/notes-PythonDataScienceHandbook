### iPython and shell commands
# iPython has integration with Bash shell (presumably DOS too)
# chapter assumes iPython is running in a Unix-like env

########################################
### Personal notes: Dev environment setup (again)

### Docker Container
# I can set up a new docker ubuntu container which has a data volume 
# connected to the C:\Users\<user>\Workspaces directory
    # Don't bother installing git, running it 'natively' on win w/ git bash
    # containers have problems w/ git when VS Code exit causes dirty shutdown
        # Second point - don't use container within the VS Code terminal.
        # It's a bit fragile as remembering to exit the shell seperate from the app

### WSL
# Despite the major performance hit for heavy I/O processes, I can definitely see
# this being useful for ad-hoc iPython stuff
# also iPython built-in has ls and stsuff..... maybe it'll 'just work' without
# further intervention. Guess we'll just start trying the magics and see what works

########################################
### Begin material 
# no changes to dev env
# will record whether funcs work or not

### Run shell commands with preceding !
!dir # on windows shell

### iPython namespace and shell cmds
# you can assign iPython variables to shell cmd output like so:
directory = !dir
# then get it's contents and type with these --- note: type returned is "IPython.utils.text.SList" > an iPython exclusive
print(directory)
type(directory)

### Automagics: list
# Can use automagics without the preceding % (so long as 'automagic' is on, which it is by default)
# The following are some (many of which I've already been using):
    # cd, ls, cp, cat, env, man, mkdir, more, mv, pwd, rm, rmdir

########################################
# so far, the only noticeable difference on a windows-based shell is the difference in output of ls, which is annoying
# will have to determine if it's worth it to make signifacnt changes to my environment based on use - hunch is 'eh maybe'