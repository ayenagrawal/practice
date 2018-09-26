import datetime

now = datetime.datetime.now()
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dayNoWeek = datetime.datetime.today().weekday()

print("a) Current date and time: "+ str(now))
print("b) Current year: ", now.year)
print("c) Current month: ", now.month)
print("d) Week number: ", datetime.date(now.year,now.month,now.day).isocalendar()[1])
print("e) Week day: ", weekday[dayNoWeek])
print("f) Day of year: ", now.timetuple().tm_yday)
print("g) Day of month: ", now.day)
print("h) Day of the week: ", dayNoWeek+1)
