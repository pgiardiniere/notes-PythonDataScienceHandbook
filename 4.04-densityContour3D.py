# To display 3 dimensional data in 2 dimensional plane, 
# can use contours / color coded regions 
# plt.contour() / plt.contourf()    # f=filled
# plt.imshow    # show images

## set up notebook:
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

##############################
### Contour plots for 3d visualization:
# for function: $z = f(x, y)$
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

# creating a plt.contour graph takes 3 args, grid of x, grid of y, grid of z
    # x, y represent positions on the plot (per usual)
    # z represents contour level

# to prepare the data, we use np.meshgrid to form the 2d grid from disparate 1d arrays x, y
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

## No color (line-only) contour plot:
plt.contour(X, Y, Z, colors='black')

    # note from resulting graph: when single color is used: 
        # negative vals are dashed lines
        # positive vals are solid lines
    
    # drawback: not super obvious what it's conveying

## Color contour plot:
plt.contour(X, Y, Z, 20, cmap='RdGy')
    
    # note from resulting graph: cmap = color map
        # RdGy = Red-Gray, works well for centered data (i.e. 0+-)
        # others viewable by tab completion of plt.cm - plt.cm.<TAB>

    # more detail in this graph also due to specifying 20 equal-space intervals within data range 

## Color contour, FILLED plot:
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()

    # Better, but still rough lines where areas are bordered

## Color contour, Filled, Smoothed plot:
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image')

# at time of book's writing:
    # plt.imshow() doesn't accept x and y grids, so manually specify extents
    # plt.imshow() origin defaults to upper left corner (actually kind of makes sense to me from an imp standpoint). Manually specify 'lower' 
    # plt.imshow() axis default adjusts axis aspect ratio to match input data. set aspect='image' to force x, y equality

### Combination contour/image plot:
# use imshow() with alpha (transperancy) set
# on top of it, draw a basic contour plot --- with in-line labels! plt.clabel()
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.5)
plt.colorbar()