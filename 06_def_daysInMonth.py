#-*- coding: utf-8 -*-
def daysInMonth(year,month):# criando a sub de dias no mes ainda considerando 30 dias.
    return 30
def nextDay(year,month,day):
    if day<daysInMonth(year,month): #apontando a função daysmonth dentro de nextday
        return year,month,day+1
    else:
        if month<12:
            return year,month+1,1
        else:
            return year+1,1,1
def dateIsBefore(year1,month1,day1,year2,month2,day2):
    if year1<year2:
        return True
    if year1==year2 and month1<month2:
        return True
    if year1==year2 and month1==month2 and day1<day2:
        return True
    return False
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days=0
    assert not dateIsBefore(year2,month2,day2,year1,month1,day1)
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1=nextDay(year1,month1,day1)
        days=days+1
    return days
def test(): #testando a função sub dias no mes:#testes com meses de 30 dias !!!!
    assert daysBetweenDates(2013,1,1,2013,1,1)==0
    assert daysBetweenDates(2013,1,1,2013,1,2)==1
    assert nextDay(2013,1,1)==(2013,1,2)
    assert nextDay(2013,4,30)==(2013,5,1)
    assert nextDay(2012,12,31)==(2013,1,1)
print "Test Finished"
