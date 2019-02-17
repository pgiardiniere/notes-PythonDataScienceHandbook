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
# %timeit 
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

##############################
### Profiling full scripts
# %prun
# This times the execution of a full-script, not just single/multi statement segments
# Here, we use the iPython magic %prun to access the python built-in code profiler. there are other ways - refer to official Py docs
def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i) for j in range(N)]
        total += sum(L)
    return total

# %prun sum_of_lists(1000000)

# returns a table which categorizes total & percentage time spent for each function call
# we can from this ID which algorithms are most time-intensive and begin optimizing

# get more information on available options with %prun?

##############################
### Line-by-line profiling
# %lprun
#
# not included by default with iPython, is an extension
# book recommends get with '$ pip install line_profiler'
# however, I'm running full-anaconda, so did the following:

# 'conda search line_profiler'
# 'conda install line_profiler'

# since I have full anaconda install, it was already in by default. I just picked up an update from 4.5.12 > 4.6.4 in current environment

# now, in your iPython session, bring in the extension by running:
#   %load_ext line_profiler

# and run:
#   %prun sum_of_lists(5000)
# output: 

## ""get output in a file and add here with the %prun -T or -D flags. %prun? for instructions"" then put the output here for reference


# compare to:
#   %lprun -f sum_of_lists sum_of_lists(5000)
# output:

## ""get output in a file and add here with the %lprun -T or -D flags. %lprun? for instructions"" then put the output here for reference



##############################
### memory profiling
# %memit
# %mprun
#
# not included by default with iPython, is an extension
# book recommends get with '$ pip install memory_profiler'
# however, I'm running full-anaconda, so did the following:

# 'conda search memory_profiler'
# 'conda install memory_profiler'

# looks like I didn't already have this one. I just picked up version 0.55.0 in current environment

# now, in your iPython session, bring in the extension by running:
#   %load_ext memory_profiler

# and run:
#    %memit sum_of_lists(1000000)
# output: 

## ""get output in a file and add here with the %prun -T or -D flags. %prun? for instructions"" then put the output here for reference

# NOTE: addt'nl setup required as %mprun will ONLY accept functions defined in seperate modules
# del sum_of_lists
# %%file mprun_demo.py
# # cd to current working dir
# def sum_of_lists(N):
#     total = 0
#     for i in range(5):
#         L = [j ^ (j >> i) for j in range(N)]
#         total += sum(L)
#     return total

# compare to:
#   %mprun -f sum_of_lists sum_of_lists(1000000)
# output: 

## ""get output in a file and add here with the %prun -T or -D flags. %prun? for instructions"" then put the output here for reference

### takes significantly longer to run