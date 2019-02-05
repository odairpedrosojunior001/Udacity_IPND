#-*- coding: utf-8 -*-
#p=[4,6,7] # exemplo de procura de numero  em lista usando index
#print p.index(9)  #exemplo de procura de numero inexistente ( error )
#print p.index(7) #exemplo de procura de numero existente, retorna a posição do 1 numero encontrado

#t=[6,10,11]
#print 10 in t # função in devolve true ou false dependendo se o elemento procurado esta dentro da listaself.
def find_element(p,v):
    i=0
    if v in p:
        return p.index(v)
    return -1



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
