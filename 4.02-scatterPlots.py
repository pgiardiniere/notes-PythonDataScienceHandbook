# Setup notebook:

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')


# Scatter Plots with plt.plot():
# same function we used for Line plots before
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black')

# Third argument represents type of symbol displayed on plot.
# Below are common shorthand symbols and their results:
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

# Character codes can be used together with line/color codes.
plt.plot(x, y, '-ok')

# additional keyword arguments to plt.plot(): (more lines/markers)
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)


# Scatter Plots with plt.scatter():

# plt.scatter() is more powerful than the simple plt.plot().
plt.scatter(x, y, marker='o')

# Main difference - plt.scatter() can alter/modify properties of single points.
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar()

# So in addition to basic scatterplots, we can now use size and color of points
# to convey information within the visualization itself. neat!

# this idea expanded in following ex: (iris data, 3 flower type measurements)
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
# so we can now easily visualize 4 dimensions of a real data set.


# Since plt.scatter() renders each point individually;
# plt.plot() is noticeably faster than plt.scatter() for large n.
