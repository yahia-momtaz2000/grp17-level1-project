# Write a program to GEt the date after 12 Working days from a date
from datetime import datetime
from dateutil import relativedelta
today = datetime.now()
required_date = today
jump_days = 12
# startdate = 25-12-2023,   enddate : 10-1-2023
for i in range(jump_days):
    if required_date.date().weekday() == 3: # Thursday
        required_date = required_date + relativedelta.relativedelta(days = 3)
    elif today.date().weekday() == 4: # Friday : only found if today is Friday
        required_date = required_date + relativedelta.relativedelta(days = 2)
    else:
        required_date = required_date + relativedelta.relativedelta(days = 1)
print(f'After {jump_days} working days from {today.date()}, the new date is {required_date.date()}')