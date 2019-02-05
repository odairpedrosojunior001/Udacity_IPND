#-*- coding: utf-8 -*-
# Now, we want to ask ourselves the question: How many occurrences of
# the number 9 appear in our randomly made list?
#
# For example, if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to loop through the list and count the number of occurrences of the
# number 9. In the example list above, the number 9 occurs three times.

import random

# 1. Create random list of integers using while loop
random_list = []
list_length = 20

count=0
index=0

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
  if random_list[index]==9:
        count=count+1
        index=index+1
# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.
# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.

print random_list
print count

"""método para contar os "U" em uma lista usando "for"
# def measure_udacity(p):
#    count=0
#    for e in p:
#        if e[0]=="U":
#            count=count+1
#    return count
#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0
#print measure_udacity(['Umika','Umberto'])
#>>> 2"""

"""código completo usando indice:
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1"""
