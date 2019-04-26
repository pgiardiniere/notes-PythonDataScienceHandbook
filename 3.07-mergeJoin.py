# Again, Pandas has high-performance, in-memory joins/merge ops
# it's main interface is pd.merge()     (also, Ser/DF join())

# First, redefine display() function from prior notes:
import pandas as pd
import numpy as np

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

### Relational Algebra
# The behavior of pd.merge() is a subset of Relational Algebra:
    # def: a set of formal rules for manipulating relational data
    # it forms the conceptual foundation of database operations

##############################
### Categories of Joins
# pd.merge() function implements a number of types of joins:
    #  one-to-one
    # many-to-one
    # many-to-many
# type of join performed is inferred based on the input data


## One-to-one joins:
# join where the Key column in both objects contain exactly the same entries
# behavior: precise match.
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
display('df1', 'df2')
df3 = pd.merge(df1, df2)
df3
# NOTE: as seen, precise index is discarded in merge, unless you are merging
# specifically using the index (e.g. left_index, right_index keywords used)


## Many-to-one joins:
# join where the Key column in one object contains duplicate entries
# behavior: match all cols, duplicate required data in the resulting table
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
display('df3', 'df4', 'pg.merge(df3, df4)')


## Many-to-many joins:
# join where key column in both objects contains duplicate entries
# behavior: match all cols, duplicate required data in the resulting table
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting', 
                              'Engineering', 'Engineering', 'HR', 'HR'],
                              'skills': ['math', 'spreadsheets', 'coding', 
                                         'linux', 'spreadsheets', 'organization']})


##############################
### Specification of the Merge Key
# default behavior of pd.merge() --- look for matching col names, use as Key
# if col names do not match, must handle:

## The 'on' keyword
# 