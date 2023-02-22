import datetime
today = datetime.datetime.today().date()
now = datetime.datetime.now()

### 1
fivedays = datetime.timedelta(5)
print(today - fivedays)

### 2
oneday = datetime.timedelta(1)
print(f" yesterday - {today - oneday} \n today - {today} \n tomorrow - {today + oneday}")

### 3
print(now.microsecond)

### 4
date1 = datetime.datetime(2023, 2, 22, 23, 50, 0)
date2 = datetime.datetime(2023, 2, 23, 0, 0, 0)
secondsDif = (date2 - date1).total_seconds()
print(secondsDif)
