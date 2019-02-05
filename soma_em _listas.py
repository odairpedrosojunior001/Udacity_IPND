#-*- coding: utf-8 -*-
#Escreva uma função, sum_list, que recebe uma lista de números e devolve a soma de seus elementos.
#list=[1,7,4]
#sum_list=list[0]+list[1]+list[2]
#print sum_list

def sum_list(p):
    result=0
    for e in p:
        result=result+e
    return result






print sum_list([1, 7, 4])
#>>> 12
print sum_list([9, 4, 10])
#>>> 23
print sum_list([44, 14, 76])
#>>> 134
