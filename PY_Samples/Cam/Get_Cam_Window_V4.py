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
# TODO (search label)
# LABEL20220826_00 :  nDimCroshair=10   #LED_TRANS_WORLD[i][3] # size of circles is not scaled
# LABEL20220826_01 :  Make seperate module for EXPORTING, make test module
# LABEL20220826_02 :TODO code must be moved to anotiations module
# LABEL20220826_03 :TODO export to SQLITE
#
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
##=============================================================================
import numpy as np
import cv2
import csv
import sys
import os
import datetime
import schedule
import subprocess

#--CAX Modules (My modules)
from selectproject import DialogProjectChoice
import cam_annotate
import cam_menu
import Transformations
# from module_transformations import transformation # used in Transformations
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
                print(row)

                if len(row)==4 :
                    MP_WORLD=  MP_WORLD + [(row[0],row[1],row[2],row[3])]
                if len(row)==3 :
                    MP_WORLD=  MP_WORLD + [(row[0],row[1],row[2])]

                i=i+1
     return MP_WORLD


#===============================================================================
def StackImages(img,LED_CAMERA,sPathfile_LED_STACK):

     for PTS,i in zip(LED_CAMERA,range(0,len(LED_CAMERA))):  # zip uses shortes of two lists

        LED_X=int(LED_CAMERA[i][1])
        LED_Y=int(LED_CAMERA[i][2])
        LED_R=int(LED_CAMERA[i][3])

        print('LED XY ',LED_X,LED_Y)
        nSlice=10
        cX1=LED_X-nSlice
        cX2=LED_X+nSlice

        cY1=LED_Y-nSlice
        cY2=LED_Y+nSlice

        #roi = image[startY:endY, startX:endX]
        crop = img[cY1:cY2,cX1:cX2 ]

        flag=3  # fails if picture matrix not compatable

        if flag==0 :
            crop_grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            crop_post_process=crop_grey
        if flag==1 :
            crop_grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            crop_post_process=crop_grey
        if flag==2 :
            (thresh, crop_BW) = cv2.threshold(crop_grey, 100, 200, cv2.THRESH_BINARY)
            crop_post_process=crop_BW
        if flag==3 :
            crop_post_process=crop

        crop_avg_color_row=np.average(crop_post_process, axis=0)
        crop_avg_color = np.average(crop_avg_color_row, axis=0)

        Color_img = np.ones((nSlice*2,nSlice*2,3), dtype=np.uint8)
        Color_img[:,:] = crop_avg_color



        print('Average Color:', i,crop_avg_color)

        print('crop:',cX1,cX2,cY1 ,cY2,LED_CAMERA[i][0])
        if i==0:
            crop0 = crop_post_process[1:2, 0:10000 ] #roi = image[startY:endY, startX:endX]
            LED_stack=np.vstack([crop0, crop_post_process]) # cv2.COLOR_BGR2GRAY
            LED_stack_average=np.vstack([crop0, Color_img])

        else:
            LED_stack=np.vstack([LED_stack, crop_post_process])
            LED_stack_average=np.vstack([LED_stack_average, Color_img])

        sPathfile_LED_STACK_raw=sPathfile_LED_STACK.replace('.png','_raw.png')
        sPathfile_LED_STACK_avg=sPathfile_LED_STACK.replace('.png','_avg.png')

     cv2.imwrite(sPathfile_LED_STACK_raw,LED_stack)
     cv2.imwrite(sPathfile_LED_STACK_avg,LED_stack_average)

     cv2.imshow('LED 1', LED_stack)
     cv2.imshow('LED 2', LED_stack_average)

#==============================================================================
nDataMeasurement=[[]] ## list of list
nDataMeasurementQue=[[[]]] ## list of list of list
nDataQue=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
nSec=5

def job():
    global nDataQue

    print("=================================================================")
    print("===Schedule Event=====Seconds:" ,nSec)
    print("=================================================================")
    nDataQue = ExtractPOIs(grey_img,LED_TRANS_WORLD,nDataQue)
    ExportPOIMeasurements(sPathfile_LED_EXPORT,nDataQue)
    print("=================================================================")
