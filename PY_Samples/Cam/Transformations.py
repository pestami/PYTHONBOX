#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     01.07.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##=============================================================================
import numpy as np
import csv
##=============================================================================
def ExportMountingFrame(sPathFile,DataPoints):
    # field names
    fields = ['POSITION', 'X', 'Y']

    # data rows of csv file
##    DataPoints = [
##             ['TL', 'COE', '2', '9.0'],
##             ['BL', 'COE', '2', '9.1'],
##             ['BR', 'IT', '2', '9.3'],
##             ['TR', 'SE', '1', '9.5'],
##            ]

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
##=============================================================================
##=============================================================================
if __name__ == '__main__':

    # IMPORT CSV
    # These points are used to create a transformation equations

        sPathFile='datapointsCAM.csv'
        PTS_CAM=ImportMountingFrame(sPathFile)
        print('====IMPORT CSV==============================================')
        print('IMPORT CSV PTS_CAM')
        print(PTS_CAM)
        print('')


        sPathFile='geometryWORLD.csv'
        PTS_GEOM=ImportMountingFrame(sPathFile)
        print('====IMPORT CSV==============================================')
        print('IMPORT CSV PTS_CAM')
        print(PTS_CAM)
        print('')

        PTS_WORLD=PTS_GEOM
        for i in[0,1,2,3,4]:

            tempX=int(PTS_GEOM[i][1])/3 +0*int(PTS_CAM[0][1])
            tempY= int(PTS_GEOM[i][2])/3 +0*int(PTS_CAM[0][2])

            tempX=str(int(tempX))
            tempY= str(int(tempY))

            PTS_WORLD[i]=(PTS_GEOM[i][0], tempX,tempY )


# EXPORT CSV
# Assume TOP LEFT is (0,0)
#  +X axis = TL to TR
#  +Y axis = TL to BL
        sPathFile='datapointsWORLD.csv'
        ExportMountingFrame(sPathFile,PTS_WORLD)
        print('====EXPORT CSV==============================================')
        print('EXPORT CSV')
        print(PTS_WORLD)
        print('')





##=============================================================================
