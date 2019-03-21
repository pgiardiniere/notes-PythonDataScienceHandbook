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