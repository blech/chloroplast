#!/usr/bin/env python3

# fetch-range
# to get a whole day's worth of goes images

from datetime import datetime, timedelta, timezone

from fetch_goes_image import FetchGOES

# GOES-17 is at 137.2º W so its midnight is at approx 0915 UTC
# there's a full disk image every 15 minutes
# this lists those times

year = 2018
doy = 341 # starting day: ending day is +1

dt = datetime(year, 1, 1, tzinfo=timezone.utc) + timedelta(doy - 1)
dt = dt + timedelta(hours=9, minutes=15)

end = dt + timedelta(days=1)

while dt < end:
    print(dt)
    FetchGOES(dt, satellite='goes17').process()
    dt = dt + timedelta (minutes=15)
    