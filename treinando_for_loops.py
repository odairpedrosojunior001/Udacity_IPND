print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2: # cria uma variavel para toda lista de listas.
    country = country_with_capital[0]       # cria uma variavel separando somente os paises da lista de listas.
    capital = country_with_capital[1]       # cria uma variavel somente com as capitais da lista de listas.
    print capital + ' is the capital of ' + country  # manipula a lista e variaveis criando 3 frases.
