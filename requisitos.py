#-*- coding: utf-8 -*-
#1 - Selecionar niveis de dificuldade
#1.1 - Exibir niveis de dificuldade
#1.2 - Pedir para usuario selecionar um nivel
#2- jogo
#2.1 - Exibir uma frase com lacunas ( deve ser diferente para cada nivel)
#2.2 - Pedir para o usuario advinhar as palavras da primeira lacuna
# -  Se usuario errar , avisar que ele errou e pedir para ele tentar novamente
# - Se usuario acerta, exibe a frase com alacuna preenchida e repete o processo para proxima lacuna
#2.3 - Quando todas as lacunas forem preenchidas , dar parabéns e encerrar o jogado
#2.4 - Extra , controlar o numero de tentativas

#Pseudo codigo : ideia do que o programa vai fazer:
#dificuldade=pergunta dificuldade()
#frase=obtem_frase_dificuldade(dificuldade)

#para cada lacuna:
# - mostrar frase(frase)
# - resposta=pergunta_resposta_lacuna(frase,lacuna)

#se resposta certa:
# - mostra parabens lacuna()
# - frase=substitui lacuna por resposta(frase,lacuna,resposta)
# - passa para proxima lacuna

#se resposta for errada:
# - mostra tente novamente()
# - repete pergunta para mesma lacuna

# final do jogo, usuaro acertou tudo:
# - mostrar _parabens final()
# - encerra o programa()
