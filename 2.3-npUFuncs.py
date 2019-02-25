### The problem: Python slowness in loops
#
#
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)

# we can then time execution with a %timeit magic

# now, consider a case with a much bigger array of values:
big_array = np.random.randint(1, 100, size=1000000)
compute_reciprocals(big_array)  # remember to %timeit preceding

