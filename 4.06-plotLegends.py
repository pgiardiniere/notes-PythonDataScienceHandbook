
# Customizing Plot Legends

# As seen before, the simplest legends are created with plt.legend(),
# which creates a legend for any labeled plot elements.

# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

# Output figure is the plot with simple legend we've dealt with thus far.
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

# Customize this legend's location and remove the frame.
ax.legend(loc='upper left', frameon=False)
fig

# Customize number of columns with ncol.
ax.legend(frameon=False, loc='lower center', ncol=2)
fig

# Use rounded box, add shadowing, add no transparency (alpha=1), specify pad.
ax.legend(fancybox=True, framalpha=1, shadow=True, borderpad=1)
fig


# Choosing elements for the legend:

# As we have seen, legend includes all labeled els by default.
# plt.plot() can create multiple lines, returning a list of created instances.
# By passing lines along with desired labels to plt.legend() to ID only those.

y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)
plt.legend(lines[:2], ['first', 'second'])

# In practice, you would probably prefer creating legend labels as below,
# applying labels to the plot els to display in the legend at initialization.
plt.plot(x, y[:, 0], label='first')
plt.plot(x, y[:, 1], label='second')
plt.plot(x, y[:, 2:])
plt.legend(framealpha=1, frameon=True)


# Legend for Size of Points:

# In the following example, the size of a point on our plot is meaningful.

# By plotting empty lists, we create labled plot objects which are picked
# up by the legend, revealing the visual scale.

# We must do this as the legend will always reference an object on the plot,
# but we don't want the scale reference on the actual plot.

import pandas as pd
cities = pd.read_csv('data/california_cities.csv')
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# Scatter the points, using size and color, but no label.
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# Create legend: plot empty lists with desired area, then label and add.
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')
plt.title('California Cities: Area and Population');


# Multiple Legends:

# Sometimes it makes sends to add multiple legends to the same axes,
# but plt.legend() only allows for 1.

# To work around this, we must create a new legend artist ourselves,
# then use the ax.add_artist() method to add the second artist to the plot.

fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')

ax.axis('equal')

# Create the first legend as usual.
ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)

# Create the second legend and add the artist
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'],
             loc='lower right', frameon=False)
ax.add_artist(leg)
