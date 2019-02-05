#-*- coding: utf-8 -*-
# 1-O jogo possui três ou mais níveis, e cada um contém quatro ou mais espaços em branco a serem preenchidos.
# 2-Imediatamente após rodar o programa, pede-se que o usuário selecione um grau de dificuldade, que pode ser fácil, médio ou difícil.
# 3-Após essa seleção, o jogo exibe um espaço em branco a ser preenchido no primeiro campo.
# 4-Quando um jogador acerta, aparece uma mensagem de resposta correta no espaço em branco anterior e um novo espaço para a próxima.
# 5-Quando ele erra, pede-se que tente novamente.
inicio=raw_input("Bem vindo ao quiz de Saint Seiya!!!!!!              digite a tecla enter para iniciar o quiz")
nivel=raw_input("Digite o grau de dificuldade do quiz (facil, medio ou dificil):       ").lower()

espacos = ["__1__", "__2__", "__3__", "__4__"]
facil= "O cavaleiro de __1__ de __2__, pertencente a quinta casa zodiacal, possui os golpes __3__ e __4__ ."
medio= "Conhecido como mestre __1__ , mas de verdadeiro nome __2__ de __3__, tentou assassinar __4__ ainda bebe, e enganou todo o santuario."
dificil="__1__de __2__, era o antigo mestre do santuario e tambem mestre de Mu de Aries, morto por __3__ de __4__ na revolta de Saga."
facil_respostas=["ouro","leao","capsula do poder","relampago de plasma"]
media_respostas=["Ares","Saga","Gemeos","Athena"]
dificil_respostas=["Shion","Aries","Saga","Gemeos"]
