#-------------------------------------------------------------------------------
# Name:        cam_annotate.py
# Purpose:
#
# Author:      SESA237770
#
# Created:     06.07.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cv2
import csv
# import cam_annotate   # copy pase


class cam_annotate:

#========================================================
    def circle(oCV2,image):

##      cv2.circle(grey_img_2,(int(POINT[1]),int(POINT[2])), 10, (0,255,0),1)

        oCV2.circle(image,(200,200), 100, (0,255,100),1)

        return image


#========================================================

class data_points:

    aPOINTS_GLOBAL=[]

# data rows of csv file
##    DataPoints = [
##             ['TL', 'COE', '2', '9.0'],
##             ['BL', 'COE', '2', '9.1'],
##             ['BR', 'IT', '2', '9.3'],
##             ['TR', 'SE', '1', '9.5'],
##            ]
#========================================================
    def __init__(self, sPathFile):

        aPOINTS =data_points.ImportFrame(sPathFile)
        self.aPOINTS_=aPOINTS
#-------------------------------------------------------
    @classmethod
    def setGlobal(blabla):
        blabla.aPOINTS_GLOBAL="GLOBAL1"
#-------------------------------------------------------
    def setGlobal2(self):
        self.__class__.aPOINTS_GLOBAL="GLOBAL2"

#-------------------------------------------------------
    def ImportFrame(sPathFile):
         with open(sPathFile, mode ='r') as csvfile:

                csvReader = csv.reader(csvfile, delimiter=',')
                i=0
                aPOINTS=[]
                for row in csvReader:
                    print(row)

                    aPOINTS=  aPOINTS + [(row[0],row[1],row[2])]
                    i=i+1
         return aPOINTS
#-------------------------------------------------------
    def ExportFrame(self,sPathFile):
        # field names
        ##fields = ['POSITION', 'X', 'Y']
        with open(sPathFile, 'w',newline='') as f:

            # using csv.writer method from CSV package
            write = csv.writer(f)

    ##        write.writerow(fields) # header
            write.writerows(self.aPOINTS_ )

#========================================================



if __name__ == '__main__':

    Points02=[["1",10,20],["2",10,20],["3",10,20]]

    #----------------instans 1-------
    sPathFile='datapointsWORLD.csv'
    PointsA=data_points(sPathFile)
    #---------------instans 2
    sPathFile='datapointsWORLD2.csv'
    PointsB=data_points(sPathFile)
    #--------------------------------

##    PointsA.setGlobal()
    PointsA.setGlobal2()

    print('INSTANC A-------------------------')
    print(PointsA.aPOINTS_)
    print(PointsA.aPOINTS_GLOBAL)

    print('INSTANC B-------------------------')
    print(PointsB.aPOINTS_)
    print(PointsB.aPOINTS_GLOBAL)

    PointsA.ExportFrame("datapointsWorld_2.csv")


    print("cam_annotate")








