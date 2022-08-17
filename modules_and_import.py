from datetime import date, timedelta
year,month,day = map(int, input().split())
data1 = date(year,month,day)
delta = timedelta(days = int(input()))
data2 = data1 + delta
print(data2.year,data2.month,data2.day)