# run the function job() every 2 seconds

schedule.every(nSec).seconds.do(job)

#===============================================================================

def ExtractPOIs(img,LED_CAMERA,nDataQueLocal):

    #get current date and time
    dt = datetime.datetime.now()
    #convert date and time to string
    dateTimeStr = str(dt)
    sDateTime=dt.strftime('%Y_%m_%d_%H_%M_%S')
    sn_DateTime=dt.strftime('%Y%m%d%H%M%S')
    sn_YM=dt.strftime('%Y%m%d')
    sn_DHMS=dt.strftime('%H%M%S')
    ##-------------------------------------------
    ## time strings convert to integers
    nYear=int(sn_YM)
    nTime=int(sn_DHMS)

    print('LOG FILE: ',sPathfile_LED_EXPORT, '@', sDateTime )

    ##-BEGIN FOR POINTS-----------------------------------------
    l_LED_CAMERA=[]
    nCount=0
    for PTS,i in zip(LED_CAMERA,range(0,len(LED_CAMERA))):  # zip uses shortes of two lists

        LED_X=int(LED_CAMERA[i][1])
        LED_Y=int(LED_CAMERA[i][2])
        LED_R=int(LED_CAMERA[i][3])

##        print('LED XY POSITIONS: ',LED_X,LED_Y)
        nSlice=10
        cX1=LED_X-nSlice
        cX2=LED_X+nSlice

        cY1=LED_Y-nSlice
        cY2=LED_Y+nSlice

        #roi = image[startY:endY, startX:endX]
        crop = img[cY1:cY2,cX1:cX2 ]

        flag=3  # fails if picture matrix not compatable

        if flag==0 :
            crop_grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            crop_post_process=crop_grey
        if flag==1 :
            crop_grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            crop_post_process=crop_grey
        if flag==2 :
            (thresh, crop_BW) = cv2.threshold(crop_grey, 100, 200, cv2.THRESH_BINARY)
            crop_post_process=crop_BW
        if flag==3 :
            crop_post_process=crop

        crop_avg_color_row=np.average(crop_post_process, axis=0)
        crop_avg_color = np.average(crop_avg_color_row, axis=0)

        ##-------------------------------------------
        ## Round colors convert to integers
        crop_avg_color = np.round_(crop_avg_color)
        n_crop_avg_color= crop_avg_color.astype(int)
          ## tag(append) list colors with year month and da hour min sec
        l_avg_color=n_crop_avg_color.tolist()
        l_avg_color.insert(0,nTime)
        l_avg_color.insert(0,nYear)
        l_avg_color.insert(0,nCount)

        nCount=nCount+1

        ##-------------------------------------------
        l_LED_CAMERA.append(l_avg_color)

    ##-END FOR POINTS-----------------------------------------

##    nDataQue.insert(0,l_LED_CAMERA)
##    print('--- nDataQueLocal---')
##    print(nDataQueLocal)
    print("---------------------------------------------------")
    print('---CAMERA MEASUREMENTS: l_LED_CAMERA---')
    for item in l_LED_CAMERA:
        print(item)
    print('--------------------------------------------------')
    for item in l_LED_CAMERA:
##        print('Item:',item)
        nDataQueLocal.insert(0,item)
        if len(nDataQueLocal)>len(l_LED_CAMERA)*10: # ensure all LED read not cut off
            nDataQueLocal.pop(-1)  # -1 default

    return nDataQueLocal

# LABEL20220826_01
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

##if len(sys.argv) ==3 :  # 1 st = 1...1000 is a job number 2 is 11 12 22 33 = size of frontplate
##    sJOBprefix=  '0000' + str(sys.argv[1])  #Number
##    sJOBprefix =+ "job" + sJOBprefix[-3:] +'_'+ str(sys.argv[2])+'_'
##
##else:
##    user = os.getlogin()
##    print('User:',user)
##    sJOBprefix=user+'_'
##
##if user=='SESA237770':
##    sPrefix='workspace_MPA\\'
##else: sPrefix='workspace_OJS\\'

