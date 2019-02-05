#-*- coding: utf-8 -*-
#Escreva a função random_verb, que não recebe nenhum argumento, mas devolve um verbo aleatório (entre dois).
#Use a função randint para gerar um número aleatório entre 0 e 1.
#Depois, devolva "run" quando esse número for 0 e "kayak" quando for 1.

from random import randint# importação função randint
def random_verb():
    random_num=randint(0,1) #geração do numero randomico
    if random_num==0: #logica para print dos verbos aleatorios.
        return "run"
    else:
        return "kayak"
print random_verb()
