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
