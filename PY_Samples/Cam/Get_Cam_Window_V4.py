#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     05.03.2021
# Copyright:   (c) SESA237770 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# pip install opencv-python
# pip install numpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()
##=============================================================================
import numpy as np
import cv2
import csv

import cam_annotate
import cam_menu
##=============================================================================
def GetImageDimensions(image):

    # Get Image dimensions
    scale_percent = 100 # percent of original size
    width = int(grey_img.shape[1] * scale_percent / 100)
    height = int(grey_img.shape[0] * scale_percent / 100)

    MID_width = int(width/2)
    MID_height = int(height/2)

    return (width, height)
#===============================================================================
def ExportMountingFrame(sPathFile,DataPoints):
    # field names
    fields = ['POSITION', 'X', 'Y']
##    print(DataPoints)
    # data rows of csv file
    with open(sPathFile, 'w',newline='') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)
##        write.writerow(fields) # header
        write.writerows(DataPoints )
#===============================================================================
def ImportMountingFrame(sPathFile):
     with open(sPathFile, mode ='r') as csvfile:

            csvReader = csv.reader(csvfile, delimiter=',')
            i=0
            MP_WORLD=[]
            for row in csvReader:
                print('Read CSV:',row)

                MP_WORLD=  MP_WORLD + [(row[0],row[1],row[2])]
                i=i+1
     return MP_WORLD

#==============================================================================
# Global Points

MountingFrame_TRANS_WORLD= [['TL',1,1],['BL',1,10],['BR',10,10],['TR',10,1]] #mounting frame world
MountingFrame_CAMERA= [['TL',1,1],['BL',1,10],['BR',10,10],['TR',10,1]]#mounting frame world

#==============================================================================
##=============================================================================

# Create point matrix get coordinates of mouse click on image for CIRCLE
X2=[0,0,0,0,0]
Y2=[0,0,0,0,0]

sCMD= 'command'
aCMD=["NULL","QUIT1","QUIT2"]

#=============================================================================
def mousePoints(event,x,y,flags,params):

    global MousePointCounter,Xmenu, Ymenu
    global aCMD
    # Left button mouse click event opencv

    dummy=199

    if event == cv2.EVENT_LBUTTONDOWN:
        print('BEGIN===def mousePoints==============' )
        if (x < aImageDim[0])  :  # menue click ignored !!
            print('Co-ordinate:',x,y)
            aCMD=menu.command(cv2,grey_img,x,y)
            print(x , y ,  'aCMD=' )
            print( aCMD)
            print('END===def mousePoints==============' )

    if event == cv2.EVENT_RBUTTONDOWN:
        print('BEGIN===def mousePoints==============' )
        printflag=1

        if  (x < aImageDim[0]) & ( y < aImageDim[1]):
            print('Circle:',x,y)
            X2[1] = x
            Y2[1] = y
            print('Circle XY:',X2,Y2)
        print('END===def mousePoints==============' )

#=============================================================================
##=============================================================================
##========PROGRAM BEGIN========================================================
##=============================================================================
## select image source
image_source = 2
if image_source==0 :
    # CAM 0
    cap = cv2.VideoCapture(0)
if image_source==1 :
     # CAM 1
     cap = cv2.VideoCapture(1)
if image_source==2 :
    # FILE
    cap = cv2.VideoCapture('grey_img.png')
#------------------------------------------------------------------------------
# Get Image with  ?filter?
if image_source!=2 :
    ret, frame = cap.read()
    grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
else:
    grey_img = cv2.imread('grey_img.png')
#------------------------------------------------------------------------------
# Get Image dimensions
aImageDim=GetImageDimensions(grey_img)
#------------------------------------------------------------------------------
print('====PROGRAM START========================')
print('====PROGRAM MAIN LOOP==================')

menu=cam_menu.cam_menu(cv2,grey_img)

while(True):
#------------------------------------------------------------------------------
# Get Image with  ?filter?
    if image_source!=2 :
        ret, frame = cap.read()
        ####    frame = cv2.resize(frame, (400, 400))
        #grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    else:
        grey_img = cv2.imread('grey_img_1.png')
#------------------------------------------------------------------------------
    # resize image
    # grey_img = cv2.resize(grey_img, dim, interpolation = cv2.INTER_AREA)
    grey_img_2 = grey_img.copy()
    grey_img=menu.draw(cv2,grey_img)
##=============================================================================

    #MountingFrame_CAMERA = [['TL', 358, 352], ['BL', 266, 248], ['BR', 446, 155], ['TR', 410, 114]]  #BGR
    for PTS,i in zip(MountingFrame_CAMERA,[0,1,2,3]):  # zip uses shortes of two lists
        if i== 0:
            PTS_Start=list(PTS)
            PTS_pre=list(PTS)
        if i > 0 :
            cv2.line(img= grey_img_2, pt1=(int(PTS_pre[1]), int(PTS_pre[2])), pt2=(int(PTS[1]), int(PTS[2])), color=(255, 0, 0), thickness=4, lineType=8, shift=0)
            PTS_pre=list(PTS)
        if i == 3 :
            cv2.line(img= grey_img_2, pt1=(int(PTS[1]), int(PTS[2])), pt2=(int(PTS_Start[1]), int(PTS_Start[2])), color=(255, 0, 0), thickness=4, lineType=8, shift=0)

    for PTS,i in zip(MountingFrame_TRANS_WORLD,[0,1,2,3]):  # zip uses shortes of two lists
        if i== 0:
            PTS_Start=list(PTS)
            PTS_pre=list(PTS)
        if i > 0 :
            cv2.line(img= grey_img_2, pt1=(int(PTS_pre[1]), int(PTS_pre[2])), pt2=(int(PTS[1]), int(PTS[2])), color=(0, 255, 0), thickness=1, lineType=8, shift=0)
            PTS_pre=list(PTS)
        if i == 3 :
            cv2.line(img= grey_img_2, pt1=(int(PTS[1]), int(PTS[2])), pt2=(int(PTS_Start[1]), int(PTS_Start[2])), color=(0, 255, 0), thickness=1, lineType=8, shift=0)

