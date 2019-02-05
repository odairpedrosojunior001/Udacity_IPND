def printExample(a, b): # exemplo de erro / debug :
    print a + b

def printInches(n):
    print n + " inches" #TypeError: unsupported operand type(s) for +: 'int' and 'str'

printExample(17, 23)
printExample('long', 'word')
printInches(42)

def printExample(a, b): # exemplo de erro / debug : correção str + int declarando str na variavel
    print a + b

def printInches(n):
    print str(n) + " inches" #correção str + int declarando str na variavel

printExample(17, 23)
printExample('long', 'word')
printInches(42)
