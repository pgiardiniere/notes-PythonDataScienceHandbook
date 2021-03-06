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

# As above, would need to 'conda install basemap' for this.
# I'm not really interested in geographic maps at this time.
# I'll revisit this later.
