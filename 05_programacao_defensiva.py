#-*- coding: utf-8 -*-
def nextDay(year,month,day): # definir uma função que traz o proximo dia , levando em conta meses de 30 dias
    if day<30:
        return year,month,day+1
    else:
        if month<12:
            return year,month+1,1
        else:
            return year+1,1,1
def dateIsBefore(year1,month1,day1,year2,month2,day2):# função que traz se data 1 é anterior a data 2
    if year1<year2:
        return True
    if year1==year2 and month1<month2:
        return True
    if year1==year2 and month1==month2 and day1<day2:
        return True
    return False
def daysBetweenDates(year1, month1, day1, year2, month2, day2): # (2013,01,24,2013,6,29)
    days=0
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1=nextDay(year1,month1,day1)
        days=days+1
    return days
# programação defensiva, trazer erro no codigo caso data 1 venha depois de data 2:
def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
test()
