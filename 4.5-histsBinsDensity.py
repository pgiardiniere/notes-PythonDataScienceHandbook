####################
### Histograms
## Displaying & customizing 1D histogram plots ---

# make data, plot histogram:
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data)

# can pass additional args to plt.hist() to customize output
plt.hist(data, bins=30, normed=True, alpha=0.5, histtype='stepfilled',
         color='steelblue', edgecolor='none')

# this approach is both more granular, and capable of displaying multiple distributions
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

# to compute histogram without displaying it (i.e. just count num points in given bin)
# use np.histogram()
counts, bin_edges = np.histogram(data, bins=5)
print(counts)

## Displaying & customizing 2D histogram plots ---
# setup data before beginning
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

# 1st way: plt.hist2d()
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

# as with plt.hist() above, can customize plot/binning. See docstring for details

# 2nd way: np.histogram2d()
# as plt.hist() is to np.histogram() :: plt.hist2d is to np.histogram2d
counts, xedges, yedges = np.histogram2d(x, y, bins=30)

# for dimensions beyond 2d, use np.histogramdd()

#########################
### Hexagonal binnings with plt.hexbin()
# by default, the 2d histogram creates a tesselation of squares across its axes
# instead we can do hexagons
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')

### Kernel Density Estimation
# another method of evaluating densities across multiple dimensions
    # (this does have a dedicated chapter a bit later)
# one quick-simple KDE impl. exists in scipy.stats
from scipy.stats import gaussian_kde

# fit an array of size [Ndim, Nsamples]
data = np.vstack([x, y])
kde = gaussian_kde(data)

# evaluate on a regular grid
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# Plot the result as img
plt.imshow(Z.reshape(Xgrid.shape), origin='lower', aspect='auto',
           extent=[-3.5, 3.5, -6, 6]), cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")

# from the output, we can observe the smoothing effect in action
# we obviously lose some detail for this, gaussian_kde uses a rule-of-thumb to find near-optimal smoothing length
# given the input data used.

# other KDE implementations in SciPy include:
    # sklearn.neighbors.KernelDensity
    # statsmodels.nonparametric.kernel_density.KDEMultivariate