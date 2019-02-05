#-*- coding: utf-8 -*-

# adicionar um novo elemento a lista, no final da lista.
stooges=["Moe","Larry","Curly"]
stooges.append("Shemp")
print stooges
stooges.append("Odair")
print stooges

# concatenar 2 ou mais listas
list1=[1,2,3]
list2=["Odair",1981,"Tamara",1991,"Duda",2016]
list3=list1+list2
print list1+list2

# len , traz a quantidade de elementos de uma lista
print len(list1)
print len(list2)
print len(list3)
