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
    # Divergent colormaps
    # Qualitative colormaps