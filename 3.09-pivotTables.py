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

## multi-level pivot tables:
# 
age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')

# can apply technique on columns as well:
fare = pd.qcut(titanic['fare'], 2)
titanic.pivot_table('survived', ['sex', age], [fare, 'class'])

## additional pivot table options
# call signature as of Pandas 0.18
DataFrame.pivot_table(data, values=None, index=None, columns=None,
                      aggfunc='mean', fill_value=None, margins=False,
                      dropna=True, margins_name='All')

# aggfunc keyword controls type of aggregation applied (default=mean)
titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived':sum, 'fare':'mean'})

# 
titanic.pivot_table('survived', index='sex', columns='class', margins=True)


### Another Example: Birthrate Data
# get CDC data (if not already in dir)
# !curl -O https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv

# Pull CDC data on births in US
births = pd.read_csv('data/births.csv')