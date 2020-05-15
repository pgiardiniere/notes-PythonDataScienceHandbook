# Can use contours / color coded regions to display higher dimensional data
# plt.contour() / plt.contourf()    # trailing 'f' denotes 'filled'
# plt.imshow()

# set up notebook:
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np


# Contour plots for 3d visualization:
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


# creating a plt.contour graph takes 3 args, which are grids of x, y, z
# (x, y) represent positions on the plot
# z represents contour level

# Use np.meshgrid() to form the 2d grid from 1d arrays x, y
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# No color (line-only) contour plot:
plt.contour(X, Y, Z, colors='black')

# note from resulting graph: when single color is used:
# negative vals are dashed lines
# positive vals are solid lines

# drawback: not super obvious what it's conveying


# Color contour plot:
plt.contour(X, Y, Z, 20, cmap='RdGy')

# note from resulting graph: cmap = color map
# RdGy = Red-Gray, works well for centered data (i.e. 0+-)
# others viewable by tab completion of plt.cm - plt.cm.<TAB>

# '20' kwarg denotes we want 20 equally-spaced lines drawn, hence more lines

# Color contour, FILLED plot:
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()
# Better, but still rough lines where areas are bordered


# Color contour, Filled, Smoothed plot:
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image')

# at time of book's writing:
# plt.imshow() doesn't accept x and y grids, so must specify extents.
# plt.imshow() origin defaults to upper left corner.
# plt.imshow() adjusts axis aspect ratio to match input range.
#              Must set aspect='image' to force x, y equality


# Combination contour/image plot:
# use imshow() with alpha (transperancy) set
# on top of it, draw a basic contour plot --- with in-line labels! plt.clabel()
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.5)
plt.colorbar()
