# setup notebook for plotting
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# create figure and axes
fig = plt.figure()
ax = plt.axes()

# the figure (instance of plt.Figure) can be thought of as a container 
# with all the objects representing  axes, graphics, text, and labels within it

# the axes (instance of plt.Axes) are bouding boxes with ticks/labels, eventually
# containing the plot elements that makeup the visualization

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))           # OO method

# alternatively, can use pylab intrrface for MATLAB stateful-style
plt.plot(x, np.sin(x))

# to create a single figure with multiple lines, call plot() again
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

#########################
### Adjusting plots: Line colors and styles
# plt.plot() has additional parameters which we can specify with args

## 'color' keyword
# with none specified, Matplotlib auto-cycles through a set of defaults
plt.plot(x, np.sin(x - 0), color='blue')            # specify color by name
plt.plot(x, np.sin(x - 1), color='g')               # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')            # Grascale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')         # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))   # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse')      # HTML color names (all supported)

## 'linestyle' keyword
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')
# shorthand codes (identical output to above, respectively)
plt.plot(x, x + 4, linestyle='-')   # solid
plt.plot(x, x + 5, linestyle='--')  # dashed
plt.plot(x, x + 6, linestyle='-.')  # dashdot
plt.plot(x, x + 6, linestyle=':')   # dotted

## combine 'linestyle' and 'color' in single non-keyword arg
plt.plot(x, x + 0, '-g')            # solid green
plt.plot(x, x + 1, '--c')           # dashed cyan
plt.plot(x, x + 2, '-.k')           # dashdot black
plt.plot(x, x + 3, ':r')            # dotted red

# single character codes reflect standard abbreviations
# RGB  (red/green/blue)
# CMYK (Cyan/Magenta/Yellow/blacK)