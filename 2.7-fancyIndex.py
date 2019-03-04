### Fancy Indexing
# until now, we've used:
    # simple indexing   e.g. arr[0] or arr[:5]
    # boolean masks     e.g. arr[arr > 0]
# can also use fancy indexing, in which we pass arrays of indices in place of scalars
# allows for selecting more complicated subsets of array values

import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
x

# access 3 different elements
[x[3], x[7], x[2]]  # simple indexing
ind = [3, 7, 4]     
x[ind]              # fancy indexing

# with fancy indexing, the shape of retrun arr reflects shape of index arrays, not shape of arr being indexed
ind = np.array([[3, 7], 
                [4, 5]])
x[ind]

# fancy indexing also works in multi-dimensional arrs
X = np.arange(12).reshape((3, 4))
X

row = np.array([0, 1, 2])]