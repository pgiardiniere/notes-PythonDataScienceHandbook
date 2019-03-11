### Visualization with Matplotlib
# initially released in 2003, it's starting to show it's age (and get replaced)
# it still has ubiquitous support though, and is widely popular to date

# "newer tools like ggplot and ggvis in R"
# ..."web visualization toolkits based on D3.js and HTML5 canvas"
    # lol and by just googling the name of the framework,
    # naturally there's a Medium post on just doing it yourself 
    # with modern CSS / native JS & virtual DOM manip instead of the framework
    # https://medium.com/@PepsRyuu/why-i-no-longer-use-d3-js-b8288f306c9a

### General Matplotlib Tips

## Importing shorthand:
import matplotlib as mpl            # for entire lib
import matplotlib.pyplot as plt     # for pyplot

## Setting styles:
plt.style.use('classic')

## using 'show()':
# depends on context of mpl use.
# 1) in a script
# 2) in iPython terminal
# 3) in iPython notebook

# Plotting from a script:
# in this context, plt.show() is very useful
# plt.show() starts an event loop, looks for currently active figure objects, and opens one or more
# interactive windows displaying the figure(s)

# example:
# ---------- file: myplot.py ----------
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
# if you run this script from command-line prompt, it will result in a window
# opening with the figure --- yay it works

####################
### Plotting from an iPython shell
# %matplotlib
### Plotting from an iPython notebook
# %matplotlib notebook  (interactive plots)
# %matplotlib inline    (static images of plots)

# generally will use inline. The following example will embed a png in the notebook
import numpy as np
x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')

## Saving figures to file with savefig()
fig.savefig('my_figure.png') 

# can confirm with an 'ls -lh my_figure.png' - new file in current working dir

# can also use python to display the contents of it using following:
from IPython.display import Image
Image('my_figure.png')

# savefig() infers filetype from the extension you give the filename
# Depending on backends installed, the file formats differ. Print list with:
fig.canvas.get_supported_filetypes()

####################
### MATLAB dual-interface --- state-based vs object-based

## State-based interface: MATLAB style
# Recall that Matplotlib originated as a Python alternative for current MATLAB users
# it's syntax often is more reflective of MATLAB than python for this reason

# ---------- MATLAB style example ----------
plt.figure()    # create plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1)    # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
# ---------- End example --------------------

# now we can discuss what 'stateful' means:
# it's keeping track of the current figure and axes, which are where all 'plt'
# commands are applied
# you can get reference to these using 
    # plt.gcf (get current figure) 
    # plt.gca (get current axes)

## Object-based interface: More power
# Instead of depending on 'active' figures/axes as above, 
# the plotting functions are methods of explicit Figure and Axes objects

# ---------- Object style example ----------
# first, create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.sublplots(2)

# Call plot() method on appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

# ---------- End example --------------------

# for simpler figures, it's a matter of preference which style to use
# for 'serious' or more complex work, object-oriented becomes a necessity

# book will switch between the 2 styles
# (in most cases in-text, only real diff is using plt.plot() or ax.plot())
