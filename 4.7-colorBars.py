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
    luminance = np.sqrt(np.dot(colorsp:, :3] ** 2, RGB_weight))
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