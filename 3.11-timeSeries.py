# Pandas was developed in conetext of financial modeling (!)
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
    # set precision to nano-seconds

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