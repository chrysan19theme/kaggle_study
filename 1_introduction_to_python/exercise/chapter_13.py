from datetime import date
from datetime import time
import time as tm
from datetime import timedelta
#13.2
today_string='2025/08/20'
print(today_string)

#13.3
fmt='%Y/%m/%d'
fmt2='%d'
today=tm.strptime(today_string,fmt)
print(tm.strftime(fmt2,today))

#13.4
my_birth=date(1998,4,3)

#13.5
print(my_birth.strftime('%A'))

#13.6
target_day=my_birth+timedelta(days=10000)
print(target_day)