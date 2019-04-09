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

#########################
### Hiding ticks or labels
# can easily hide ticks/labels using
# plt.NullLocator() and plt.NullFormatter()

ax = plt.axes()
ax.plot(np.random.rand(50))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formattor(plt.NullFormattor())

# X axis, removed labels but kept ticks
# Y axis, removed labels and ticks
    # really, we removed the Ticks from Y axis, which means there cannot be labels for null ticks

# useful example: images of faces, something commonly used in supervised
# machine learning problems

fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)

# Get some face data from scikit-learn
from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces().images

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")

# notice each image has its own axes, with no locatorsm, as the tick values 
# (i.e. pixel numbers) don't convey any info in our visualization

#########################
### Reducing or increasing the number of ticks
# small subplots get crowded labels w/ default settings, e.g.:
fix, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# numbers with near overlap = bad
# use plt.MaxNLocator() to specify the max num ticks displayed
# Matplotlib will use other internal logic to choose locations given max

# for every axis, set the x and y major locator
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
fig

#########################
### fancy tick formats
# matplotlibs default formatting is iight
# consider following plot of sine/cosine:

# Plot sine/cosine curves
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw=3, label='Sine')
ax.plot(x, np.cos(x), lw=3, label='Cosine')

# set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
ax.axis('equal')
ax.set_xlim(0, 3 * np.pi)
