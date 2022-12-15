import calendar

date = input()
x = date.split(" ")
month= int(x[0])
day = int(x[1])
year = int(x[2])

weekday = calendar.weekday(year,month,day)

if weekday == 0:
    print("MONDAY")
elif weekday == 1:
    print("TUESDAY")
elif weekday == 2:
    print("WEDNESDAY")
elif weekday == 3:
    print("THURSDAY")
elif weekday == 4:
    print("FRIDAY")
elif weekday == 5:
    print("SATURDAY")
elif weekday == 6:
    print("SUNDAY")
else:
    print("Houston, we have a problem!")
