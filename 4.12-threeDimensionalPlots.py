# matplotlib was initially designed with 2d plots in mind
# around 1.0 release, some 3d plotting utils were built on top of it
# result is convenient (if limited) set of tools for 3d data visualizations

# must import the mplot3d toolkit, included in main Matplotlib install

from mpl_tookits import mplot3d

# once imported, a 3ds axes can be created using the keyword:
# projection='3d' to normal axes creation routine

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

