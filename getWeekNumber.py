from datetime import datetime
from pytz import timezone, utc

print(datetime(2016, 5, 2).strftime("%V"))


test = datetime(2017, 11, 24, tzinfo=timezone('EST'))

print(test.astimezone(utc))