#------------------------------------------------------------------------------

##for i in range(1,5):
##    nDataQue.append([0,0,0,0,0,0])

#------------------------------------------------------------------------------
# Choose WORKSPACE"
sJOBprefix='job_'
##sPrefix='workspace_MPA\\'
##sPrefix='workspace_OJS\\'
##sPrefix='workspace_2X2\\'
##sPrefix='workspace_1X2\\'
##sPrefix='workspace_2X2\\'

oDialog=DialogProjectChoice(["workspace_1X2","workspace_1X2_ojs","workspace_2x2","workspace_1X2_Elastic","workspace_1X2_Perspective"])
sPrefix = oDialog.Show()
sPrefix +='\\'

#------------------------------------------------------------------------------
# select iuser folder

sPathfile_ExportImage1=sPrefix + 'grey_img_left.png'
sPathfile_ExportImage2=sPrefix + 'grey_img_right.png'
sPathfile_VideoSubstituteImage=sPrefix + 'grey_img_substitute.png'

sPathFileImport=sPrefix + 'MountingFrame_TRANS_WORLD.csv'
sPathFileExport=sPrefix + 'MountingFrame_CAMERA.csv'
sPathFileImportLED_WORLD=sPrefix + 'LED_TRANS_WORLD.csv'

sPathfile_LED_STACK=sPrefix + 'LED_Stack.png'
sPathfile_LED_EXPORT=sPrefix + 'LED_Stack.log'

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
# build menu
# TO DO  munue items declared here :
menu=cam_menu.cam_menu(cv2,grey_img)

################################################################################
#------------------------------------------------------------------------------
print('====PROGRAM START========================')
print('====PROGRAM MAIN LOOP====================')
################################################################################
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
# LABEL20220826_02
# TODO code must be moved to anotiations module
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
        nDimCroshair=10   #LED_TRANS_WORLD[i][3]   #LABEL20220826_00
        nCircle=1
        CircleX=int(LED_TRANS_WORLD[i][1])
        CircleY=int(LED_TRANS_WORLD[i][2])
        cv2.circle(grey_img_2,(CircleX,CircleY), nDimCroshair, (0,0,255),nCircle)

        org=(CircleX-nDimCroshair,CircleY+nDimCroshair) # bottom left of circle
        color = (100, 0, 100) # Blue color in BGR
        thickness = 1 # Line thickness of 2 px
        font = cv2.FONT_HERSHEY_SIMPLEX # font
        fontScale = 0.5 # fontScale
        cv2.putText(grey_img_2, str(i), org, font, fontScale, color, thickness, cv2.LINE_AA)

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
        import Transformations
        Transformations.main(sPrefix)
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
        StackImages(grey_img,LED_TRANS_WORLD,sPathfile_LED_STACK)
        print('LED:',LED_TRANS_WORLD[0])
##        print('crop:',cX1,cY1, cX2,cY2)

        cam_menu.cam_menu.aCMD[0]="DONE"

    if sCMD=='watch':
        print('====CROP IMAGE==============================================')
        print('')
        print('LED:',LED_TRANS_WORLD[0])
##        print('crop:',cX1,cY1, cX2,cY2)
        print('watch Toggle status:', menu.getToggleStatus('watch'))
        cam_menu.cam_menu.aCMD[0]="DONE"

    if menu.getToggleStatus('watch')=='1':
#        print('====LOG IMAGE==============================================')
#        print('')
        schedule.run_pending()
#        LED_Export(grey_img,LED_TRANS_WORLD,sPathfile_LED_EXPORT)



##=============================================================================
# TO DO CODE must be replaced:
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
    cv2.setWindowTitle('frame', sPrefix)
    cv2.setMouseCallback('frame', mousePoints)

##=============================================================================
#------------------------------------------------------------------------------
print('====END PROGRAM E========================')
print('====END PROGRAM MAIN LOOP====================')
################################################################################
################################################################################
################################################################################
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()