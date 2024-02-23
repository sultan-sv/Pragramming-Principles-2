import datetime
date1 = datetime.datetime(2024, 10, 4)
date2 = datetime.datetime.today()
delta = date1 - date2
print(delta.total_seconds())