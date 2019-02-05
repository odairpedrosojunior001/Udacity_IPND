#-*- coding: utf-8 -*-
# Dada a variável days_in_month (dias do mês), crie uma função how_many_days,
# que recebe um número representando um mês do ano e devolve o número de dias naquele mês.
def how_many_days(month_number):
    days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month_number==1:
        return days_in_month[0]
    if month_number==2:
        return days_in_month[1]
    if month_number==3:
        return days_in_month[2]
    if month_number==4:
        return days_in_month[3]
    if month_number==5:
        return days_in_month[4]
    if month_number==6:
        return days_in_month[5]
    if month_number==7:
        return days_in_month[6]
    if month_number==8:
        return days_in_month[7]
    if month_number==9:
        return days_in_month[8]
    if month_number==10:
        return days_in_month[9]
    if month_number==11:
        return days_in_month[10]
    if month_number==12:
        return days_in_month[11]
print how_many_days(12)
