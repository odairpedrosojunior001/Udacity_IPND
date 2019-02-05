# coding=utf-8
nivel = raw_input('Escolha um dos seguintes niveis -> facil/ medio/ dificil: ').lower()
def obter_frase_lacuna_resposta(nivel):
    if nivel=="facil":
        facil="O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
        espacos = ["__1__", "__2__", "__3__", "__4__"]
        facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
        return facil,espacos,facil_respostas
print obter_frase_lacuna_resposta(nivel)
