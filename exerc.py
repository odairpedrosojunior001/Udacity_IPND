# exercicio: imprimir udacious sem usar caracter de aspas.
S ="udacity"
T ="bodacius"
print S[0:4]+T[1]+T[6:8]

sentence = "A NOUN went on a walk."   #corte e mostre tudo que vem depois de A NOUN
substring = sentence[6:]
print substring
#Corte a string sentence e coloque tudo antes de "NOUN" em substring1,
# tudo entre "NOUN" e "VERB" em substring2 e tudo depois de "VERB" na substring3.
sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]
print substring1
print substring2
print substring3
#Armazene, nas variáveis noun_replacement e verb_replacement,
#strings contendo um substantivo e um verbo à sua escolha.
#Depois, concatene as variáveis substring1, noun_replacement, substring2, verb_replacement e substring3,
#de forma a montar uma frase. Guarde o resultado em new_sentence, respeitando a mesma ordem da variável sentence.
#Dica: a += b é uma abreviação para a = a + b. As duas linhas de código a seguir são equivalentes:
#new_sentence += substring1
#new_sentence = new_sentence + substring1
sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]
noun_replacement="ball"
verb_replacement="play"
