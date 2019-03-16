##############################
### Customizing Plot Legends
# Plot legends are very important for communicating meaning of your plots
# here we will focus on legend aesthetics

# as seen before, the simplest legends are created with the plt.legend() method
# which automatically creates a legend for any previously labeled plot elements

import matplotlib.pyplot as plt
plt.style.use('classic')
# %matplotlib inline
import numpy as np

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

# output observed is the simple legend we've dealt with thus far

## we can customize this legend's location and remove the frame as follows:
ax.legend(loc='upper left', frameon=False)
fig

# further, can customize number of columns with ncol
ax.legend(frameon=False, loc='lower center', ncol=2)
fig

# can use rounded box, and add shadowing, or transparency (alpha), as well as padding:
ax.legend(fancybox=True, framalpha=1, shadow=True, borderpad=1)
fig

# see additional legend options by checking plt.legend docstring