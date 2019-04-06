# Matplotlibis is a useful and popular visualization tool, but it isn't perfect
# valid complaints include:

## Before 2.0, matplotlib defaults are OLD - based off MATLAB around 1999
## Matplotlib API is low-level - often large amounts of boilerplate code
## Matplotlib predates Pandas by over 10 years. Cannot natively use Dataframe.S

# An easy way to cirumvent?
# Use 'Seaborn' (as seen already)

# Seaborn provides an API on top of Matplotlib tha offers better choices for plot styles
# and color defaults, defines high-level funcs for common plot types, and integrates with Pandas 'DataFram S' type

# also note: Matplotlib is addresing as it has added plt.style tools already discussed
# and is integrating Pandas data better. 

# 2.0 release (will) include --- personal note: figure out when 2.0 was released and record date here)
# new default stylesheet to improve on current staus quo

#########################
### Seaborn vs Matplotlib
# here is a simple random-walk plot in Matplotlib, using classic plot formatting/colors

## imports
import matplotlib.pyplot as plt
plt.style.use('clasic')
# %matplotlib inline
import numpy as np
import pandas as pd

## create random walk data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.linspace(rng.randn(500, 6), 0)