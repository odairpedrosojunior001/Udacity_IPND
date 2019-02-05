#-*- coding: utf-8 -*-
i = 0 # loop while exemplo
while i != 10:
    i = i + 1
    print i


def remove_spaces(text): #remover os espaços de uma string qualquer
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")
