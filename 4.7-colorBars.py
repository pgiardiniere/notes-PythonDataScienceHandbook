#########################
### Customizing Colorbars
# Plot legends identify discrete labels of discrete points
# labeled colorbars identify continuous labels based on color of points, lines, regions

# can view the additional color-coded stuff in link provided:
# https://github.com/jakevdp/PythonDataScienceHandbook

## set up notebook:
import matplotlib.pyplot as plt
plt.style.use('classic')

# %matplotlib inline
import numpy as np

# as seen before, basic colorbar:
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])
plt.imshow(I)
plt.colorbar()

# now we can go further and customize

# colormap can be specified using 'cmap' arg to the plt function creating it
plt.imshow(I, cmap='gray')
# see all available colormaps in the plt.cm namespace with tab completion
# plt.cm.<TAB>

## Choosing the colormap
# several articles linked as this topic goes deeper than one chapter, of course
# 3 different kinds of colormaps discussed here:

    # Sequential colormaps
        # made up of one continuous sequence of colors
        # e.g. binary, viridis
    # Divergent colormaps
        # usually contain 2 distinct colors, positive and negative devs from mean
        # e.g. RdBu, PuOr
    # Qualitative colormaps
        # mix colors with no particular sequence
        # e.g. rainbow, jet

# jet actually used to be default for matplotlib, despite the fact that 
# qualitative colormaps are generally the least-helpful scheme due to non-uniform progression

# converting jet colorbar to black and white demonstrates this concept:
from matplotlib.colors import LinearSegmentedColormap

def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived grayscale Luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)

def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize=(6, 2), 
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])

view_colormap('jet')

# from output, can see bright white stripes in the grayscale image.
# note how they are present even in full-color
# these brighter sections naturally draw the eye, which defeats the purpose
# of using color-scale for data representation (unless you're intentionally
# obscuring meaning)

# "viridis" became the replacement for jet
# by plotting we can tell difference immediately: even brightness (in color and grayscale)
view_colormap('viridis')

# for a rainbow-style scheme on continuous data, can use the "cubehelix" colormap in place of
view_colormap('cubehelix')

# for other applications (e.g. positive-negative deviations from a mean)
# dual-color colorbars like RdBu are useful
# --- note that grayscale translation of these dual-color schemes lose +/- info
# keeps magnitude only, not direction
view_colormap('RdBu')

# to view additional colormaps, view the plt.cm submodule
# or refer to the Seaborn documentation

###################################
### Color limits and extensions
# As seen, Matplotlib allows for colorbar customizations.
# Colorbar is an instance of plt.Axes, so all the axes and tick formatting already used are applicable

# for instance, can set color limits and indicate out-of-bounds vals with traingular arrow
# accomplished using the "extend" property
# see the following example for a use case:

# ----------------------------------------

# make noise in 1% of the image pixels
speckles = (np.random.random(I.shape) < 0.01)
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

plt.figure(figsize=(10, 3.5))

plt.sublplot(1, 2, 1)
plt.imshow(I, cmap='RdBu')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(I, cmap='RdBu')
plt.colorbar(extend='both')
plt.clim(-1, 1)

# ----------------------------------------

# per example, 
# in the left panel, default color limits incorporate the added noise, ruining the visualization
# in the right panel, the visualization limits disregard the noise, displaying a useful graph

##############################
### Discrete color bars
# colormaps by default are continuous, but can be made to represent discrete values
# plt.cm.get_cmap() function, passing name of suitable colormap and desire bin num
plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1)

## example: handwritten digits
# we'll use some data included in scikit-learn of hand written digits data

# download the data and visualize several example images with plt.imshow():

# ----------------------------------------

# Load images of the digits 0 through 5 and visualize several of them
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)

fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])


# ----------------------------------------