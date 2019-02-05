#-*- coding: utf-8 -*-
#Escreva uma função, replace_spy, que recebe uma lista com três números e incrementa em um o valor do terceiro elemento.
# Remova o # das últimas linhas do código inicial para testar sua função.
spy = [0,0,9]
def replace_spy(spy):
    replace_spy=spy
    spy[2]=replace_spy[2]+1

replace_spy(spy)
print spy

#spy = [0,0,7]
#agent = spy
#spy[2] = agent[2] + 1
