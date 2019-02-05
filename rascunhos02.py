#-*- coding: utf-8 -*-
resposta=raw_input("Digite a resposta correta para lacuna 1 :   ").lower()
def resposta_frase(resposta):
    frase="O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
    resposta_certa=["ouro","leao","capsula do poder","relampago de plasma"]
    lacunas=["__1__","__2__","__3__","__4__"]
    if resposta==resposta_certa[0]:
        resposta="(resposta certa)"
        lacuna=lacunas[0]
        nova_frase=frase.replace(lacuna,resposta)
        print "Resposta correta!!!"
        return nova_frase
    else:
        return "Tente novamente"
    
print resposta_frase(resposta)
#lacuna1="__1__"
#resposta1="ouro"
#lacuna2="__2__"
#resposta2="leao"
#nova_frase=frase.replace(lacuna,resposta)

#print nova_frase
