### Computation on NumPy Arrays: Universal Functions
# NumPy array computation can be very fast, or very slow
# if you try to use them in a more traditional loop-style manner, it's very slow
# Vectorized operations are fast though, these are generally implemented in np ufuncs

# here's a traditional loop-based approach to operating on arr values to demonstrate
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)     # remember to precede with %timeit in ipython

# we can then time execution with a %timeit magic

# now, consider a case with a much bigger array of values:
big_array = np.random.randint(1, 100, size=1000000)
compute_reciprocals(big_array)  # remember to precede with %timeit in ipython
    # in my case, returned "1.63 s +- 3.97 ms per loop ..."

##############################
### UFuncs introduction
# Interface for statically typed, compiled routines are known as vectorized operations
# can be achieved by performing an operation on the array, which then is applied to each el
# Advantage of vectorized approach is it pushes loop into the compiled layer under NumPy, for faster exec

# sample 1: ufunc operation b/w Scalar type and Array
compute_reciprocals(values)
1.0 / values

(1.0 / big_array)    # remember to preceded with %timeit in ipython
    # in my case, returned "4.11 ms +- 2.83 us per loop ..."

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

# can see a partial list of the long-form uFunc arithmetic utilies used above in the chapter text

## Absolute Value
## Trigonometric functions
## Exponents and logarithms
## Specialized ufuncs

### Advanced UFunc Features
# 
# 
# 