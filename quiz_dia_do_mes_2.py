def how_many_days(month_number):
    days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]

print how_many_days(11)
