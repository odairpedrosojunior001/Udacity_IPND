#-*- coding: utf-8 -*-
#traz a frase, lacunas e respostas para dificuldade x.Dificuldade ="string" ;"facil","medio","dificil"
#return = string (frase com lacunas 1/4) ; list(lista de lacunas da frase) ; list(lista de respostas para cada lacuna)
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
pergunta_dificuldade()
def obter_frase_lacuna_resposta(nivel):
    if nivel=="facil":
        facil="O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
        espacos = ["__1__", "__2__", "__3__", "__4__"]
        facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
        return facil,espacos,facil_respostas
print obter_frase_lacuna_resposta(nivel)
#    """"if nivel=="medio":
#        medio="Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
#        espacos = ["__1__", "__2__", "__3__", "__4__"]
#        medio_respostas=["Ares","Saga","Gemeos","Athena"]
#        return medio,espacos,medio_respostas
#    if nivel=="dificil":
#        dificil="__1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
#        espacos = ["__1__", "__2__", "__3__", "__4__"]
#        dificil_respostas=["Shion","Aries","Saga","Gemeos"]
#        return dificil,espacos,dificil_respostas
#print obter_frase_lacuna_resposta(nivel):""""
#def pergunta_resposta_lacuna(lacuna):
#"""    #return "resposta certa"""
#inputs=
#outputs=

#def substitui_lacuna_por_resposta(frase,lacuna,resposta):
    #return frase
#def mostra_parabens_final(frase):
    #print "parabéns, voce superou os desafios do quiz!!!"

# raw_input() - exibe uma mensagem, captura o input do usuario, e o exibe como uma string
# string.lower() - converte uma string para letras minusculas
# for index, item in enumerate(list): Percorre uma lista obtendo o item e o indice da vez
# string.replace(part,replacement): Substitui um pedaço de string por outra string
