from datetime import datetime
import pytz
print(pytz.all_timezones[:5])

india= pytz.timezone("Asia/Kolkata")

india_time = datetime.now(india)
print("Indian time: ", india_time)

#  Convert time from one timezone to Another

utc = pytz.utc    # coordinated Universal Time
ist = pytz.timezone("Asia/Kolkata")    # Indian Standard time
us = pytz.timezone("US/Eastern")

utc_time = datetime.now(utc)

ist_time= utc_time.astimezone(ist)
us_time= utc_time.astimezone(us)

print("UTC time: ", utc_time)
print("ISt time: ", ist_time)
print("US Time: ", us_time)

naive=datetime.now()
print("naive: ",naive)

aware= pytz.timezone("Asia/Kolkata").localize(naive)
print("Aware: ", aware)

# ISO format (international standard date and time format)
time= datetime.now(pytz.timezone("Asia/Kolkata"))
print(time.isoformat())
