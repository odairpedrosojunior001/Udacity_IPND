#-*- coding: utf-8 -*-
#Escreva um código que imprime a capital da Índia, dada a lista abaixo:
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]
#Há um erro nesta lista: a capital da Índia, na verdade, é Nova Délhi.
print countries[1][1]
#Dada a mesma lista de países do exercício anterior, quantas vezes a população da Romênia cabe na da China?
#Acesse as posições correspondentes da lista, faça a divisão e imprima o resultado.
pop_china=countries[0][2]
pop_romenia=countries[2][2]
tam_relativo=pop_china/pop_romenia
print tam_relativo

#outra forma
print countries[0][2]/countries[2][2]