##=============================================================================
##    sCMD=menu.command(cv2,grey_img,Xmenu,Ymenu)  # do not draw image in begin

    if type(aCMD[0]) is str:
        sCMD=aCMD[0]

    if sCMD=="QUIT":
        break

    if sCMD=='LOAD PTS':
        print('====IMPORT CSV==============================================')
        print('IMPORT CSV - MountingFrame_TRANS_WORLD.csv')
        # Draw Lines of  imported Mounting Frame
        sPathFile='MountingFrame_TRANS_WORLD.csv'
        MountingFrame_TRANS_WORLD=ImportMountingFrame(sPathFile)
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='SAVE PTS':
        print('====EXPORT CSV==============================================')
        print('EXPORT CSV - MountingFrame_CAMERA.csv')
        sPathFile='MountingFrame_CAMERA.csv'
        ExportMountingFrame(sPathFile,MountingFrame_CAMERA)
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='SAVE IMG':
        print('====EXPORT CSV==============================================')
        print('EXPORT CSV - grey_img_1.png grey_img_2.png')
##        cv2.imwrite('grey_img_1.png',grey_img)
        cv2.imwrite('grey_img_2.png',grey_img_2)
        print('EXPORT png')
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='BL' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[0][1]=aCMD[0][0]
        MountingFrame_CAMERA[0][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='BR' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[1][1]=aCMD[0][0]
        MountingFrame_CAMERA[1][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='TR' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[2][1]=aCMD[0][0]
        MountingFrame_CAMERA[2][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='TL' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[3][1]=aCMD[0][0]
        MountingFrame_CAMERA[3][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"
##=============================================================================
# READ PIXEL
    nDimCroshair=5
    for j in range(-nDimCroshair,nDimCroshair):
            if j==-nDimCroshair:
                sBrightnessV1=0
                sBrightnessH1=0
                sBrightnessV2=0
                sBrightnessH2=0
            sColorV1 = grey_img_2[ X2[1]+0 ][ Y2[1]+j]
            sColorV2 = grey_img_2[ X2[1]+j ][ Y2[1]+j]
            sColorH1 = grey_img_2[ X2[1]+j ][ Y2[1]+0]
            sColorH2 = grey_img_2[ X2[1]-j ][ Y2[1]+j]

##            print('Color:', sColorV1)

            sBrightnessV1=sBrightnessV1+ (1*sColorV1[0] + 1*sColorV1[1] + 1*sColorV1[2])/3
            sBrightnessV2=sBrightnessV2+ (1*sColorV2[0] + 1*sColorV2[1] + 1*sColorV2[2])/3

            sBrightnessH1=sBrightnessH1+ (1*sColorH1[0] + 1*sColorH1[1] + 1*sColorH1[2])/3
            sBrightnessH2=sBrightnessH2+ (1*sColorH2[0] + 1*sColorH2[1] + 1*sColorH2[2])/3

    sBrigntnessX=(sBrightnessV1 + sBrightnessH1 +sBrightnessV2 + sBrightnessH2)/4/21
    sBrightness=int((sBrigntnessX)/10) *10 # remove 1 digit

    if sBrightness > 200 :
        sONOFF='LED ON '
        nCircle=10
    else:
        sONOFF='LED OFF '
        nCircle=1

 # Draw circle for LED query
    cv2.circle(grey_img_2,(X2[1],Y2[1]), nDimCroshair, (0,255,0),nCircle)

##    print('Circle LM:',X2[1],Y2[1])
##=============================================================================
##    rect = cv2.Rect(x, y, width, height)
##    region = image(rect)
##=============================================================================
# KEYSTRIKE COMMANDS
    # EXPORT CSV
    if cv2.waitKey(1) & 0xFF == ord('e'):
        print('====EXPORT CSV==============================================')

    # IMPORT CSV
    if cv2.waitKey(1) & 0xFF == ord('i'):
        print('====IMPORT CSV==============================================')

    # SAVE IMAGE
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('grey_img_1.png',grey_img)
        cv2.imwrite('grey_img_2.png',grey_img_2)
        print('EXPORT png')
        sCMD= 'EXPORTED IMAGES L & R'
    # QUIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
##=============================================================================
# IMAGE SHOW
    img_3 = np.concatenate((grey_img, grey_img_2), axis=1)
    cv2.imshow('frame',img_3)
    cv2.setMouseCallback('frame', mousePoints)

##=============================================================================
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()