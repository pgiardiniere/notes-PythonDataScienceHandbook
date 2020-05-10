# General Matplotlib Tips

# Importing shorthand:
import matplotlib as mpl
import matplotlib.pyplot as plt

# Setting styles:
plt.style.use('classic')

# Three contexts for using mpl:
# 1) in a script
# 2) in iPython terminal
# 3) in iPython notebook


# 1) Plotting from a script (i.e. some "name.py"):
# In this context, we use plt.show()

# plt.show() starts an event loop, looks for currently active figure objects,
# and opens one or more interactive windows to display the active figure(s).

# For example running this very file '4.00-introMatplotlib.py'.
import numpy as np
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()

# If you run this script via command line through a Python interpreter which is
# installed to the OS running your desktop environment / windowing system;

# Then show() will pop up a graph in a new window with the relevant plot.


# 2) Plot from an iPython shell using the magic %matplotlib


# 3) Plot from an iPython notebook using either magic...
# %matplotlib notebook  for interactive plots.
# %matplotlib inline    for static plots.

# Generally the book uses inline plots.
# NOTE: Port the following example to a .ipynb file.
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')


# Save figures to file with savefig().
fig.savefig('my_figure.png')

# Can use python to display the contents of it like so:
from IPython.display import Image
Image('my_figure.png')

# savefig() infers filetype from the extension you give the filename
# Depending on backends installed, the file formats differ. Print list with:
fig.canvas.get_supported_filetypes()


# Matlab dual-interface: state-based vs object-based

# 1) State-based interface: Matlab-like

# Recall that Matplotlib originated as a Python alt for Matlab junkies;
# its syntax often is more reflective of Matlab than python for this reason

# ---------- state-based example ----------
plt.figure()            # create plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1)    # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
# ---------- End example --------------------


# Stateful just means state-tracking.
# I.e. plt has a notion of 'current' figure/axes, referenced by the following:
# plt.gcf()     get current figure
# plt.gca()     get current axes


# 2) Object-based interface: more Pythonic

# Instead of depending on 'active' figures/axes as above,
# the plotting functions are methods of explicit Figure and Axes objects

# ---------- Object-based example ----------
# first, create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.sublplots(2)

# Call plot() method on appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

# ---------- End example --------------------

# for simpler figures, it's a matter of preference which style to use
# for more complex work, object-oriented is a necessity

# book will switch between the 2 styles
# (in most cases in-text, only real diff is using plt.plot() or ax.plot())
