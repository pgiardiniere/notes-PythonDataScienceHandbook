# GroupBy as an abstraction allows deeper understanding of datasets
# Pivot Tables are somewhat of an extension on the idea
# the same split-apply-combine happens, but output is now 2D grid

##############################
### Motivating Pivot Tables
# Using dataset of passengers on the Titanic for demonstrations:
import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')

titanic.head()

titanic.groupby('sex')[['survived']].mean()

titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()
# issue: to get more detailed data requires lots of ugly syntax with GroupBy

### Pivot table syntax:
# this is the pivot_table() method equivalent:
titanic.pivot_table('survived', index='sex', column='class')