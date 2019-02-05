#-*- coding: utf-8 -*-
niveis=["facil","medio","dificil"]
espacos = ["__1__", "__2__", "__3__", "__4__"]

facil= "O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
medio= "Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
dificil="__1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
media_respostas=["Ares","Saga","Gemeos","Athena"]
dificil_respostas=["Shion","Aries","Saga","Gemeos"]
# TAREFA 2
# TODO: Crie uma função pra dar início à partida.
# O jogador deve escolher entre os níveis 'fácil', 'médio', 'difícil', ou similar.
# IMPORTANTE: Veja que comecei a esboçar uma documentação para a função abaixo,
# É fundamental se familiarizar com as boas práticas, uma delas é comentar sua função
apresentacao=raw_input("Bem vindo ao quiz de Saint Seiya !!!       digite a tecla enter para iniciar")
nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
def select_level(nivel):
    if nivel=="facil":
        return facil
    if nivel=="medio":
        return medio
    if nivel=="dificil":
        return dificil
    return " nivel inexistente"
print select_level(nivel)
