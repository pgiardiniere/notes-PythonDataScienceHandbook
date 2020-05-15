# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data)

# Pass additional args to plt.hist() to customize output
plt.hist(data, bins=30, density=True, alpha=0.5, histtype='stepfilled',
         color='steelblue', edgecolor='none')

# This approach is more granular, and capable of multiple distributions
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

# To compute histogram without displaying it (count elements in given bin),
# use np.histogram().
counts, bin_edges = np.histogram(data, bins=5)
print(counts)


# Displaying & customizing 2D histogram plots:
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

# 1 - plt.hist2d()
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')
# as with plt.hist() above, can customize bins & plot output.

# 2 - np.histogram2d()
# plt.hist() is to np.histogram(),
# as plt.hist2d is to np.histogram2d
counts, xedges, yedges = np.histogram2d(x, y, bins=30)

# for dimensionality > 2, use np.histogramdd()


# Hexagonal binnings with plt.hexbin():

# By default, the 2d histogram creates a tesselation of squares across its axes
# Can specify hexagons instead if desired.
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')


# Kernel Density Estimation:

# KDE is a method of evaluating probability density function of a random var
# Said random variable can be multi-dimensional.
# KDE gets a dedicated chapter later.

# For now, demo a simple KDE implementation from scipy.stats
from scipy.stats import gaussian_kde

# Fit data to an array of size [Ndim, Nsamples].
data = np.vstack([x, y])
kde = gaussian_kde(data)

# Evaluate on a regular grid
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# Plot the result as img
plt.imshow(Z.reshape(Xgrid.shape), origin='lower', aspect='auto',
           extent=[-3.5, 3.5, -6, 6], cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")

# The output demonstrates the smoothing effect in action.
# There's a loss of fidelity, but gaussian_kde autofinds a near-optimal
# smoothing length on the input data.

# other KDE implementations in SciPy include:

# sklearn.neighbors.KernelDensity
# statsmodels.nonparametric.kernel_density.KDEMultivariate
