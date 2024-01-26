# program to add, subtract 2 years, 5 months, 7 days to a date
from datetime import datetime
from dateutil import relativedelta

today = datetime.now()

# new_date = today + 5  ERRRORRR : should use relativedelta
new_date = today + relativedelta.relativedelta(years=0, months= 6, days=0)
print(new_date.date())