#-*- coding: utf-8 -*-
# Problema : Uma lista de inteiros na qual cada número (vamos chamar de "n")
# representa a conta de um inteiro que ocorre um n número de vezes na lista de inteiros gerada aleatoriamente.
#Por exemplo, se o número 4 está na lista gerada aleatoriamente 5 vezes,
#então teremos outra lista que contém o número 5 em index 4 nesta lista.
#Se o número 6 está na lista gerada aleatoriamente 2 vezes, então nossa lista output terá o número 2 em index 6 desta lista.
#O output até então ficaria assim: [0,0,0,0,5,0,2,0,0,0,0]

# 1 - Primeiro nossa lista randomica de tamanho 20 com 10 numeros randomicos:
import random
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
print random_list
# 2 - Criar loop para cada elemento lista:
count_list=[0]*11
count=0
index=0
print count_list
print list_length
# 3 - configurandoa estrutura de um loop para percorrer todos os indices da lista:
while index<len(random_list):
    index=index+1
print index
# obter a variavel que irá percorrer a lista:
    number=random_list[index]
#agora vamos somar 1 a contagem deste numero:
    count_list[number]=count_list[number]+1
