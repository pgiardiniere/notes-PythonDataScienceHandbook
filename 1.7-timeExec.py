### Timing & Profiling code execution
# A handful of iPython magics useful for benchmarking your code's execution:
 
%time     # Time exec of a single statement
%timeit   # Time exec of a single statement w/ more accurracy 
%prun     # Profile-Run --- Run code with the profiler
%lprun    # Line-Profile-Run --- Run code with the line-by-line profiler
%memit    # Measure memory use of a single statement
%mprun    # Memory-Profile-Run --- Run code with line-by-line memory profiler

# magics 3-6 are not included by default with iPython
#   3-4 are part of the 'line-profiler' extension
#   5-6 are part of the 'memory-profiler' extension


### Timing snippet w/ %timeit 
%timeit sum(range(100))             # small operation -> high num of repetitions (~1,000,000 loops in this case)

%%timeit
total = 0
for i in range(1000):
    for j in range(1000):
        total += i * (-1) ** j      # large operation -> low  num of repetitions (1 loop in this case)

# This is desirable behavior - e.g. repeated sorting of a list is dumb. (since re-sort on sorted data is best case runtime)

# example of this behavior:
import random
L = [random.random() for i in range(100000)]
%timeit L.sort()
%timeit L.sort()

# notice the second result 'wall time' is MUCH faster than first
# also you can compare the result to running %time twice (delete and re-initialize the list between runs)

# %timeit is always noticeably faster to execute than %time, for following reasons:
#   %time stops Python garbage collection
#   %time stops other system call
# i.e. we trade off accurracy (remove signal noise) for speed


### Profiling full scripts
# %prun
# This times the execution of a full-script, not just single/multi statement segments. This is just one way of accsesing. (more: %prun?)
def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i) for j in range(N)]
        total += sum(L)
    return total

%prun sum_of_lists(1000000)

# returns a table which categorizes total & percentage time spent for each function call
# we can from this ID which algorithms are most time-intensive and begin optimizing


### Profiling Line-by-line
%lprun

# not included by default with iPython, is an extension
    # for miniconda, check/install with:
    conda search line_profiler
    conda install line_profiler

%load_ext line_profiler                     # load in the extension to current session

%prun sum_of_lists(5000)                    # profile whole thing
%lprun -f sum_of_lists sum_of_lists(5000)   # profile function      (not different formats of output)


### memory profiling
%memit
%mprun

### %memit
# not included by default with iPython, is an extension
    # check/install to miniconda with:
    conda search memory_profiler
    conda install memory_profiler

%load_ext memory_profiler                   # load in the extension to current session
%memit sum_of_lists(1000000)


### %mprun
# NOTE: addt'nl setup required as %mprun will ONLY accept functions defined in seperate modules

del sum_of_lists
%%file mprun_demo.py

def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i) for j in range(N)]
        total += sum(L)
    return total


%mprun -f sum_of_lists sum_of_lists(1000000)        ## this one takes significantly longer to run