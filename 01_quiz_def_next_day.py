#-*- coding: utf-8 -*-
#Defina uma função, nextDay(year, month, day), que recebe uma data válida do calendário gregoriano
# separada em ano, mês e dia (nesta ordem e em números) como input e devolve a data do dia seguinte,
#novamente como ano, mês e dia. Suponha que todos os meses têm 30 dias!
def nextDay(year,month,day):

    if day<30:
        return year,month,day+1
    else:
        if month<12:
            return year,month+1,1
        else:
            return year+1,1,1
print nextDay(1900,12,31)
