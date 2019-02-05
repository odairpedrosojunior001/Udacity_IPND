# coding=utf-8
#1 - variaveis de frases,niveis e chances do topo da listas
niveis=["facil","medio","dificil"]
espacos = ["__1__", "__2__", "__3__", "__4__"]
facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
medio_respostas=["Ares","Saga","Gemeos","Athena"]
dificil_respostas=["Shion","Aries","Saga","Gemeos"]
#2 - defina metodo selecionar_nivel() e programe ele:
apresentacao=raw_input("Bem vindo ao quiz de preenchimento de lacunas de Saint Seiya !!!  Digite a tecla enter para iniciar   ")
tentativas=raw_input("Escolha a quantidade de tentativas que deseja realizar a cada rodada do jogo  ")
nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
def game(nivel):# função para que o usuário selecione o nivel de dificuldade do quiz.
    facil="Quiz facil: O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
    medio="Quiz medio: Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
    dificil="Quiz dificil: __1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
    if  nivel=="facil":
        print facil
        resposta_L1F=raw_input("Digite a resposta para a lacuna 1 :   ").lower()
        if resposta_L1F=="ouro":
            print "resposta lacuna 1 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L1F=resposta_correta
            facil=facil.replace("__1__",resposta_L1F)
            print facil
            resposta_L2F=raw_input("Digite a resposta para a lacuna 2 :   ").lower()
        if resposta_L2F=="leao":
            print "resposta lacuna 2 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L2F=resposta_correta
            facil=facil.replace("__2__",resposta_L2F)
            print facil
            resposta_L3F=raw_input("Digite a resposta para a lacuna 3 :   ").lower()
        if resposta_L3F=="capsula do poder":
            print "resposta lacuna 3 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L3F=resposta_correta
            facil=facil.replace("__3__",resposta_L3F)
            print facil
            resposta_L4F=raw_input("Digite a resposta para a lacuna 4 :   ").lower()
        if resposta_L4F=="relampago de plasma":
            print "resposta lacuna 4 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L4F=resposta_correta
            facil=facil.replace("__4__",resposta_L4F)
            print facil
            print " Parabens , voce venceu todos os desafios do quiz nivel facil"
    if  nivel=="medio":
        print medio
        resposta_L1M=raw_input("Digite a resposta para a lacuna 1 :   ").lower()
        if resposta_L1M=="ares":
            print "resposta lacuna 1 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L1M=resposta_correta
            medio=medio.replace("__1__",resposta_L1M)
            print medio
            resposta_L2M=raw_input("Digite a resposta para a lacuna 2 :   ").lower()
        if resposta_L2M=="saga":
            print "resposta lacuna 2 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L2M=resposta_correta
            medio=medio.replace("__2__",resposta_L2M)
            print medio
            resposta_L3M=raw_input("Digite a resposta para a lacuna 3 :   ").lower()
        if resposta_L3M=="gemeos":
            print "resposta lacuna 3 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L3M=resposta_correta
            medio=medio.replace("__3__",resposta_L3M)
            print medio
            resposta_L4M=raw_input("Digite a resposta para a lacuna 4 :   ").lower()
        if resposta_L4M=="athena":
            print "resposta lacuna 4 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L4M=resposta_correta
            facil=facil.replace("__4__",resposta_L4M)
            print medio
            print " Parabens , voce venceu todos os desafios do quiz nivel medio"
    if  nivel=="dificil":
        print dificil
        resposta_L1D=raw_input("Digite a resposta para a lacuna 1 :   ").lower()
        if resposta_L1D=="shion":
            print "resposta lacuna 1 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L1D=resposta_correta
            dificil=dificil.replace("__1__",resposta_L1D)
            print dificil
            resposta_L2D=raw_input("Digite a resposta para a lacuna 2 :   ").lower()
        if resposta_L2D=="aries":
            print "resposta lacuna 2 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L2D=resposta_correta
            dificil=dificil.replace("__2__",resposta_L2D)
            print dificil
            resposta_L3D=raw_input("Digite a resposta para a lacuna 3 :   ").lower()
        if resposta_L3D=="saga":
            print "resposta lacuna 3 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L3D=resposta_correta
            dificil=dificil.replace("__3__",resposta_L3D)
            print dificil
            resposta_L4D=raw_input("Digite a resposta para a lacuna 4 :   ").lower()
        if resposta_L4D=="gemeos":
            print "resposta lacuna 4 correta!"
            resposta_correta=("!resposta correta!")
            resposta_L4D=resposta_correta
            facil=facil.replace("__4__",resposta_L4D)
            print dificil
            print " Parabens , voce venceu todos os desafios do quiz nivel dificil"
print game(nivel)

#def controlador_nivel():
    #nivel=select_nivel()
    #index=niveis.index(nivel)
    #jogar_nivel(frases[index],respostas[index],chances[index])
    #print controlador_nivel()


#frase = "Batatinha quando __1__, se esparrama pelo chão."
#palavra = "nasce"
#frase = frase.replace('__1__', palavra)
#print frase  # Vai imprimir: Batatinha quando nasce, se esparrama pelo chão."""


#3 - defina o metodo : controlador_nivel() e programe ele: aqui vc vai chamar o metodo selecionar_nivel e jogar_nivel:
#  dica: def controlador():
#           nivel=selecionar_nivel()
#           index=niveis.index(nivel)
#           jogar_nivel(frases[index],respostas[index],chances[index])
#4 - defina o metodo : jogar_nivel(frase,lista_respostas,num_chances) e programe ele:
#       dentro de jogar nivel usar o que aprendemos sala de aula: while,.replace,if,else,print,raw_input
#5 - chame o metodo controlador_nivel() para iniciar jogo:
