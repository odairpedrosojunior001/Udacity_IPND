#-*- coding: utf-8 -*-
def isLeapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
def daysInMonth(year,month):# criando a sub de dias no mes ainda considerando 30 dias.
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    if month==2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
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
    assert nextDay(2013,9,30)==(2013,10,1)
    assert daysBetweenDates(2013,1,1,2014,1,1)==365
    assert daysBetweenDates(2012,1,1,2013,1,1)==366
    assert nextDay(2012,2,28)==(2012,2,29)
