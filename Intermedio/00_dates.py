### dates ###
from datetime import datetime, date, time, timedelta

now = datetime.now()
current_date = date(2024, 12, 31)

print(f"year: {now.year}, month: {now.month}, day: {now.day}")
print(f"hour: {now.hour}, minute: {now.minute}, second: {now.second}")

print(f"date: {current_date.today()}")

# timedelta

starDate = timedelta(days=30, weeks=2)
endDate = timedelta(days=10, weeks=3)
print(f"operation {starDate - endDate}")
