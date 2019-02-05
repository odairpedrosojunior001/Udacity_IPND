#-*- coding: utf-8 -*-
def mostra_boas_vindas():#exibe boas vindas ao jogador
    print "Bem vindo ao quiz de Saint Seiya!!!!"
mostra_boas_vindas()
def pergunta_dificuldade():#pergunta a dificuldade ao usuario, retorna string com dificuldade : "facil","medio" ou "dificil"
    niveis=["facil","medio","dificil"]
    nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
    while nivel not in niveis:
        nivel=raw_input("Nivel inexistente, realize nova tentativa:    ").lower()
    print "Nivel selecionado:  " + nivel + " , responda ao seguinte quiz:"
    return nivel
nivel=pergunta_dificuldade()
def obter_frase_lacuna_resposta(nivel):
    if nivel=="facil":
        facil="O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
        espacos = ["__1__", "__2__", "__3__", "__4__"]
        facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
        print facil
        return facil,espacos,facil_respostas
    if nivel=="medio":
        medio="Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
        espacos = ["__1__", "__2__", "__3__", "__4__"]
        medio_respostas=["Ares","Saga","Gemeos","Athena"]
        print medio
        return medio,espacos,medio_respostas
    if nivel=="dificil":
        dificil="__1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
        espacos = ["__1__", "__2__", "__3__", "__4__"]
        dificil_respostas=["Shion","Aries","Saga","Gemeos"]
        print dificil
        return dificil,espacos,dificil_respostas
frase_nivel,lacunas,resposta_nivel=obter_frase_lacuna_resposta(nivel)
def frase_lacuna_resposta(lacunas,frase_nivel,resposta_nivel):#pergunta a resposta para uma lacuna , retorna quando resposta esta resposta_correta
    resposta_usuario=raw_input("Digite o valor da lacuna" +  lacuna  ).lower()
    for index,respostas in resposta_nivel:
        if resposta==resposta_facil[0]:
            frase==frase.split()
            frase==frase.remove(3)
            frase==frase.insert(3,resposta_usuario)
            return frase_nivel
    else:
        "Resposta errada, tente novamente"

print frase_lacuna_resposta(lacunas,frase_nivel,resposta_nivel)
    #resposta_usuario=raw_input("Digite o valor da lacuna" + lacuna )  .lower()
    #while resposta_usuario != resposta:
        #resposta_usuario=raw_input("Sua resposta esta errada, tente novamente :  "   ).lower()
    #print "Voce acertou !!!"
    #return resposta_usuario
#inputs=lacuna(lista)que deve ser substituida ; frase(string ) de resposta certa
#outputs= string (resposta correta dada pelo usuario)
#print frase_lacuna_resposta(lacunas,frase_nivel)
#def substitui_lacuna_por_resposta(frase,lacuna,resposta):
    #return frase
#def mostra_parabens_final(frase):
    #print "parabéns, voce superou os desafios do quiz!!!"


#previa do programa com funçoes falsas:
#def iniciar_jogo():
    #mostra boas vindas() - ok
    #dificuldade = pergunta_dificuldade() - ok
    #frase,lacuna=obtem_frase_dificuldade(dificuldade)
    #for lacuna in lacunas:
        #print frase
        #resposta=pergunta_resposta_lacuna(lacuna)
        #frase=substitui_lacuna_por_resposta(frase,lacuna,resposta)
    #mostra_parabens_final(frase)
#iniciar_jogo()

#dicas
# raw_input() - exibe uma mensagem, captura o input do usuario, e o exibe como uma string
# string.lower() - converte uma string para letras minusculas
# for index, item in enumerate(list): Percorre uma lista obtendo o item e o indice da vez
# string.replace(part,replacement): Substitui um pedaço de string por outra string
# coding=utf-8
