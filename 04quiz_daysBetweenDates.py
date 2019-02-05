#-*- coding: utf-8 -*-
# 1 -  definição dos inputs e outputs e cenarios.
#inputs =  2 datas  / output  = 1 saida em dias
# template de entrada da função indica 6 parametros para as entradas (y1,m1,d1,y2,m2,d2)
# output (saidas do problema) = retornar um valor em dias que corresponde ao intervalo entre a 1 e 2 datas.
#2 - testes de exemplo entre as entradas e saida para saber o comportamento das saidas em relação as entradasself.
# pseudo codigo para teste 1:
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
print daysBetweenDates(2013,1,24,2013,6,29)

#odair (04/10/18) :  tem 36 anos 11 meses 10 dias
#(y2-y1)-1 quant. anos (2018-1981) -1 = 36 anos
#se m1=m2 : 23/10/1981 - 04/10/2018  ; conta: a= 2018-1981=37-1= 36 anos ; m= m1 ou m2 +1 = 11 meses ; d=30-(23-3) = 10 dias
#se m1>m2 : 01/10/2000 - 02/05/2018  : conta: a = 2018-1981=18-1=17 ; e m=12-05= 07  ; d=30-(01-02)
#se m1<m2 : 01/05/2000 - 02/10/2018 : conta: a= 2000-2018= 18 ; m= 10-5 = 05 ; d= 31+30+31+31+30+02 =
#return days
