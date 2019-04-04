# before beginning, a note on Matplotlib plot object hierarchy
# Matplotlib aims to have a Python object representing everything that appears on the plot
# recall, figure is the bouding box within which plot elements appear
# each matplotlib object can act as a container of sub-objects,
# i.e. 'figure' can contain one or more 'axes', which then contain other objects representing plot contents

# tick marks being no exception. axes has attributes xaxis and yaxis, which have attributes that contain all the properties of the lines, ticks, and lables that make up the axes

### major and minor ticks
# major tick marks are usually bigger, minor tick marks are usually smaller
# by default, minor ticks aren't used generally. 
# Exception being Log plots:

import matplotlib.pyplot as plt
plt.style.use('classic')
# %matplotlib inline
import numpy as np

ax = plt.axes(xscale='log', yscale='log')
ax.grid()

# tick properties (locations and labels) can be cusomized with:
  # formatter
  # locator
# objects of each axis

print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())

print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())

# from the output, we see major and minor tick labels have their locations specified
# by a 'LogLocator' (makes sense, it's a logarithmic plot)

# as the minor ticks have a .NullFormatter, they do not have any labels.