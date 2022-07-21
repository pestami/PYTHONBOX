#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     23.06.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
##=============================================================================
import numpy as np
import cv2
import csv
##=============================================================================

def ExportMountingFrame(sPathFile,DataPoints):

    print(DataPoints)
    # field names
    fields = ['POSITION', 'X', 'Y']

    with open(sPathFile, 'w',newline='') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(DataPoints )





def ImportMountingFrame(sPathFile):

    with open(sPathFile, mode ='r') as csvfile:

            csvReader = csv.reader(csvfile, delimiter=',')
            i=0
            MP_WORLD=[]
            for row in csvReader:
                print(row)

                MP_WORLD=  MP_WORLD + [(row[0],row[1],row[2])]
                i=i+1
    return MP_WORLD

##=============================================================================

X1=[0,1,0,0,0]
Y1=[0,1,0,0,0]

DataPoints= [
             ('TL',X1[1],Y1[1]),
             ('BL',X1[2],Y1[2]),
             ('BR',X1[3],Y1[3]),
             ('TR',X1[4],Y1[4])
            ]


# EXPORT CSV
print('====EXPORT CSV==================================================')
sPathFile='datapointsCAM.csv'
ExportMountingFrame(sPathFile,DataPoints)

print('')

# IMPORT CSV
print('====IMPORT CSV==================================================')
sPath='C:\\Users\\sesa237770\\Documents\\GITBOX\\Snippets_py\\Cam'
sFile='datapointsWORLD.csv'
sPathFile=sPath +'\\'+sFile

MP_WORLD= ImportMountingFrame(sPathFile)
print('')

print(MP_WORLD)

##=============================================================================

print('====PROGRAM COMPLETED==================================================')














