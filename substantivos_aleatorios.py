#-*- coding: utf-8 -*-Escreva a função random_noun, que não recebe nenhum argumento,
#mas devolve um substantivo aleatório (entre dois). Use a função randint para gerar um número aleatório entre 0 e 1.
# Depois, devolva "sofa" quando esse número for 0 e "llama" quando for 1.
#Não use o comando print dentro da função!

from random import randint #importa a função randint , presente no módulo random

def random_noun(): # definir a função : "substantivo_aleatório"
    random_num=randint(0,1) # geração do numero randomico e seus estados.
    if random_num ==0: # criação do codigo que vai dizer de a variavel for 1 o que será printado e se for 0 o que retornará
        return "Sofa"
    else:
        return "llama"
print random_noun() # chamada da função : "substantivo_aleatório"

#from random import randint
#randint(low,high)
#num=randint(1,3)
#def random_noun():
