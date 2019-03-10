# setup notebook for plotting
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# create figure and axes
fig = plt.figure()
ax = plt.axes()

# the figure (instance of plt.Figure) can be thought of as a container 
# with all the objects representing  axes, graphics, text, and labels within it

# the axes (instance of plt.Axes) are bouding boxes with ticks/labels, eventually
# containing the plot elements that makeup the visualization