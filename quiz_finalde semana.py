#-*- coding: utf-8 -*-
# Escreva uma função chamada weekend, que recebe o nome de um dia de semana em inglês e
#devolve True se for um final de semana, ou False, no caso contrário. Os dias da semana em inglês,#
# começando pela segunda-feira, são: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' e 'Sunday'.
# Sua função deve devolver True para 'Saturday' ou 'Sunday'.
def weekend(day):
    if day=="Saturday" or day=="Sunday":
        return True
    return False
print weekend("Jully")
