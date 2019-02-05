#-*- coding: utf-8 -*-
# multiplicar os valores de uma lista
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    total=1
    for i in list_of_numbers:
        total= total*i
    return total



print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1
