### Aggregation and Grouping
# Now that we've fetched data in PD, time to explore the aggregation funcs
# sum(), mean(), median(), min(), max(), "groupby"s, etc.

import numpy as np
import pandas as pd

# omitting display function - muddies up the notes for not much gain

### Planets Data
# Will use Planets dataset, available via Seaborn pkg
# it has info on planets astronomers have discovered around other stars
import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape
planets.head()

##############################
### Simple Aggregation in Pandas
# Pandas Series aggregations behave similarly to the NumPy Arrays covered
# i.e. aggregates return a single value on them
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser
ser.sum()
ser.mean()

# for DataFrames, by default aggregates return results for each column
df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df
df.mean()
# specify "axis" argument to receive row info (i.e. columns as to-be-aggregated)
df.mean(axis=1)


# In addition to the other aggregators covered in CH-2.4 (np Aggregation)
# describe() method will return common summary statistics:

# describe() planets, drop rows with missing data
planets.dropna().describe()
