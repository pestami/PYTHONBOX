from operator import add


def VV_Multiply(a,b):
    DELIMITER=[' ',' ',' ']
    CR=[]
    b=list( map(add, DELIMITER,b))
    c=list( map(add, a,b))
    return c

def MV_Multiply(a,b):
    DELIMITER=[' ',' ',' ']
    CR=[]
    b=list( map(add, DELIMITER,b))
    for item in a:
        C=list( map(add, item,b) )
        CR.append( C)
    return CR

def VV_Add(a,b):
    CR=[]
    for item in a:
        C=list( map(add, item,b) )
        CR.append( C)
    return CR

##====================================================
