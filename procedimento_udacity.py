#-*- coding: utf-8 -*-
#Defina uma função, measure_udacity, que recebe uma lista de strings
# e devolve um número que corresponde à contagem das strings na lista começadas com a letra 'U' maiúscula.
def measure_udacity(p):
    count=0
    for e in p:
        if e[0]=="U":
            count=count+1
    return count




print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

#def sum_list(p):
#    result=0
#    for e in p:
#        result=result+e
#    return result

#print sum_list([1, 7, 4])
#>>> 12
