"""To make comparisons of averages/data aggregates on disparate data sets,
use a Margin of Error.
"""

# Basic errorbars in Matplotlib

# Notebook setup:
# %matplotlib inline`
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)    # introduce randomness into sin plot

plt.errorbar(x, y, yerr=dy, fmt='.k')
# 'fmt' refers to format code controling appearance of lines and points
# it uses same syntax/shorthand seen in plt.plot before

# errorbar has options to fine-tune outputs
# e.g. make errorbars lighter than points
plt.errorbar(x, y, yerr=dy, fmt='o', color='black', 
             ecolor='lightgray', elinewidth=3, capsize=0)

# check errorbar docstring for more options


# Continuous errors:
"""Sometimes we want to show errorbars on continuous quantities.
matplotlib has no built-in function, but can combine primitives for it
"""
# e.g. Gaussian process regression w/ Scikit-Learn API
from sklearn.gaussian_process import GaussianProcess

# Define a model and draw data.
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# Compute the Gaussian process fit.
gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1, random_start=100)
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
dyfit = 2 * np.sqrt(MSE)    # 2*sigma ~ 95% confidence region

# To compute continuous error, we would not use plt.errorbar, as we don't want
# 1000 points with 1000 errorbars.

# Instead, use plt.fill_between() with a light color to visualize it
# Visualize the result:
plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')

plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color='gray', alpha=0.2)
plt.xlim(0, 10)

# For more options, see plt.fill_between() docstring.

# This is a tad low-level, so in the "Visualization With Seaborn" section,
# a dedicated API is discussed for visualizing this type of continuous errorbar
