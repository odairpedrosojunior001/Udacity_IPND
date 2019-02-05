#-*- coding: utf-8 -*-Defina uma função, median, que recebe três números e devolve a mediana dos três.
def median(x,y,z):
    if x<y and y<z or y<x and y>z:
        return y
    if z<x and z>y or z>x and z<y:
        return z
    if x>y and x<z or x<y and x>z:
        return x
    if x<y and y==z:
        return z
    if x==y and x>z:
        return x
    if x==z and x>y:
        return x
    if x==y and x<z:
        return y
    if x==z and x<y:
        return x
    if x>y and y==z:
        return z
    if x==y and y==z:
        return y
print median(1,2,3)#r=2
print median(9,3,6)#r=6
print median(7,8,7)#r=7
print median(1,3,2)#r=2
print median(2,1,3)#r=2
print median(1,2,2)#r=2
print median(2,2,1)#r=2
print median(2,1,2)#r=2
print median(2,2,3)#r=2
print median(3,2,2)#r=2
print median(2,2,2)#r=2
print median(7,0,9)
print median(0,9,6)
