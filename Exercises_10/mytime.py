from datetime import datetime as dt 
# Get the current time, returns a value like 2022-10-09 17:46:45.151666 
today = dt.now()
print(today) 
weekday = dt.now().strftime("%A")
print(weekday)
month = dt.now().strftime("%B")
print(month)
# Get Unix time, returns a value like 1665566809.057217 
unix_epoch_time = dt.timestamp(today) 
print(unix_epoch_time)


# Import date class from datetime module
from datetime import date
 
# Returns the current local date
today = date.today()
print("Today date is: ", today)