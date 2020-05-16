# Matplotlib is is a useful/popular visualization tool, but it isn't perfect
# valid complaints include:

#   Before 2.0, matplotlib defaults are OLD - based off MATLAB around 1999
#   Matplotlib API is low-level - often large amounts of boilerplate code
#   Matplotlib predates Pandas by over 10 years. Cannot use Dataframes

# Easy solution: Just use Seaborn

# Seaborn is an API on top of Matplotlib that offers better plot styles
# and color defaults, defines high-level funcs for common plots,
# and integrates with pd.dataframe objects.

# also note: Matplotlib is addresing as it has added plt.style tools
# covered earlier and is integrating more with Pandas.

# NOTE: This book makes reference to 'upcoming' Matplotlib 2.0 features.
#       from the matplotlib user guide, the current version is 3.2.1
#       https://matplotlib.org/users/index.html


# Seaborn vs Matplotlib:
# Differences demo'd on a simple random walk.

# Matplotlib classic plot style:
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd

# create random walk data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.linspace(rng.randn(500, 6), 0)
