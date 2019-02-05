#-*- coding: utf-8 -*-
frase1="O cavaleiro AIORIA e o cavaleiro de OURO de LEAO." # variavel com string 1
frase2="IKKI e o cavaleiro de BRONZE de FENIX."  # variavel com string 2
print frase1
print frase2
lista_palavras_substituir=["AIORIA","OURO","LEAO","IKKI","BRONZE","FENIX"] # variavel com palavras a substituir nas variaveis
frase1_lista=frase1.split() # transformando a variavel1 com string em variavel contendo uma lista
frase2_lista=frase2.split() # transformando a variavel2 com string em variavel contendo uma lista
print frase1_lista
print frase2_lista
print " ".join(frase1_lista) # retornando a variavel1 com lista para string novamente
print " ".join(frase2_lista) # retornando a variavel2 com lista para string novamente
