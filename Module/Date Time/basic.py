import datetime

today = datetime.datetime.today()# module.class.function

print(today)

today_1 = datetime.datetime.now()

print(today_1.year)
print(today_1.month)
print(today_1.day)
print(today_1.strftime("%A"))
#print(today_1.strftime())
print(today_1.hour)
print(today_1.minute)
print(today_1.second)
print(today_1.microsecond)
print(today_1.time())
