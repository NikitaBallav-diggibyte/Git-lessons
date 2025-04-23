import datetime
res=datetime.datetime.now()
res1=datetime.datetime(2020,6,8,10,30,45)

from datetime import datetime
res2=datetime.now()
res3=datetime(2020,6,8,10,30,45)
print(res)
print(res1)
print(res2)
print(res3)


cd=datetime.now()
res4=cd.strftime("%y")
print("short version of year", res4)
res5=cd.strftime("%Y")
print("Full version of year", res5)
res6=cd.strftime("%b")
print("short version of month", res6)
res7=cd.strftime("%B")
print("full version of month", res7)
res8=cd.strftime("%m")
print("month in digits", res8)
res9=cd.strftime("%a")
print("short version of day", res9)
res10=cd.strftime("%A")
print("full version of day", res10)
res11=cd.strftime("%d")
print("Date", res11)
res12=cd.strftime("%w")
print("No. of Weekday", res12)
res13=cd.strftime("%H")
print("24 hour format", res13)
res14=cd.strftime("%I")
print("12 hour format", res14)
res15=cd.strftime("%p")
print("AM/PM", res15)

from datetime import timedelta

n1= timedelta(days=5)
new=cd+n1
new2= cd-n1
print(new)
print(new2)

# similarly can do with month, weeks, hours, minutes, seconds
diff= cd-new
print(diff)