# a common visualization is that of geographic data
# Matplotlib's main tool is the Basemap toolkit
# lives in the mpl_toolkits namespace
# Basemap is kinda clunky, often simple visualization take long to create

# The more modern counterparts (non-python) would be leaflet or Google Maps API

# Still, it may be worth spending a few minutes to learn basic Basemap stuff

# installation:
# conda install basemap

# import:
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
# seems like it has been retired then... or replaced. Interesting

plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)

# go look further into whether Basemap has been replaced
# if so, determine what the replacement is
# don't spend any extra time implementing code for a deprecated lib