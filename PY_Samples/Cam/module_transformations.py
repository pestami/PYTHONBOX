#-------------------------------------------------------------------------------
# Name:        module_transformations.py
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
import os
##=============================================================================
#========================================================
#========================================================
class transformation:
    ##  Class variables: This variable is shared between all objects of a class
    PTS_XY_IN=[['POSITION', 'X', 'Y']]
    PTS_XY_OUT =[['POSITION', 'X', 'Y']]
    PTS_WORLD_IN_CAM = [['POSITION', 'X', 'Y']]

    Tij=np.array([[1,0],[0,1]])
    Di=np.array([0,0])

#========================================================
    def __init__(self, PTS_XY_IN,PTS_XY_OUT):

        ## class attributes
        self.PTS_XY_IN=PTS_XY_IN
        self.PTS_XY_OUT =PTS_XY_OUT
#-------------------------------------------------------
    def Build_TransMatrix_scaling(self,PTS_CAM ,PTS_GEOM):


        print('=====Build_TransMatrix_scaling================')
        LXgeo=float(PTS_GEOM[0][1]) -float(PTS_GEOM[3][1])
        LXcam=float(PTS_CAM[0][1]) -float(PTS_CAM[3][1])
        LYgeo=float(PTS_GEOM[0][2]) -float(PTS_GEOM[2][2])
        LYcam=float(PTS_CAM[0][2]) -float(PTS_CAM[2][2])
        scaleX= round(LXcam/LXgeo,2)
        scaleY= round(LYcam/LYgeo,2)

        offsetX=round(float(PTS_CAM[0][1])-float(PTS_GEOM[0][1]),2)
        offsetY=round(float(PTS_CAM[0][2])-float(PTS_GEOM[0][2]),2)

        self.Tij=np.array([[scaleX,0],[0,scaleY]])
        self.Di=np.array([offsetX,offsetY])
#-------------------------------------------------------
    def Build_TransMatrix_elastic(self,PTS_CAM_LT ,PTS_GEOM_LT):

## LineaR TRANSFORMATION  3 UNKNOWN  require 3 equations , 4 equations are available
## choice of equations influences the solution accuracy
##  X' = aX + bY + m
##  Y' = cX + dY + n
##  Xi' = aXi + bYi + m
##  Yi' = cXi + dYi + n
## [X1',Y1',X2',Y2',X3',Y3'] = [POINTSij] * [a,b,c,d,m,n]

##        PTS_GEOM = [list(ele) for ele in PTS_GEOM_LT]
        PTS_GEOM= PTS_GEOM_LT.copy()
        PTS_CAM= PTS_CAM_LT.copy()
        print('=====Build_TransMatrix_elastic================')
        print(PTS_GEOM)
        print('VECTOR:')
        print(PTS_CAM)
        print('')
        x=1

        POINTSij=[
        [float(PTS_GEOM[0][1]),float(PTS_GEOM[0][2]),0,0,1,0],
        [0,0,float(PTS_GEOM[0][1]),float(PTS_GEOM[0][2]),0,1],

        [float(PTS_GEOM[1][1]),float(PTS_GEOM[1][2]),0,0,1,0],
        [0,0,float(PTS_GEOM[1][1]),float(PTS_GEOM[1][2]),0,1],

        [0,0,float(PTS_GEOM[2][1]),float(PTS_GEOM[2][2]),1,0],
        [float(PTS_GEOM[2][1]),float(PTS_GEOM[2][2]),0,0,0,1]]

        POINTSi=[
        float(PTS_CAM[0][1]),
        float(PTS_CAM[0][2]),
        float(PTS_CAM[1][1]),
        float(PTS_CAM[1][2]),
        float(PTS_CAM[2][1]),
        float(PTS_CAM[2][2])
        ]

        np.set_printoptions(precision=1)
        np.set_printoptions(suppress=True)
        print('=====Linear Equations================')
        print(POINTSij)
        print('VECTOR:')
        print(POINTSi)


        INV_POINTSij = np.linalg.inv(POINTSij)

        Mi=INV_POINTSij.dot(POINTSi)

        print('=====Mi Solution ================')
        print(Mi)

        print('=====INV_POINTSij * POINTSij================')

        print(INV_POINTSij.dot(POINTSij))

        self.Tij=np.array([[Mi[0],Mi[1]],[Mi[2],Mi[3]]])
        self.Di=np.array([Mi[4],Mi[5]])

        if 1==1 :
            self.Tij=np.array([[1,0],[0,1]])
            self.Di=np.array([0,0])

        print('=====================================')



#-------------------------------------------------------
    def transform_WORLD_TO_CAM(self,PTS_GEOM):
        print('============================================================')
        print('=====transform_World_to_CAM_by_scale========================')
        print('')
        PTS_CAM =PTS_GEOM.copy()
        print(PTS_CAM)
        j=0

        for i in range(0,len(PTS_GEOM)):

                print("Count i:",i)
                print(PTS_GEOM)
                print('')

                Xj=np.array([float(PTS_GEOM[i][1]),float(PTS_GEOM[i][2])])

                x2j=self.Tij.dot(Xj) +  self.Di

                PTS_CAM[i][1]= str(int(x2j[0]))

                PTS_CAM[i][2]= str(int(x2j[1]))
        print('===========================================================')


        return PTS_CAM
#----------------------------------------------------------
##=============================================================================
##=============================================================================
##=============================================================================
def main():

##=============================================================================
    print('')
    print('==============================================================')
    print('====Calculate the Transformation Equations====================')
    print('====COnvert job list from WORLD to CAMERA COORDINATES=========')
    print('==============================================================')
    print('')
#----------------------------------------------------------


    print('')
    print('====================================================')
    print('====TEST THE PROGRAM =======================')
    print('====================================================')
    print('')
    PTS_CAM=[
    ['TL','39','56'],
    ['BL','43','366'],
    ['BR','607','358'],
    ['TR','596','51']]

    PTS_GEOM =[
    ['TL', '0', '0'],
    ['BL', '0', '75'],
    ['BR', '140', '75'],
    ['TR', '140', '0'] ]

# test for unity matrix
    if 1==1:
     PTS_GEOM = PTS_CAM.copy()


    PTS_WORLD_IN_CAM = [
    ['LED_OFF', '50', '25', '10'],
    ['LED01', '40', '38', '20'],
    ['LED02', '100', '38', '20'],
    ['LED03', '20', '47', '20']]

    oTRANS=transformation(PTS_CAM,PTS_GEOM)
    print('')
    print('UNITY MATRICES')
    print('MATRIX Tij= ')
    print(oTRANS.Tij)
    print('MATRIX Di= \n',oTRANS.Di)


    if 1==1:
        oTRANS.Build_TransMatrix_elastic(PTS_CAM,PTS_GEOM)
    else:
        oTRANS.Build_TransMatrix_scaling(PTS_CAM,PTS_GEOM)

    print('')
    print('TRANSFORMATION MATRICES')
    print('MATRIX Tij= ')
    print(oTRANS.Tij)
    print('MATRIX Di= \n',oTRANS.Di)

    print('')
    print('Transform to CAM')
    PTS_WORLD_IN_CAM =  oTRANS.transform_WORLD_TO_CAM(PTS_WORLD_IN_CAM)
    print('POINTS PTS_CAM= ')
    print(PTS_WORLD_IN_CAM)

##=============================================================================

if __name__ == '__main__':

    main()







