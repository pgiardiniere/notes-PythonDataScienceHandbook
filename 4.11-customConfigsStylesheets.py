### matplotlib's default plot settings often subject of complaint
# Much should have changed in Matplotlib 2.0 (released in late 2016?)

# Matplotlib's runtime config options covered here
# newer stylesheets feature covered here

## plot customization by hand
# Generally until now we've done plot customizations on an individual basis. E.g.

import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

# %matplotlib inline

x = np.random.randn(1000)
plt.hist(x)

# can adjust by hand to make visually pleasing

# use a gray background
ax = plt.axes(axisbg='#E6E6E6')