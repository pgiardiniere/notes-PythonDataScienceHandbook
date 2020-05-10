# setup notebook for plotting
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# create figure and axes
fig = plt.figure()
ax = plt.axes()

# The figure instance can be thought of as a container,
# with all the objects representing axes, graphics, text, and labels inside.

# The axes in instance ax are bouding boxes with ticks/labels,
# which go on to contain the plot elements of the visualization.

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))           # OO method

# Alternatively, we can use Matlab-style stateful call
plt.plot(x, np.sin(x))

# to create a single figure with multiple lines, call plot() again
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))


# Adjusting plots: Line colors and styles
# plt.plot() has additional parameters which we can specify with args

# 'color' keyword
# with none specified, Matplotlib auto-cycles through a set of defaults
plt.plot(x, np.sin(x - 0), color='blue')            # specify color by name
plt.plot(x, np.sin(x - 1), color='g')               # short code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')            # Grascale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')         # Hex code (RRGGBB, 00-FF)
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))   # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse')      # HTML color names

# 'linestyle' keyword
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')
# shorthand codes (identical output to above, respectively)
plt.plot(x, x + 4, linestyle='-')   # solid
plt.plot(x, x + 5, linestyle='--')  # dashed
plt.plot(x, x + 6, linestyle='-.')  # dashdot
plt.plot(x, x + 6, linestyle=':')   # dotted

# combine 'linestyle' and 'color' in single non-keyword arg
plt.plot(x, x + 0, '-g')            # solid green
plt.plot(x, x + 1, '--c')           # dashed cyan
plt.plot(x, x + 2, '-.k')           # dashdot black
plt.plot(x, x + 3, ':r')            # dotted red

# single character codes reflect standard abbreviations
# RGB  (red/green/blue)
# CMYK (Cyan/Magenta/Yellow/blacK)

# View the plt.plot() docstring for more available appearance customization.


# Adjusting plots: Axes limits

# most direct approach: xlim() and ylim()
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# can also display the graph in reverse by reversing your args
plt.plot(x, np.sin(x))
plt.xlim(10, 0)
plt.ylim(1.2, -1.2)

# related: plt.axis() can set x and y limits in one call. 
# pass it an iterable of form: [xmin, xmax, ymin, ymax]
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5])

# NOTE: plt.axis() != plt.axes()

# alternatively, can auto-tighten bounds like so:
plt.plot(x, np.sin(x))
plt.axis('tight')
# or ensure equal aspect ratio on-screen (so 1 unit in x == 1 unit in y) 
plt.plot(x, np.sin(x))
plt.axis('equal')

# view the docstring of plt.axis() for more available capabilities


# Labeling Plots:
# A brief look at titles, axis labels, simple legends.

# Title and Axis labels are simples, can set with these methods:
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Position, size, and style of these labels can be adjusted, check docs
# of individual funcs for info on how to do that.


# Simple Legends with plt.legend():
# Are useful when displaying multiple lines within a single set of axes

# Just specify 'label' keyword in your plt.plot(),
# and then call plt.legend() to display those labels
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), '-b', label='cos(x)')
plt.axis('equal')
plt.legend()
