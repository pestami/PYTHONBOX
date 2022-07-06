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

        width = int(image.shape[1] / 20)
        height = int(image.shape[0]  / 20)


        start_point = (1, 1)
        end_point = (width, width)
        color = (255, 0, 0) # Blue color in BGR
        thickness = 2 # Line thickness of 2 px
        # Using cv2.rectangle() method
        image = oCV2.rectangle(image, start_point, end_point, color, thickness)


        font = cv2.FONT_HERSHEY_SIMPLEX # font

        org = (20, 10) # org
        fontScale = 0.5 # fontScale
        color = (0, 255, 0) # Blue color in BGR
        thickness = 1 # Line thickness of 2 px
        org = (int(width/3), int(width/3))  #X Y
        # Using cv2.putText() method
        image = oCV2.putText(image, "QUIT", org, font, fontScale, color, thickness, oCV2.LINE_AA)


        return image

    def command(oCV2,image,X,Y):

        # Get Image dimensions

        width1 = int(image.shape[1] / 20)
        height1 = int(image.shape[0]  / 20)
        cmd="NULL"

        if (Y> height1) & (X < width1) :

            cmd="QUIT"

        return cmd



if __name__ == '__main__':



    print("CAM_MENUE")








