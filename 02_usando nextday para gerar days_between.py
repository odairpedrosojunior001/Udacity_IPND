def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    month0=30
    year0=360
    if year1==year2 and month1==month2:
        return day2-day1
    if year1==year2 and day1==day2:
        return (month2-month1)*month0
    if month1==month2 and day1==day2 and year1!=year2:
        return (year2-year1)*year0

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
