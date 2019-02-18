### Python data types vs C
# As python is dynamically typed, we don't assign types to variables on declaration
# We can also switch a variable of type int to String seamlessly
# i.e.: 
# x = 4
# x = 'four'
# works without error, where C would throw an error due to type mismatch


### Python ints are more than ints
# The standard python implementation is written in C
# SO, all python objects (and everything in Python is an object) is deep down
# just a compound C structure
x = 1000

# 