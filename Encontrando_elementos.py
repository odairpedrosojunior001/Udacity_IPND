#-*- coding: utf-8 -*-
#Defina uma função, find_element, que recebe uma lista e um valor (de qualquer tipo)
#e devolve o índice do primeiro elemento da lista que corresponde ao valor passado.
def find_element(p,v):
    i=0  #buscar o indice
    for e in p:
        if e==v:
            return i
        i=i+1
    return -1
print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
