s = "any string" #uso de .find em uma variavel contendo uma string
print s.find("t")
print s.find(s)
print "s".find("s")
print s.find(s+"!!!")+1
print s.find('')
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print "Example 1: Finding substrings in a string" #exemplo 1 : encontrando substrings dentro de uma string
print "test".find("te")
print "test".find("st")
print "test"[2:]
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print "Example 2: Finding substrings in a string which is stored as a variable" #exemplo 2. uso .find em uma string usando variavel
my_string = "test"
print my_string.find("te")
my_string = "test"
print my_string.find("st")
print my_string[2:]
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print "Example 3: Printing out everything after a certain substring"#exemplo3: .find aplicado a string longa e variavel contendo outra string longa.
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color
print favorite_color[7:]
