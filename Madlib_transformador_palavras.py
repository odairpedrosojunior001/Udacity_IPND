#-*- coding: utf-8 -*-
# Escreva código para a função word_transformer, que recebe uma string contendo uma palavra.
# Se a palavra for "NOUN", a função devolve um substantivo aleatório.Se for "VERB",
# ela devolve um verbo aleatório. Se não for nenhum dos dois, ela devolve a primeira letra da palavra.
from random import randint
def random_verb(): # FUNCAO DE VERBO RANDOMICO
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
def random_noun(): # FUNÇÃO DE SUBSTANTIVO RANDOMICO
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"
def word_transformer(word): # FUNÇÃO PALAVRA RANDOMICA, TRAZENDO VERBO OU SUBSTANTIVO CONFORME A CHAMADA DAS FUNCOES
    if word=="NOUN":
        return random_noun()
    if word=="VERB":
        return random_verb()
    return word[0]
print word_transformer("NOUN")
