def bracket(text):
    return '[' + text + ']'

def boldwrap(text): #bug na linha 4 , função definida sem os : ao final
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')
