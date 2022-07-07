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

    menu=["QUIT","SAVE PTS","LOAD PTS","SAVE IMG","...."]
#----------------------------------------------------------------------------
    def draw(oCV2,image):

        # Get Image dimensions

        width_button = int(image.shape[1] / 5)
        height_button = int(image.shape[0] / 20)
        spacing_button = int(image.shape[1] / 5)

        color = (100, 0, 100) # Blue color in BGR
        thickness = 2 # Line thickness of 2 px
        # Using cv2.rectangle() method

##        menu=["QUIT","SAVE PTS","LOAD PTS","SAVE IMG","...."]
        font = cv2.FONT_HERSHEY_SIMPLEX # font
        fontScale = 0.4 # fontScale
        thickness = 1 # Line thickness of 2 px

        for i in[0,1,2,3,4]:
                start_point = (1+spacing_button*i, 1)
                end_point = (1+spacing_button*i+ width_button, height_button)
                TextX = int(1+spacing_button*i +(width_button)/ 80) + 1
                TextY = int(height_button/2 ) + 1
                org=(TextX,TextY)
                image = oCV2.rectangle(image, start_point, end_point, color, thickness)
                image = oCV2.putText(image, cam_menu.menu[i], org, font, fontScale, color, thickness, oCV2.LINE_AA)

        return image
#----------------------------------------------------------------------------
    def command(oCV2,image,X,Y):

        # Get Image dimensions

        width_button = int(image.shape[1] / 5)
        height_button = int(image.shape[0] / 20)
        spacing_button = int(image.shape[1] / 5)

##        menu=["QUIT","SAVE PTS","LOAD PTS","SAVE IMG","...."]
        cmd="NULL"

        for i in[0,1,2,3,4]:
            start_point = (1+spacing_button*i, 1)
            end_point = (1+spacing_button*i+ width_button, height_button)

            if (Y< height_button) and (start_point[0] < X < end_point[0]) :
                cmd=cam_menu.menu[i]

        return cmd
#----------------------------------------------------------------------------


if __name__ == '__main__':



    print("CAM_MENUE")








