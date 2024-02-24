import datetime as dt 

current_date = dt.datetime.now()
print(current_date - dt.timedelta(days = 5))


today = dt.date.today()
yesterday = today - dt.timedelta(days = 1)
tomorrow = today + dt.timedelta(days = 1)
print(yesterday, today, tomorrow, sep = "\n")


current_date_modified = current_date.replace(microsecond=0)
print(current_date_modified)


#difference in seconds 

date1_str = input()
date2_str = input()

date1 = dt.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = dt.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference = (date2 - date1).total_seconds()

print(f"The difference between the two dates is {difference} seconds.")