# program to show the nearest sundays
import calendar
from datetime import datetime
from dateutil import relativedelta

today = datetime.now() # 25-12-2023

print('----- the nearest sunday from today ------')
nearest_sunday = today + relativedelta.relativedelta(weekday = calendar.SUNDAY)
print(nearest_sunday)

print('----- the nearest 2nd sunday from today ------')
nearest_sunday = today + relativedelta.relativedelta(weekday = calendar.SUNDAY, weeks=1)
print(nearest_sunday)