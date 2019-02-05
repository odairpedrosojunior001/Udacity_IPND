#-*- coding: utf-8 -*-
espacos = ["__1__", "__2__", "__3__", "__4__"]
facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
media_respostas=["Ares","Saga","Gemeos","Athena"]
dificil_respostas=["Shion","Aries","Saga","Gemeos"]



def inicio_game():
    apresentacao=raw_input("Bem vindo ao quiz de preenchimento de lacunas de Saint Seiya !!!  Digite a tecla enter para iniciar   ")
inicio_game()

def select_level():
    nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
    facil="Quiz facil: O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
    medio="Quiz medio: Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
    dificil="Quiz dificil: __1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
    niveis=["facil","medio","dificil"]
    if nivel==niveis[0]:
        print facil
    if nivel==niveis[1]:
        print medio
    if nivel==niveis[2]:
        print dificil
select_level()
