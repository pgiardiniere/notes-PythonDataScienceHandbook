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



import numpy as np