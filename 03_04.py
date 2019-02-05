#-*- coding: utf-8 -*-
apresentacao=raw_input("Bem vindo ao quiz de Saint Seiya !!!       digite a tecla enter para iniciar")
nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
niveis=["facil","medio","dificil"]
espacos = ["__1__", "__2__", "__3__", "__4__"]
facil= "O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
medio= "Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
dificil="__1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
media_respostas=["Ares","Saga","Gemeos","Athena"]
dificil_respostas=["Shion","Aries","Saga","Gemeos"]
def select_level(niveis):
    for item in niveis:
        print item
