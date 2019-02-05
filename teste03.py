#-*- coding: utf-8 -*-
def mostra_boas_vindas():#exibe boas vindas ao jogador
    print "Bem vindo ao quiz de Saint Seiya!!!!"
mostra_boas_vindas()
def selecionar_nivel():#pergunta a dificuldade ao usuario, retorna string com dificuldade : "facil","medio" ou "dificil"
    niveis=["facil","medio","dificil"]
    nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
    while nivel not in niveis:
        nivel=raw_input("Nivel inexistente, realize nova tentativa:    ").lower()
    print "Nivel selecionado:  " + nivel + " , responda ao seguinte quiz:"
    return nivel
nivel=selecionar_nivel() # guardei a string do nivel ( "facil ou medio ou dificil") na variavel nivel
def frase_escolhida(nivel):
    frase_facil="O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
    frase_media ="Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
    frase_dificil="__1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
    if nivel=="facil":
        return frase_facil
    if nivel=="medio":
        return frase_media
    if nivel=="dificil":
        return frase_dificil
print frase_escolhida(nivel)
frase=frase_escolhida(nivel)
def respostas_frase(frase):
    resposta_facil=["ouro","leao","capsula do poder","relampago de plasma"]
    resposta_media=["Ares","Saga","Gemeos","Athena"]
    resposta_dificil=["Shion","Aries","Saga","Gemeos"]
    repostas_lista=[resposta_facil,resposta_media,resposta_dificil]
    resposta=raw_input("Digite a resposta correta para lacuna 1:   ").lower()
    for respostas in resposta:
        if resposta==resposta_facil[0]:
            frase==frase.split()
            frase==frase.remove(3)
            frase==frase.insert(3,resposta)
            return frase
    else:
        "Resposta errada, tente novamente"




print respostas_frase(frase)
