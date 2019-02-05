print "Example 3: Printing out everything after a certain substring"#exemplo 3 modificado para estudo,dada uma variavel e uma string,
                                                                    #transformar em diversas variaveis com partes da string inicial.
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
print color_start_location
favorite_color = my_string[color_start_location:]
print favorite_color
print favorite_color[7:]
