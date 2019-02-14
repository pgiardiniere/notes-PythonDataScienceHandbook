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
        # is a bit dodgy when pressed for time

### WSL
# Despite the major performance hit for heavy I/O processes, I can definitely see
# this being useful for ad-hoc iPython stuff
# also iPython built-in has ls and stsuff..... maybe it'll 'just work' without
# further intervention. Guess we'll just start trying the magics and see what works
