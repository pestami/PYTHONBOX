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

    ##  Class variables: This variable is shared between all objects of a class
    menu=      ["SOURCE","BL" ,"BR" ,"TR" ,"TL" ,"SAVE PTS" ,"CALC","LOAD PTS","LOAD LED","SAVE IMG" ,"crop","watch","QUIT"]
    menutype=  ["BTN"   ,"BTN","BTN","BTN","BTN","BTN"      ,"BTN" ,"BTN"     ,"BTN"     ,"BTN"      ,"BTN" ,"TGL"  ,"BTN"]
    menustatus=["BTN"   ,"BTN","BTN","BTN","BTN","BTN"      ,"BTN" ,"BTN"     ,"BTN"     ,"BTN"      ,"BTN" ,"0"    ,"BTN"]

    ## BTN = BUTTON  TGL = TOGGLE
    ## command history and command latest
    aCMD=["NULL","QUIT1","QUIT2"]
    aCMD_TGL=[]

    #========================================================
    def __init__(self, oCV2,image):

        ## class attributes
        self.menue_items=len(self.menu) + 1
        self.menue_width=int(image.shape[1])
        self.width_button = int(image.shape[1] / (self.menue_items-1))
        self.height_button = int(image.shape[0] / 20)
        self.spacing_button = int(image.shape[1] / (self.menue_items-1))
        self.color = (100, 0, 100) # Blue color in BGR
        self.color_toggle = (100, 0, 0) # Blue color in BGR
        self.thickness = 2 # Line thickness of 2 px
##        print("INITIALIZE: width height sapacing",width_button,height_button,spacing_button ) # test = ok

#-------------------------------------------------------
#-------------------------------------------------------
    def draw(self,oCV2,image):

        width_button =self.width_button
        height_button = self.height_button
        spacing_button = self.spacing_button
        color = self.color
        thickness =self.thickness

         # Using cv2.rectangle() method

##        menu=["QUIT","SAVE PTS","LOAD PTS","SAVE IMG","...."]
        font = cv2.FONT_HERSHEY_SIMPLEX # font
        fontScale = 0.3 # fontScale
        thickness = 1 # Line thickness of 2 px

        start_point = (1, 1)
        end_point = (self.menue_width, height_button)
        color2 = (200, 200, 200)
        thickness2 = -1   # Thickness of -1 will fill the entire shape
        image = cv2.rectangle(image, start_point, end_point, color2, thickness2)

        for i in range(0, self.menue_items-1):
                start_point = (1+spacing_button*i, 1)
                end_point = (1+spacing_button*i+ width_button, height_button)
                TextX = int(1+spacing_button*i +(width_button)/ 80) + 1
                TextY = int(height_button/2 ) + 1
                org=(TextX,TextY)
                if self.menutype[i]=='TGL':
                    color =self.color_toggle
                else:
                    color =self.color
                if self.menustatus[i]=='1':
                    image = oCV2.rectangle(image, start_point, end_point, color, 2)



                image = oCV2.rectangle(image, start_point, end_point, color, thickness)
                image = oCV2.putText(image, cam_menu.menu[i], org, font, fontScale, color, thickness, oCV2.LINE_AA)

        return image
#----------------------------------------------------------
    def command(self,oCV2,image,X,Y):

        # Get Image dimensions
        width_button =self.width_button
        height_button = self.height_button
        spacing_button = self.spacing_button

##        menu=["QUIT","SAVE PTS","LOAD PTS","SAVE IMG","...."]
        cmd="NULL"

        for i in range(0,self.menue_items-1):
            start_point = (1+spacing_button*i, 1)
            end_point = (1+spacing_button*i+ width_button, height_button)

            if (Y< height_button) and (start_point[0] < X < end_point[0]) :

                if self.menutype[i]=='TGL':
                    if self.menustatus[i]=='1':
                        new_menustatus='0'
                    if self.menustatus[i]=='0':
                        new_menustatus='1'
                    self.menustatus[i]=new_menustatus

                cmd=cam_menu.menu[i]

                cam_menu.aCMD[2]=cam_menu.aCMD[1]
                cam_menu.aCMD[1]=cam_menu.aCMD[0]
                cam_menu.aCMD[0]=cmd
        if cmd=="NULL" :
                cmd=(X,Y)
                cam_menu.aCMD[2]=cam_menu.aCMD[1]
                cam_menu.aCMD[1]=cam_menu.aCMD[0]
                cam_menu.aCMD[0]=cmd


        return cam_menu.aCMD
#----------------------------------------------------------
    def getToggleStatus(self,sMenuItem):

        svalue=''

        for i in range(0,self.menue_items-1):
            if self.menu[i] ==sMenuItem:
                sValue=self.menustatus[i]


        return sValue



#-----------------------------a-----------------------------------------------


if __name__ == '__main__':


    print("CAM_MENUE")








