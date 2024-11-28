#-------------------------------------------------------------------------------
# Name:        cam_export_poi.py
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
import datetime
##=============================================================================
def ExportPOIMeasurements(sPathfile_LED_EXPORT,nDataQueLocal):
    print("===EXPORT==MEASUREMENTS=TO=DELIMITED FILE=====================")

    #get current date and time
    dt = datetime.datetime.now()
    #convert date and time to string
    dateTimeStr = str(dt)
    sDateTime=dt.strftime('%Y_%m_%d_%H_%M_%S')

    file=open(sPathfile_LED_EXPORT,'w')

    for List_items in nDataQueLocal:
        sLine=''
        j=0
        for integer_items in List_items:

            if j==0:
                sLine=sDateTime + '\t' + str(integer_items)
            else:
                sLine= sLine + '\t' + str(integer_items)
            j=j+1
        file.writelines(sLine+'\n')
    file.close()

    print("--SAVED TO-------------------------------------------------")
    print(sPathfile_LED_EXPORT)
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
        print('=============')
        print('=============')
        print('==============================================================')
        print('')



##=============================================================================
##=============================================================================

if __name__ == '__main__':

    sPathfile_LED_EXPORT='garbage\\export.dat'

    lData=[[3, 20220826, 94902, 186, 147, 131],
             [2, 20220826, 94902, 243, 243, 243],
             [1, 20220826, 94902, 247, 233, 244],
             [0, 20220826, 94902, 132, 124, 121],
             [3, 20220826, 94857, 186, 147, 131],
             [2, 20220826, 94857, 243, 243, 243],
             [1, 20220826, 94857, 247, 233, 244],
             [0, 20220826, 94857, 132, 124, 121],
             [3, 20220826, 94852, 186, 147, 131],
             [2, 20220826, 94852, 243, 243, 243],
             [1, 20220826, 94852, 247, 233, 244],
             [0, 20220826, 94852, 132, 124, 121],
             [3, 20220826, 94847, 186, 147, 131],
             [2, 20220826, 94847, 243, 243, 243],
             [1, 20220826, 94847, 247, 233, 244],
             [0, 20220826, 94847, 132, 124, 121],
             [3, 20220826, 94842, 186, 147, 131],
             [2, 20220826, 94842, 243, 243, 243],
             [1, 20220826, 94842, 247, 233, 244],
             [0, 20220826, 94842, 132, 124, 121],
             [3, 20220826, 94837, 186, 147, 131],
             [2, 20220826, 94837, 243, 243, 243],
             [1, 20220826, 94837, 247, 233, 244],
             [0, 20220826, 94837, 132, 124, 121],
             [3, 20220826, 94832, 186, 147, 131],
             [2, 20220826, 94832, 243, 243, 243],
             [1, 20220826, 94832, 247, 233, 244],
             [0, 20220826, 94832, 132, 124, 121],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]




    print('')
    print('==============================================================')
    print('====TEST THE PROGRAM =======================')
    print('==============================================================')
    print('')

    sPrefix='workspace_1X2'+'\\'
    sPrefix='MPA\\'

##    main(sPrefix)

    ExportPOIMeasurements(sPathfile_LED_EXPORT,lData)

    print('')
    print('==============================================================')