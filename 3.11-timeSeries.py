# Pandas was developed in conetext of financial modeling
# has extensive tools for dates, times, time-indexed data:
    # Time Stamps                   - particular moments in time (6:00 Jul 4th, 2015)
    # Time Intervals and Periods    - length of time between a begin and end point
    # Time deltas or durations      - an exact length of time (22.5 seconds)

### Dates and Times in Python
# general python - not PD specific (though PD's are often better)

## native Python dates and times: "datetime" and "dateutil"
# "datetime" module contains built-in basic objects
# "dateutil" is a 3rd party module.

# manually build a date using 'datetime' type:
from datetime import datetime
datetime(year=2015, month=7, day=4)

from dateutil import parser
date = parser.parse("4th of July, 2015")
date

# Once you have a datetime object, can print day of week
date.strftime('%A')
    # see doc at: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    # also: http://labix.org/python-dateutil 
    # and TimeZones for the particularly masochistic: http://pytz.sourceforge.net/

# datetime and dateutil are flexible and have simple syntax
# these objects and built-ins perform most ops you'd ever want
# issue: large arrays of dates/times are NOT efficient
    # enter: NP

## Typed arrays of times: NumPy's "datetime64"
import numpy as np
date = np.array('2015-07-04', dtype=np.datetime64)
date
date + np.arange(12)
    # with a small op, can't see the efficiency gain really, but same idea as shown before

np.datetime64('2015-07-04 12:00')
    # time zone automatically set to TZ of local computer
np.datetime64('2015-07-04 12:59:59:50', 'ns')
    # set precision to nano-seconds -NOTE: "timezone aware datetimes are deprecated" 

# a detail of datetime64 and timedelta64 objects: built upon a 
# "fundamental time unit". As they're limited to 64 bit precision, the limit
# to range of times encodable is dependent upon the precision of time you specify


## Dates and times in pandas: best of both (native/NP)

import pandas as pd
date = pd.to_datetime("4th of July, 2015")
date

# use string format code to output day of week for given date object
date.strftime('%A')     # Returns: 'Saturday'

# can do NP-style vectorized operations directly on date objects:
date = pd.to_timedelta(np.arange(12), 'D')

##############################
### Pandas Time Series: Indexing by Time
# PD is best when you index data by timestamps
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
data

# now we have data (ints) in a Series (indexed by timestamps)
# can make use of Series indexing patterns familiar with,
# where now we pass values which are coerced into Date object type
data['2014-07-04':'2015-07-04']

# additionally, date-only index operations available.
# e.g. pass a year to obtain a slice of all data from given year:
data['2015']


### Pandas Time Series Data Structures:
# fundamental PD data structures for Time Series data:

# Type                      Index Structure     About
# -----------------------------------------------------------------
# Timestamps                DatetimeIndex       A replacement for Python native datetime
# Time Periods              PeriodIndex         fixed-frequency interval
# Time Deltas/Durations     TimedeltaIndex      

# most fundamental is timestamp/DatetimeIndex

# pd.to_datetime()
    # when passed single val, yields a timestamp
    # when passed a list/arr, yields a DatetimeIndex
dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                        '2015-Jul-6', '07-07-2015', '20150708'])
dates

# can convert a DatetimeIndex to a PeriodIndex by using:
# to_period()
    # by adding a frequency code as well. 'D' indicates daily freq:
dates.to_period('D')

# TimedeltaIndex is created (in one case) by subtracing a date from another:
dates - date[0]


## Regular Sequences: pd.date_range()

# pd.date_range()       for     timestamps
# pd.period_range()     for     periods
# pd.timedelta_range()  for     timedeltas

# begin and end date (frequency default: 1 day)
pd.date_range('2015-07-03', '2015-07-10')

# can specify with startpoint and num periods
pd.date_range('2015-07-03', periods=8)

# Additionally, can make custom frequncy - see hourly timestamp range below
pd.date_range('2015-07-03', periods=8, freq='H')

# or, a sequence of durations increasing by an hour:
pd.timedelta_range(0, periods=10, freq='H')


### Frequencies and Offsets
# (table of codes)
# stuff ------
pd.timedelta_range(0, periods=9, freq="2H30T")

# get range of 5 business days, beginning on 2015-07-01
from pandas.tseries.offsets import BDay
pd.date_range('2015-07-01', periods=5, freq=BDay())


### Resampling, Shifting, and Windowing
from pandas_datareader import data 

goog = data.DataReader('GOOG', start='2004', end='2016', data_source='google')
#   NOTE: "ImmediateDeprecationError - Google Finance dep. due to API breaks"
#       will not be able to complete section notes. Goes into some basic plots.

## Resampling and Converting Frequencies
    # still uses deprecated functionality


### Example: Visualizing Seattle Bicycle Counts
# data get:
  # as before, boot up the ubuntuvm and curl into the (old) GD workspaces data volume
  # !curl -o FremontBridge.csv https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD
  # then push into 'real' workspaces/data dir for manipulation
data = pd.read_csv('data/FremontBridge.csv', index_col='Date', parse_dates=True)
data.head()

# formatting, shorten column names and provide a simple aggregate col
data.columns = ['West', 'East']
data['Total'] = data.eval('West + East')

data.dropna().describe()
## Visualizing the data
%matplotlib inline
import seaborn; seaborn.set()

data.plot()
plt.ylabel('Hourly Bicycle Count');

# problem: 25,000 hourly samples are too granular
# resample data to a courser grid (weekly)
weekly = data.resample('W').sum()
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count');

# can use a rolling mean, 30 day window width, to smooth edges a little:
daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])

# use a Guassian window to smooth edges further: (50 day width, 10 day Gaussian intra-width)
daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', '--', '-'])

## Digging in
# with our smooth graph, we have general idea, but can't see particulars
# e.g. How is average traffic affected as function of time of day. Use GroupBy's
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-'])
    # unsurprisignly, traffic is highest overall around 8:00 and 5:00 
    # can see directionality too - West high @ 8, East high @ 5

# check traffic by weekday (instead of avg daily overall)
by_weekday = data.groupby(data.index.dayofweek).mean()
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
by_weekday.plot(style=[':', '--', '-']);
    # unsurprisingly, traffic is highest M-Fri  

# Now, compound groupby to check hourly trends on weekdays vs weekends
# set up 2 flags, to mark type of day and time groupings, respectively
weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()

import matplotlib.pyplot as pltfig, ax = plt.subplots(1, 2, figsize=(14, 5))
by_time.ix['Weekday'].plot(ax=ax[0], title='Weekdays',
                           xticks=hourly_ticks, style=[':', '--', '-'])
by_time.ix['Weekend'].plot(ax=ax[1], title='Weekends',
                           xticks=hourly_ticks, style=[':', '--', '-'])