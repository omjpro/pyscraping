import time
import calendar
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%a', time.localtime(time.time())))
print(calendar.calendar(2021))