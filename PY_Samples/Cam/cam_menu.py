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

#========================================================
#========================================================

class cam_menu:


    def draw(oCV2,image):

        # Get Image dimensions

        width = int(image.shape[1] / 5)
        height = int(image.shape[0]  / 20)
        step = int(image.shape[1] / 5)

        TextX = int((width)/ 80) + 1
        TextY = int(height ) + 1
##
##        start_point = (1, 1)
##        end_point = (width, width)
        color = (100, 0, 100) # Blue color in BGR
        thickness = 2 # Line thickness of 2 px
        # Using cv2.rectangle() method

        menu=["QUIT","SAVE PTS","LOAD PTS","SAVE IMG","...."]
        font = cv2.FONT_HERSHEY_SIMPLEX # font
        org = (TextX, TextY) # org
        fontScale = 0.4 # fontScale
        thickness = 1 # Line thickness of 2 px

        for i in[0,1,2,3,4]:
                start_point = (1+step*i, 1)
                end_point = (1+step*i+ width, height)
                TextX = int(1+step*i +(width)/ 80) + 1
                TextY = int(height ) + 1
                org=(TextX,TextY)
                image = oCV2.rectangle(image, start_point, end_point, color, thickness)
                image = oCV2.putText(image, menu[i], org, font, fontScale, color, thickness, oCV2.LINE_AA)


        font = cv2.FONT_HERSHEY_SIMPLEX # font
        org = (TextX, TextY) # org
        fontScale = 0.4 # fontScale
        thickness = 1 # Line thickness of 2 px
        # Using cv2.putText() method
        image = oCV2.putText(image, "QUIT", org, font, fontScale, color, thickness, oCV2.LINE_AA)


        return image

    def command(oCV2,image,X,Y):

        # Get Image dimensions

        width = int(image.shape[1] / 5)
        height = int(image.shape[0]  / 20)
        step = int(image.shape[1] / 5)

        cmd="NULL"

        if (Y< width) and (X < width) :

            cmd="QUIT"

        return cmd



if __name__ == '__main__':



    print("CAM_MENUE")








