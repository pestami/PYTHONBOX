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
import subprocess
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


#===============================================================================
def StackImages(img,LED_CAMERA):

     for PTS,i in zip(LED_CAMERA,range(0,len(LED_CAMERA))):  # zip uses shortes of two lists

        LED_X=int(LED_CAMERA[i][1])
        LED_Y=int(LED_CAMERA[i][2])
        print('LED XY ',LED_X,LED_Y)
        nSlice=20
        cX1=LED_X-nSlice
        cX2=LED_X+nSlice

        cY1=LED_Y-nSlice
        cY2=LED_Y+nSlice

        #roi = image[startY:endY, startX:endX]
        crop = img[cY1:cY2,cX1:cX2 ]
        crop_grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        #(thresh, crop_BW) = cv2.threshold(crop_grey, 100, 200, cv2.THRESH_BINARY)

        print('crop:',cX1,cX2,cY1 ,cY2,LED_CAMERA[i][0])
        if i==0:
            crop0 = crop_grey[1:2, 0:10000 ] #roi = image[startY:endY, startX:endX]
            LED_stack=np.vstack([crop0, crop_grey])
        else:
            LED_stack=np.vstack([LED_stack, crop_grey])

     cv2.imwrite('LED_Stack.png',LED_stack)
     cv2.imshow('LED 1', LED_stack)

#==============================================================================
# Global Points

MountingFrame_TRANS_WORLD= [['TL',1,1],['BL',1,10],['BR',10,10],['TR',10,1]] #mounting frame world
MountingFrame_CAMERA= [['TL',1,1],['BL',1,10],['BR',10,10],['TR',10,1]]#mounting frame world
LED_TRANS_WORLD= [['TL',1,1,5],['BL',1,10,5],['BR',10,10,5],['TR',10,1,5]] #mounting frame world

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
sPathfile_ExportImage1='grey_img_left.png'
sPathfile_ExportImage2='grey_img_right.png'
sPathfile_VideoSubstituteImage='grey_img_substitute.png'

sPathFileImport='MountingFrame_TRANS_WORLD.csv'
sPathFileExport='MountingFrame_CAMERA.csv'
sPathFileImportLED_WORLD='LED_TRANS_WORLD.csv'
#------------------------------------------------------------------------------
# select image source
image_source = 1
if image_source==0 :
    # CAM 0
    cap = cv2.VideoCapture(0)
if image_source==1 :
     # CAM 1
     cap = cv2.VideoCapture(1)
if image_source==2 :
    # FILE
    cap = cv2.VideoCapture(sPathfile_VideoSubstituteImage)
#------------------------------------------------------------------------------
# Get Image with  ?filter?

##    if image_source!=2 :
##        ret, frame = cap.read()
##        grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
##    else:
##        grey_img = cv2.imread(sPathfile_VideoSubstituteImage)
try:
        ret, frame = cap.read()
        grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
except:
        grey_img = cv2.imread(sPathfile_VideoSubstituteImage)

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
    try:
        ret, frame = cap.read()
        ####    frame = cv2.resize(frame, (400, 400))
        #grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    except:
        grey_img = cv2.imread(sPathfile_VideoSubstituteImage)
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

    for PTS,i in zip(LED_TRANS_WORLD,range(0,len(LED_TRANS_WORLD))):  # zip uses shortes of two lists
        nDimCroshair=10   #LED_TRANS_WORLD[i][3]
        nCircle=1
        cv2.circle(grey_img_2,(int(LED_TRANS_WORLD[i][1]),int(LED_TRANS_WORLD[i][2])), nDimCroshair, (0,0,255),nCircle)

##=============================================================================
##    sCMD=menu.command(cv2,grey_img,Xmenu,Ymenu)  # do not draw image in begin

    if type(aCMD[0]) is str:
        sCMD=aCMD[0]

    if sCMD=="QUIT":
        break

    if sCMD=='SOURCE':
        print('====CHANGE VIDEO SOURCE======================================')
        image_source_pre=image_source
        print('Change Source', image_source_pre)
        if image_source==2:
            image_source=1
            print('Changed to ', image_source)
        if image_source==1 and image_source_pre !=2 :
            image_source=2
            print('Changed to ', image_source)

        print('New Source', image_source)
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='LOAD PTS':
        print('====IMPORT CSV==============================================')
        print('IMPORT CSV - MountingFrame_TRANS_WORLD.csv')
        # Draw Lines of  imported Mounting Frame
        sPathFile=sPathFileImport
        MountingFrame_TRANS_WORLD=ImportMountingFrame(sPathFile)
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='LOAD LED':
        print('====IMPORT CSV==============================================')
        print('IMPORT CSV - LED_TRANS_WORLD.csv')
        # Draw Lines of  imported Mounting Frame
        sPathFile=sPathFileImportLED_WORLD
        LED_TRANS_WORLD=ImportMountingFrame(sPathFile)
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='CALC':
        print('====ICalculate Transformations==============================================')
        print('Transformations.py')
        subprocess.call("Transformations.py", shell=True)
        cam_menu.cam_menu.aCMD[0]="DONE"


    if sCMD=='SAVE PTS':
        print('====EXPORT CSV==============================================')
        print('EXPORT CSV - MountingFrame_CAMERA.csv')
        sPathFile=sPathFileExport
        ExportMountingFrame(sPathFile,MountingFrame_CAMERA)
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='SAVE IMG':
        print('====EXPORT CSV==============================================')
        print('EXPORT CSV - ' , sPathfile_ExportImage1, sPathfile_ExportImage2)
        cv2.imwrite(sPathfile_ExportImage1,grey_img)
        cv2.imwrite(sPathfile_ExportImage2,grey_img_2)
        print('EXPORT png')
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='TL' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[0][1]=aCMD[0][0]
        MountingFrame_CAMERA[0][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"


    if aCMD[1]=='BL' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[1][1]=aCMD[0][0]
        MountingFrame_CAMERA[1][2]=aCMD[0][1]

        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='BR' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[2][1]=aCMD[0][0]
        MountingFrame_CAMERA[2][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"

    if aCMD[1]=='TR' and type(aCMD[0]) is tuple:
        print('====NEW BL POINT Detected====================================')
        #MountingFrame_CAMERA= [('TL',1,1),('BL',1,10),('BR',10,10),('TR',10,1)]#mounting frame world
        MountingFrame_CAMERA[3][1]=aCMD[0][0]
        MountingFrame_CAMERA[3][2]=aCMD[0][1]
        print(MountingFrame_CAMERA)
        cam_menu.cam_menu.aCMD[2]=cam_menu.cam_menu.aCMD[1]
        cam_menu.cam_menu.aCMD[1]=cam_menu.cam_menu.aCMD[0]
        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='crop':
        print('====CROP IMAGE==============================================')
        print('')
        StackImages(grey_img,LED_TRANS_WORLD)
        print('LED:',LED_TRANS_WORLD[0])
##        print('crop:',cX1,cY1, cX2,cY2)

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
        cv2.imwrite('grey_img_left.png',grey_img)
        cv2.imwrite('grey_img_right.png',grey_img_2)
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