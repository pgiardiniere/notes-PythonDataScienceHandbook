### Multiple Subplots
# To compare different views of data side-by-side, we can use subplots
# subplots are groups of smaller axes that can exist together in 1 figure

# we'll cover 4 routines for creating subplots in matplotlib:

# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

#########################
### Subplots by hand: plt.axes()
# the most basic method of creating an axes is plt.axes()
# defaults to creating a standard axes which fills the entire figure
# we can fill in the optional arg with a list of 4 nums in coordinate system:
    # [left, bottom, width, height]

# following example creates a second subset of axes in the 
# upper right hand corner of the first plot (see fig)

ax1 = plt.axes()    # standard axes
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

# equivalent in the object-oriented interface: 
    # fig.add_axes()
# example, 2 vertically stacked axes
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))


### plt.subplot() --- simple, singular grids of subplots
# aligned columns/rows of subplots are common, so Matplotlib has built-in
# methods for this use case

# lowest level: creates a single subplot within a grid
# plt.subplot() || fig.add_subplot() -- latter being object oriented version
# takes 3 ints as args. num rows, num cols, index of plot to be created
# (upper left to the bottom right)
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

# plt.subplots_adjust(), unsurprisingly, adjusts spacing between plots
# use OOP method below
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')


### plt.subplots() --- multiple grids of subplots (note the 's')
# when dealing with larger grids of subplots,
# especially when hiding x/y axis labels on inner plots, we use this method. 
# function specifically creates a full grid of subplots in a line,
# and returns in a NumPy array. Args are num rows and num cols
# optional arg: sharex / sharey

# example: create 2 x 3 grid of subplots, al
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
