from operator import add
import numpy as np
import module_matrix as m

##===============================================================
Material=['MNHA1234561','MNHA1234600','MNHA1234700']
SUCHBEGRIFF=['(1)','(2)','(3)']
Quantity=[['1','0','1'],['1','2','0'],['3','3','3']]
Article=['ART01','ART02','ART03']

#  Artikel = Quantity x Suchbegrif X Material

temp= m.VV_Multiply(SUCHBEGRIFF,Material)
CR= m.MV_Multiply(Quantity,temp)

##================================================================

print ("==================================================")
print ("BOM FOR SAP UPLOAD:")
print()
i=0
for item in CR:
    i+=1
    print( Article[i-1]  +"= "  +" ".join(item))
    print()

##================================================================
#  Artikel = Quantity x Suchbegrif X Material +  Quantity x Suchbegrif X Material 

Material1=['MNHA1234561','MNHA1234600','MNHA1234700']
Material2=['MPHA1234561','MNPA1234600','MPHA1234700']
#  usw.......

SUCHBEGRIFF=['(1)','(2)','(3)']


Quantity1=['1','0','1']
Quantity2=['1','2','0']


Article=['ART01','ART02','ART03']

temp1= m.VV_Multiply(SUCHBEGRIFF,Material1)
temp2= m.VV_Multiply(SUCHBEGRIFF,Material2)

temp3= m.VV_Multiply(Quantity1,temp1)
temp4= m.VV_Multiply(Quantity2,temp2)

temp5= m.VV_Add(temp3,temp4)


print ("==================================================")
print ("BOM FOR SAP UPLOAD:")
print()
i=0
for item in temp5:
    i+=1
    print( Article[i-1]  +"= "  +" ".join(item))
    print()






