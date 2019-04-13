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
%timeit compute_reciprocals(values)

# now, consider a case with a much bigger array of values:
big_array = np.random.randint(1, 100, size=1000000)
%timeit compute_reciprocals(big_array)

# check the vals in iPython, note that it's orders of magnitude slower than it should be in both cases

##############################
### UFuncs introduction
# Interface for statically typed, compiled routines are known as vectorized operations
# can be achieved by performing an operation on the array, which then is applied to each el
# Advantage of vectorized approach is it pushes loop into the compiled layer under NumPy, for faster exec

# sample 1: ufunc operation b/w Scalar type and Array
compute_reciprocals(values)
1.0 / values
%timeit (1.0 / big_array)

# sample 2: ufunc operation b/w Array type and Array
np.arange(5) / np.arange(1, 6)

# sample 3: ufunc operation on Multi-dimensional array
x = np.arange(9).reshape((3,3))
2 ** x

# as a general rule, vectorized computations are magnitudes faster than Python loops
# try to replace loops with vectorized expressions like the above when possible


##############################
### Exploring additional UFuncs 
# Two types, Unary ufuncs and Binary ufuncs

## Array Arithmetic
# NumPy ufuncs are nice, they make use of Python's native arithmetic operators
# addition, subtraction, multiplication, division, etc.
x = np.arange(4)
x
x + 5
x - 5
x * 2
x / 2
x // 2  # floor division 
-x      # unary negation
x ** 2  # exponentiation
x % 2   # modulus (remainder)

# can also string together operations, standard operations order respected
-(0.5*x + 1) ** 2

# the arithmetic operations are convenient wrappers for specific NP funcs, + relates to add
np.add(x, 2)    # long form
x + 2           # wrapper equivalent

# can find a partial list of the long-form uFunc arithmetic utilies used above in the chapter text


## Absolute Value
# python has built-in abs value func, np does recognize it
x = np.array([-2, -1, 0, 1, 2])
abs(x)
# np also has its own function np.absolute() --- also callable as np.abs()
np.absolute(x)
np.abs(x)
# ufun also handles complex data, where abs val returns magnitude
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
np.abs(x)


## Trigonometric functions
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

## Exponents and logarithms
x = [1, 2, 3]
x
np.exp(x)       # basic exp yields natural exponential: 2.718
np.exp2(x)      
np.power(3, x)

x = [1, 2, 4, 10]
x
np.log(x)       # natural logarithm
np.log2(x)      # base 2 logarithm
np.log10(x)     # base 10 logarithm
# specialized log funcs, useful for precision over small inputs
x = [0, .001, .01, .1]
np.expm1(x)
np.log1p(x)

## Specialized ufuncs
# some additional examples: hyperbolic trig funcs, bitwise arithmetic, comparison operators,
# radian > degree conversions, rounding/remainders, etc. See all in NumPy docs

# another source (with demonstrations): 
# scipy.special
from scipy import special

# Gamma functions (generalized factorials) & related funcs
x = [1, 5, 10]
special.gamma(x)    # gamma
special.gammaln(x)  # ln|gamma      not sure why pylint IDs as errors - runs fine
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
y
# Can also utilize this with array views
y = np.zeros(10)
y = np.power(2, x, out=y[::2])
y
# compare speed between statement 2 and below, for a larger op, to see savings of not having temp array creation & copy
y[::2] = 2 ** x


## Aggregates
# With reduce() method, we can repeatedly execute a given operation to 
# all elements of the array, until a single result remains
# example with add, multiply
x = np.arange(1, 6)
np.add.reduce(x)
np.multiply.reduce(x)

# with accumulate() method, we can reduce AND store all the intermediate values
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