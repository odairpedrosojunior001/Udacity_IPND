s = "any string" # .find utilizado em uma variavél s
print s.find("t")
print s.find(s)
print "s".find("s")
print s.find(s+"!!!")+1
print s.find('')
print "Example 1: Finding substrings in a string" #Encontrando substrings em uma string
print "test".find("te")
print "test".find("st")
print "test"[2:]
print "Example 2: Finding substrings in a string which is stored as a variable"#Encontrar substrings em uma string que é armazenada como uma variável
my_string = "test"
print my_string.find("te")
my_string = "test"
print my_string.find("st")
print my_string[2:]
print "Example 3: Printing out everything after a certain substring"#Imprimindo tudo depois de uma certa substring
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color
print favorite_color[7:]
print "Example 4: Other interesting things about string.find()..."#Outras coisas interessantes sobre string.find ()
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1
print "Example 1: using find to print the second occurrence of a sub-string"#usando find para imprimir a segunda ocorrência de uma subcadeia
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
