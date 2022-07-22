#-------------------------------------------------------------------------------
# Name:        Transformations.py
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
import os
from module_transformations import transformation
##=============================================================================
def ExportMountingFrame(sPathFile,DataPoints):
    # field names
    ##    fields = ['POSITION', 'X', 'Y']
    # data rows of csv file
    ##    DataPoints = [
    ##
    ##             ['BL', 'COE', '2', '9.1'],
    ##             ['BR', 'IT', '2', '9.3'],
    ##             ['TR', 'SE', '1', '9.5'],
    ##             ['TL', 'COE', '2', '9.0'],
    ##            ]
    with open(sPathFile, 'w',newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
    ##        write.writerow(fields)
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
#========================================================
#========================================================

#----------------------------------------------------------
##=============================================================================
##=============================================================================
##=============================================================================
def main(sPrefix_in):
##        user = os.getlogin()
##        if user=='SESA237770':
##            sPrefix='MPA\\'
##        else: sPrefix='OJS\\'


        # Choose WORKSPACE"
        sPrefix=sPrefix_in


        print('')
        print('==============================================================')
        print('====Calculate the Transformation Equations====================')
        print('====COnvert job list from WORLD to CAMERA COORDINATES=========')
        print('==============================================================')
        print('')

    # IMPORT CSV
    # These points are used to create a transformation equations
        sPathFileImport_FRAME_CAMERA=sPrefix + 'MountingFrame_CAMERA.csv'
        sPathFileImport_FRAME_WORLD=sPrefix + 'MountingFrame_WORLD.csv'
        sPathFileImport_FRAME_TRANS_WORLD=sPrefix + 'MountingFrame_TRANS_WORLD.csv'

        sPathFileImport_LED_WORLD=sPrefix + 'LED_WORLD.csv'
        sPathFileImport_TRANS_LED_WORLD=sPrefix + 'LED_TRANS_WORLD.csv'

##        WORLDS=[sPathFileImportWORLD,sPathFileImportWORLD2]
##        TRANS_WORLDS=[sPathFileImportTRANS_WORLD,sPathFileImportTRANS_WORLD2]

        print('====IMPORT CSV==============================================')
        print('IMPORT CSV MountingFrame Points from CAMERA   PTS_CAM_FRAME')
        sPathFile=sPathFileImport_FRAME_CAMERA
        PTS_CAM_FRAME=ImportMountingFrame(sPathFile)
##        print(PTS_CAM)

        print('====IMPORT CSV==============================================')
        print('IMPORT WORLD MountingFrame Points from WORLD   PTS_GEOM_FRAME')
        sPathFile=sPathFileImport_FRAME_WORLD
        PTS_GEOM_FRAME=ImportMountingFrame(sPathFile)
##        print(PTS_PIXEL_GEOM)

        print('====IMPORT CSV==============================================')
        print('IMPORT WORLD LED Points from WORLD   PTS_GEOM_LED')
        sPathFile=sPathFileImport_LED_WORLD
        PTS_GEOM_LED=ImportMountingFrame(sPathFile)
##        print(PTS_PIXEL_GEOM)



        LL_PTS_CAM_FRAME = [list(ele) for ele in PTS_CAM_FRAME]
        LL_PTS_GEOM_FRAME = [list(ele) for ele in PTS_GEOM_FRAME]
        oTRANS=transformation(LL_PTS_CAM_FRAME,LL_PTS_GEOM_FRAME)

        oTRANS.Build_TransMatrix_scaling(LL_PTS_CAM_FRAME,LL_PTS_GEOM_FRAME)
        if 1==2 :  # debug
            oTRANS.Build_TransMatrix_scaling(LL_PTS_CAM_FRAME,LL_PTS_CAM_FRAME)
        if 1==1 :  # flag
            oTRANS.Build_TransMatrix_elastic(LL_PTS_CAM_FRAME,LL_PTS_GEOM_FRAME)

        print('\n====Transformation Equations====')
        print('',LL_PTS_CAM_FRAME)
        print('',LL_PTS_GEOM_FRAME)

        print('TRANSFORMATION MATRICES')
        print('MATRIX Tij= ')
        print(oTRANS.Tij)
        print('MATRIX Di= \n',oTRANS.Di)
        print('===============================\n')


        PTS_TRANS_GEOM_LED=PTS_GEOM_LED.copy()

#------DATA STRUCTURE CONVERSION   LIST TUPLES  to LIST LIST
# https://www.geeksforgeeks.org/python-convert-list-of-lists-to-tuple-of-tuples/
# https://www.geeksforgeeks.org/python-convert-list-of-tuples-to-list-of-list/

##          [('LED_OFF', '50', '25'),
##          ('LED01', '40', '38'),
##          ('LED02', '100', '38'),
##          ('LED03', '20', '47')]

##                [['TL', '42', '58'],
##                 ['BL', '42', '157'],
##                 ['BR', '199', '162'],
##                 ['TR', '203', '57'] ]
#------DATA STRUCTURE CONVERSION   LIST LIST to  LIST TUPLES

        LL_PTS_GEOM_LED = [list(ele) for ele in PTS_GEOM_LED]
        LL_PTS_TRANS_GEOM_LED =  oTRANS.transform_WORLD_TO_CAM(LL_PTS_GEOM_LED)
        PTS_TRANS_GEOM_LED=res = list(tuple(sub) for sub in LL_PTS_TRANS_GEOM_LED)

        LL_PTS_GEOM_FRAME = [list(ele) for ele in PTS_GEOM_FRAME]
        LL_PTS_TRANS_GEOM_FRAME =  oTRANS.transform_WORLD_TO_CAM(LL_PTS_GEOM_FRAME)
        PTS_TRANS_GEOM_FRAME=res = list(tuple(sub) for sub in LL_PTS_TRANS_GEOM_FRAME)


        print('====EXPORT CSV==========')
        print('EXPORT TRANS FRAME CAMERA')
        sPathFile=sPathFileImport_FRAME_TRANS_WORLD
        print('File:', sPathFile)
        ExportMountingFrame(sPathFile,PTS_TRANS_GEOM_FRAME)
        [print(i) for i in PTS_TRANS_GEOM_FRAME]
        print('')
        print('===========================================================')



        print('====EXPORT CSV==========')
        print('EXPORT TRANS LED GEOMETRY')
        sPathFile=sPathFileImport_TRANS_LED_WORLD
        print('File:', sPathFile)
        ExportMountingFrame(sPathFile,PTS_TRANS_GEOM_LED)
        [print(i) for i in PTS_TRANS_GEOM_LED]
        print('')
        print('===========================================================')

##=============================================================================
##=============================================================================

if __name__ == '__main__':

    print('')
    print('==============================================================')
    print('====TEST THE PROGRAM =======================')
    print('==============================================================')
    print('')

    sPrefix='workspace_1X2'+'\\'
    main(sPrefix)

    sPrefix='MPA\\'
    sPathFileImport=sPrefix + 'MountingFrame_TRANS_WORLD.csv'
    sPathFileExport=sPrefix + 'MountingFrame_CAMERA.csv'

    sPathFileCAM=sPathFileImport
    sPathFileWORLD=sPathFileExport

    print( 'PATHS = ' , sPathFileCAM )
    print( 'PATHS = ' , sPathFileWORLD )


##    transform_WORLD_IN_CAM_byscale(self,PTS_GEOM,PTS_CAM)


