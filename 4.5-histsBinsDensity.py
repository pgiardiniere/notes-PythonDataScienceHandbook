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
# 1st way:
# 2nd way: 