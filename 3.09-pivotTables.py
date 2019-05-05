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
titanic.pivot_table('survived', index='sex', columns='class')

## multi-level pivot tables:
# just like GroupBy, pivot tables can be specified with multiple levels
# check age as third dimesnions using pd.cut() function:
age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')

# can apply cut() on columns as well:
fare = pd.cut(titanic['fare'], 2)
titanic.pivot_table('survived', ['sex', age], [fare, 'class'])

## additional pivot table options
# call signature as of Pandas 0.18
DataFrame.pivot_table(data, values=None, index=None, columns=None,
                      aggfunc='mean', fill_value=None, margins=False,
                      dropna=True, margins_name='All')

# aggfunc keyword controls type of aggregation applied (default=mean)
titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived':sum, 'fare':'mean'})
    # values keyword omitted - determined automatically when specifying aggfunc

# margins useful to compute totals along each grouping
titanic.pivot_table('survived', index='sex', columns='class', margins=True)


### Another Example: Birthrate Data
# get CDC data (if not already in dir)
# !curl -O https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv

# Pull CDC data on births in US
births = pd.read_csv('data/births.csv')
births.head()

# add Decade column, check M/F births as func of decade:
births['decade'] = 10 * (births['year' // 10])
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')

%matplotlib inline
import matplotlib.pyplot as plt
sns.set()   # use Seaborn styles
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year');


## Further data exploration
# there are more interesting features (not related to Pivot Tables)
# can pull out of this dataset using PD tools

# trim input data:
quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])

# now, can use query() method to filter out rows with births outside given vals
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig')
# set 'day' column to integer (was originallyy string)
births['day'] = births['day'].astype(int)

# combine day, month, and year to create a Date index (time series)
births.index = pd.to_datetime(10000 * births.year + 100 * births.month + 
                              births.day, format='%Y%m%d')

births['dayofweek'] = births.index.dayofweek


import matplotlib.pyplot as plt
import matplotlib as mpl

births.pivot_table('births', index='dayofweek', 
                   columns='decade', aggfunc='mean').plot()

plt.gca().setxticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day')

# insight: births less common on weekends than weekdays

# now, group by month and day seperately
births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
births_by_date.head()