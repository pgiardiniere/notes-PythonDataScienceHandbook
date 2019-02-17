### Timing & Profiling code execution
# A handful of iPython magics useful for benchmarking your code's execution:
# 
# %time     Time exec of a single statement
# %timeit   Time exec of a single statement w/ more accurracy 
# %prun     Profile-Run --- Run code with the profiler
# %lprun    Line-Profile-Run --- Run code with the line-by-line profiler
# %memit    Measure memory use of a single statement
# %mprun    Memory-Profile-Run --- Run code with line-by-line memory profiler

# magics 3-6 are not included by default with iPython
# 3-4 are part of the 'line-profiler' extension
# 5-6 are part of the 'memory-profiler' extension

### Timing snippets
# %timeit sum(range(100))
# since small op, timeit does very numerous repetitions
#   runs 100,000 loops
# here is larger operation:
# %%timeit
# total = 0
# for i in range(1000):
#     for j in range(1000):
#         total += i * (-1) ** j
#
# larger op does few repetitions
#   runs 1 loop

# This is desirable behavior - repeated sorting of a list, for example, would skew results down,
# as running a sort on a pre-sorted list is faster than unsorted
# see the following:
#
# import random
# L = [random.random() for i in range(100000)]
# %timeit L.sort()
# %timeit L.sort()
# 
# notice the second result 'wall time' is MUCH faster than first
# also you can compare the result to running %time twice (remember to delete and re-initialize the list)
# %timeit is always noticeably faster to execute than %time, for following reasons:
#   %time stops Python garbage collection to prevent interference with results
#   %time stops other system calls from occurring during timing to prevent interference with results

