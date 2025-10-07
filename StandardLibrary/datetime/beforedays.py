import datetime

before30days=datetime.date.today() + datetime.timedelta(days=-30)

print(before30days)