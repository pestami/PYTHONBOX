from operator import add
import numpy as np

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

##====================================================


Material=['MNHA1234561','MNHA1234600','MNHA1234700']
SUCHBEGRIFF=['(1)','(2)','(3)']
Quantity=[['1','0','1'],['1','2','0'],['3','3','3']]
Article=['ART01','ART02','ART03']


X= VV_Multiply(SUCHBEGRIFF,Material)
CR= MV_Multiply(Quantity,X)

print ("==================================================")
print ("BOM FOR SAP UPLOAD:")
print()
i=0
for item in CR:
    i+=1
    print( Article[i-1]  +"= "  +" ".join(item))
    print()
