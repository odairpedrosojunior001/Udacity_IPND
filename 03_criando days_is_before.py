#-*- coding: utf-8 -*-
def dateIsBefore(year1,month1,day1,year2,month2,day2):

    if year1<year2:
        return True
    if year1==year2 and month1<month2:
        return True
    if year1==year2 and month1==month2 and day1<day2:
        return True
    return False

print dateIsBefore(2012,1,1,2011,1,7)





#return True or False para a condição da data 1 vir antes da 2.
