##############################
### Customizing Plot Legends
# Plot legends are very important for communicating meaning of your plots
# here we will focus on legend aesthetics

# as seen before, the simplest legends are created with the plt.legend() method
# which automatically creates a legend for any previously labeled plot elements

import matplotlib.pyplot as plt
plt.style.use('classic')
# %matplotlib inline
import numpy as np

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

# output observed is the simple legend we've dealt with thus far

## we can customize this legend's location and remove the frame as follows:
ax.legend(loc='upper left', frameon=False)
fig

# further, can customize number of columns with ncol
ax.legend(frameon=False, loc='lower center', ncol=2)
fig

# can use rounded box, and add shadowing, or transparency (alpha), as well as padding:
ax.legend(fancybox=True, framalpha=1, shadow=True, borderpad=1)
fig

# see additional legend options by checking plt.legend docstring

###################################
### Choosing elements for the legend
# as we have seen, legend includes all labeled elems by default
# plt.plot() command is able to create multiple lines, returns a list of created line instances
# passing any given line to plt.legend() tells it which to identify, and it's label:

y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)
# lines is a list of plt.Line2D instances
plt.legend(lines[:2], ['first', 'second'])

# in practice, it is author's opinion that is clearer to use the first method,
# i.e. apply labels to the plot elements you want to show in the legend in advance
plt.plot(x, y[:, 0], label='first')
plt.plot(x, y[:, 1], label='second')
plt.plot(x, y[:, 2:])
plt.legend(framalpha=1, framon=True)

# I would agree, second example shows the labels at plt.plot() point,
# so of course plt.legend() would pick those up and not the third

### Legend for Size of Points
# sometimes the defaults are not sufficient for a visualization
    # HAH! HAHA! THE AUTHOR MADE A TYPO
    # "For example, perhaps you're be using the size of points to mark..."
    # he's human like me after all lel

# following is an example of using size of points to indicate populations
# legend should specify scale of sizes at points, accomplished by plotting labeled data with no entries

# ------------- example begin -----------------
import pandas as pd
cities = pd.read_csv('data/california_cities.csv')

# extract data we're analyzing
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# Scatter the points, using size and color, but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# create legend & plot: plotting empty lists with desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')
plt.title('California Cities: Area and Population')

# ------------- example end -----------------

# the legend will always reference an object that is on the plot
# in this case, the objects were not on the plot (the gray circles)
# so we plot empty lists to achieve them

# by plotting empty lists, we create labled plot objects which are picked
# up by the legend, now it reveals the scale visual factor

#########################
### Multiple legends
# sometimes it makes sends to add multiple legends to the same axes
# plt.legend() ONLY allows for 1 however

# to work around it, we must create a new legend artist from scratch,
# then use the ax.add_artist() method to add the second artist to the plot

# ------------------------------
fig, ax = plt.subplots()

lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')

ax.axis('equal')

# specify the lines and labels of the first legend
ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)

# create the second legend and add the artist manually
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'], loc='lower right', frameon=False)
ax.add_artist(leg)
# ------------------------------

