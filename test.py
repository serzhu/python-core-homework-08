from datetime import date, datetime, timedelta

users = [
        {"name": "1", "birthday": datetime(1976, 12, 31).date()},
        {"name": "2", "birthday": datetime(1976,  1, 1).date()},
        {"name": "3", "birthday": datetime(1976, 12, 10).date()},
        {"name": "4", "birthday": datetime(1976, 12, 13).date()},
        {"name": "5", "birthday": datetime(1976, 12, 15).date()},
    ]
if len(users) == 0:
    print({})

#d = date.today()
d = date(2023, 12, 29)
crnt_year = d.year
next_year = crnt_year + 1
week = []

for i in  range(0,7):
    #if (d.day+i) < 
    week.append(d + timedelta(days=i)) # make list with future 7 dates
print(week)
#key == "birthday" and 
birthdays = []
for item in users:
    for key,val in item.items():
        if key == "birthday":
            crnt_year = val.replace(year=d.year)
            next_year = val.replace(year=d.year+1)
            if (crnt_year in week or next_year in week):
            #print(val.replace(year=d.year).strftime('%A'))  # from dict birthday weekday
                birthdays.append(item.)
print(birthdays)




# for i in  range(0,7):
#     weekday = d.replace(day=d.day+i).strftime('%A')
#     if weekday not in ['Saturday', 'Sunday']:
        #print(weekday)
