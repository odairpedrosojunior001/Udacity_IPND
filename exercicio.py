print 'hello world'
# 1 dia = 60*24 = 1440 minutos
# 1 semana = 1440*7 = 10080
# 7 semanas = 10080 * 7 = 70560 minutos
print 60*24*7*7
d=(299792458*100)*(1.0/1000000000)
print d
print 5/2
print 5.0/2
print 5/2.0
print 5.0/2.0

print 1
print  2
print   3
print     4
print        5
print              6
print                       7
print                                     8
print                                                          9
vel_luz=299792458
print vel_luz
bilionesimo=(1.0/1000000000)
print bilionesimo
nanostick=vel_luz*bilionesimo*100
print nanostick
print "Ola"
print"peppa pig"
name="Odair"
print "Obrigado, "+name+"!"+"!"+"!" #concatenar strings
print name  +"?"*55
nome = "Maria"+" Eduarda"+" Pedroso "
print nome*10
name = "Andy"
print "Hello " + name
print name * 4
print 4
print "4"
print 4 + 4
print "4" + "4"
s = '<any string>'
print s[0]
print (s + s)[0]
print s[0]
print s[1] + s[0 +1 ]
print s[1]
print (s + "ity")[1]
print s[-1]
print (s+s)[-1]
print s[0]+s[1]
print s[0+1]
print s[0]
print (s + s)[0]
print s[3]
print s[1+1+1]
#subsequencias de strings:
#( dada uma string, selecionar intervalos de caracteres)
nome= "Odair Pedroso Junior"
print nome[0:5]
nome = "Maria Eduarda"
print nome[4:8]
print nome[4:]
s = 'audacity'
print "U" + s[2:]
s = "any string"
print s[0:]
print s[:-1]
s = "any string"
print s.find(s)
print "s".find("s")
print s.find(s+"!!!")+1
print s.find('')
# testes exemplo com string.find
print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]
print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
my_string = "test"
print my_string.find("st")
print my_string[2:]
print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color
print favorite_color[7:]
print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1
# mais exercicios com strings
print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)
print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.
print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string
#ecercicio
# Write Python code that prints out the number of hours in 7 weeks.
# 1 semana = 7 dias
# 1 dia = 24hs

# exercicio:
S = 'udacity'
T = 'bodacious'
#Escreva o código Python que imprime udacious sem usar nenhum caractere de citação em seu código.
print S[0:4]
