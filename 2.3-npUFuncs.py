### Computation on NumPy Arrays: Universal Functions
# Using NP arrays in the traditional loop-style manner, is VERY slow
# Vectorized operations are preferred, and generally implemented in ufuncs

# here's a traditional loop-based approach to operating on arr values to demonstrate
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
# %timeit compute_reciprocals(values)

# now, consider a case with a much bigger array of values:
big_arr = np.random.randint(1, 100, size=1000000)
# %timeit compute_reciprocals(big_array)

# note that both ops are way slower than they should be

##############################
### UFuncs introduction
# Interface for statically typed, compiled routines are known as vectorized operations
# can be achieved by performing an operation on the array, which then is applied to each el
# Advantage of vectorized approach is it pushes loop into the compiled layer, rather than being interpreted piecewise

# sample 1: ufunc operation b/w Scalar type and Array
compute_reciprocals(big_arr)
1.0 / big_arr
# %timeit (1.0 / big_array)

# sample 2: ufunc operation b/w Array type and Array
np.arange(5) / np.arange(1, 6)

# sample 3: ufunc operation on Multi-dimensional array
x = np.arange(9).reshape((3,3))
2 ** x

# the Pythonic way :: replace loops with vectorized expressions like the above when possible


##############################
### Exploring additional UFuncs 
# Two types, Unary ufuncs and Binary ufuncs

## Array Arithmetic
# NumPy ufuncs use simple arithmetic operators
x = np.arange(4)
x
x + 5
x - 5
x * 2
x / 2
x // 2  # floor division 
-x
x ** 2
x % 2

# can also string together operations, standard operations order respected
-(0.5*x + 1) ** 2

# Arithmetic operators in this context are wrappers for specific NP funcs. I.e. + evaluates to add()
np.add(x, 2)    # long form
x + 2           # wrapper equivalent


# We also have Boolean and Bitwise operators translated to NP ufuncs. Covered in "2.6-boolMasking.py"


## Absolute Value
# np plays nice with python standard library absolute val function abs()
x = np.array([-2, -1, 0, 1, 2])
abs(x)
# np has its own ufunc np.absolute() --- also callable as np.abs()
np.absolute(x)
np.abs(x)

x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])  # complex nums example
abs(x)
np.abs(x)


## Trigonometric ufuncs
# we can start by defining an array of angles
theta = np.linspace(0, np.pi, 3)
theta
np.sin(theta)
np.cos(theta)
np.tan(theta)
# and inverse trig funcs
x = [-1, 0, 1]
np.arcsin(x)
np.arccos(x)
np.arctan(x)

# side-note: recall that doubles get 15 decimal digits of precision.
#            to get less messy output, must round.
#            NON-Ufunc:  np.round(np.sin(theta), decimals=15)  # rounds to 15th (dec precision limit)
#                ufunc:  np.rint( np.sin(theta))              # rounds to 0 th decimal


## Exponents and logarithms
import math;
x = np.array([1, 2, 3])

math.e ** x
np.exp(x)

2 ** x
np.exp2(x)

3 ** x
np.power(3, x)

x = [1, 2, 4, 10]           # NOTE: x is a list --> cannot use ufunc operators like ** or +

np.log(x)                   # natural logarithm
np.log2(x)                  # base 2 logarithm
np.log10(x)                 # base 10 logarithm

# related exp/log funcs, good for precision on small input vals
x = [0, .001, .01, .1]
np.exp(x)
np.expm1(x)             # Calculates ``exp(x) - 1``  
np.log(x)
np.log1p(x)             # Calculates ``log(1 + x)``

## Specialized ufuncs
# some additional examples: hyperbolic trig funcs, bitwise arithmetic, comparison operators,
# radian > degree conversions, rounding/remainders, etc. See NumPy ufunc docs

# another source of ufuncs :: scipy.special 
from scipy import special

# Gamma functions (generalized factorials) & related funcs
x = [1, 5, 10]
special.gamma(x)    # gamma
special.gammaln(x)  # ln|gamma
special.beta(x, 2)  # beta

# Error function (integral of Gaussian), complement, and inverse
x = np.array([0, 0.3, 0.7, 1.0])
special.erf(x)
special.erfc(x)
special.erfinv(x)

###################################
### Advanced UFunc Features
# 3 topics: Out, Aggregates, Outer Products

## Specifying output: using "out"
# We can directly specify mem location to store result of a calculation using "out"
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)

# Can also utilize this with array views
y = np.zeros(10)
y = np.power(2, x, out=y[::2])
y[::2] = 2 ** x

# the above 2 lines do the same thing, but 2nd line requires creation of temp array and full copy
# so generally, specifying 'out' is just saying "store result in this memory location" in imperative style
# means efficiency savings.


## Aggregates
# With reduce() method, we can repeatedly execute a given operation to all elements of the array
# returning a single scalar value
x = np.arange(1, 6)
np.add.reduce(x)
np.multiply.reduce(x)

# with accumulate() method, we reduce() while storing all intermediate outputs in array
np.add.accumulate(x)
np.multiply.accumulate(x)

# note that there are dedicated NumPy funcs for these particular cases
# np.sum, np.prod, np.cumsum, np.cumprod - respectively


## Outer products
# Any ufunc can compute the output of all pairs of two different inputs with outer()
x = np.arange(1, 6)
np.multiply.outer(x, x)

# ufunc.at() and ufunc.reduceat() will be covered later in Fancy Indexing, and build on this idea

# additional ufuncs available in the NumPy/SciPy docs