def biggest (x,y,z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
    if x==y or x==z:
        return x
    if y==z:
        return y
print biggest (10,11,11)
