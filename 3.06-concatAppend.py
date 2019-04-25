# next few chapters will deal with aggregating data from different sources
# as such, will cover a few tools to help combine these datasets

# here we'll cover concatenation of Series/DataFrame objects with pd.concat
import pandas as pd
import numpy as np

# define a DF constructor for re-use within examples:
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

# example DataFrame:
make_df('ABC', range(3))

# also create a class to allow display of multiple DataFrames side-by-side
# it utilized the _repr_html_ method, iPython uses it to implement rich obj disp
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


##############################
### Recall: Concatenation of NumPy arrays
# Concatenation of Series/DF is similar to NP arrs, 
# done via np.concatenate function discussed in "basics of NP arrays" ch
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])