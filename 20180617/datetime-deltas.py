import datetime

date1 = 'April 12, 1961 2:07'
date2 = '07/21/69 2:56:15 AM UTC'

date1_dt = datetime.datetime.strptime(date1, '%B %d, %Y %H:%M')
date2_dt = datetime.datetime.strptime(date2, '%m/%d/%y %I:%M:%S %p %Z')

print(date1_dt)
print(date2_dt)

datediff = date2_dt - date1_dt
YEAR = 365
MONTH = 30
years_diff, days_diff = divmod(datediff.days, YEAR)
month_diff, days_diff = divmod(days_diff, MONTH)

print(years_diff,month_diff)

future_now = datetime.datetime.now() + datetime.timedelta(days=years_diff * 365 + 30*days_diff)
print(future_now)

print(future_now.date())
# print(future_now.date() - datetime.datetime.now.date())

my_future_age = divmod((future_now.date() - datetime.datetime.now().date()).days + datetime.timedelta(days=365*39).days, 365)
print(my_future_age[0])