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

# by specifying sharex/sharey, we inner labels are auto-removed.
# because returned in NumPy array, can use standard array index notation 

# axes are in a 2D array, indexed by [row, column]
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')

# plt.subplot() indexes at 1
# plt.subplots() indexes at 0   hurrah


#########################
### plt.GridSpec() for more complicated arrangements
# plt.GridSpec() object does not create a plot by itself,
# it is an interface recognized by the plt.subplot() cmd

# example: gridspec for a grid of two rows and three columns
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)

# then we can specify subplot location/extents with typical Python slicing syntax
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])

# flexible grid alignment has many applications.
# author likes it when doing multi-axes histogram plots such as below:
# ----------begin----------------------------------------

# create some normally distributed data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# set up axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled', orientation='vertical', color='gray')
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled', orientation='horizontal', color='gray')
y_hist.invert_xaxis()

# -----------end-----------------------------------------