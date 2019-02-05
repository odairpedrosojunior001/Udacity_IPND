#-*- coding: utf-8 -*-
#Faça uma função chamada countdown (contagem regressiva), que recebe um inteiro positivo como input
#e imprime uma contagem regressiva desse número até 1, seguido pela palavra "Blastoff!"
#(a palavra utilizada para autorizar o lançamento de um foguete, em inglês).
#A função não deve retornar nada. Para executar uma contagem a partir de 3, por exemplo,
#você deve executá-la chamando apenas countdown(3), e não print countdown(3).
def countdown(x):
    i=6
    while i>x:
          i=i-3
          print i
          i=i+2
    print "Blastoff!"
countdown(3)

def countdown(n):
   while n > 0:
     print n
     n = n-1
   print "Blastoff!"
countdown(3)
