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

import numpy as np
import cv2

##=============================================================================
import numpy as np

# Create point matrix get coordinates of mouse click on image
X1=[0,1,0,0,0]
Y1=[0,1,0,0,0]
counter =1

X2=[0,0,0,0,0]
Y2=[0,0,0,0,0]

counter = 0
def mousePoints(event,x,y,flags,params):
    global counter
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Co-ordinate:',x,y)
        X1[counter] = x
        Y1[counter] = y
        counter = counter + 1
        if counter == 5 :
            counter = 1
    if event == cv2.EVENT_RBUTTONDOWN:
        print('Circle:',x,y)
        X2[1] = x
        Y2[1] = y
        print('Circle XY:',X2,Y2)




##=============================================================================
##cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
##=============================================================================
    # Our operations on the frame come here
    frame = cv2.resize(frame, (400, 400))

##     grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    grey_img_2=grey_img
##=============================================================================
##    print('Original Dimensions : ',grey_img.shape)

    scale_percent = 50 # percent of original size
    width = int(grey_img.shape[1] * scale_percent / 100)
    height = int(grey_img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
##    grey_img = cv2.resize(grey_img, dim, interpolation = cv2.INTER_AREA)
    grey_img_2 = grey_img.copy()


##    print('Resized Dimensions : ',resized.shape)

##=============================================================================

    # Display the resulting frame
    thresh = 128

##    grey_img_2 = cv2.cvtColor(grey_img_2, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('b'):
         grey_img_2 = cv2.threshold(grey_img_2, thresh, 255, cv2.THRESH_BINARY)[1]
##    cv2.line(img= grey_img_2, pt1=(10, 10), pt2=(100, 100), color=(0, 0, 0), thickness=5, lineType=8, shift=0)
##    cv2.circle(grey_img_2,(100,100), 20, (0,0,255),1)
##    cv2.rectangle(grey_img_2,(20,20),(180,180),(0,255,0),3)

    if counter == 1 :
        cv2.circle(grey_img_2,(10,10), 5, (0,0,255),1)
    if counter == 2 :
        cv2.circle(grey_img_2,(10,100), 5, (0,0,255),1)
    if counter == 3 :
        cv2.circle(grey_img_2,(100,100), 5, (0,0,255),1)
    if counter == 4 :
        cv2.circle(grey_img_2,(100,10), 5, (0,0,255),1)

    cv2.line(img= grey_img_2, pt1=(X1[4], Y1[4]), pt2=(X1[1], Y1[1]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.line(img= grey_img_2, pt1=(X1[1], Y1[1]), pt2=(X1[2], Y1[2]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.line(img= grey_img_2, pt1=(X1[2], Y1[2]), pt2=(X1[3], Y1[3]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.line(img= grey_img_2, pt1=(X1[3], Y1[3]), pt2=(X1[4], Y1[4]), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

    cv2.circle(grey_img_2,(X2[1],Y2[1]), 10, (0,255,0),1)
    print('Circle LM:',X2[1],Y2[1])

##=============================================================================
    for i in [(100,100),(101,101),(101,100),(100,101)]:
        grey_img_2[ i[0] ][ i[1] ]  = 0

##    grey_img_2[ 15 ][ 15]  = [0, 0, 0]
##    grey_img_2[ X2[1] ][ Y2[1]]  = 255

    sColor = grey_img_2[ X2[1] ][ Y2[1]]

    sBrightness= (1*sColor[0] + 1*sColor[1] + 1*sColor[2])/3
    if sBrightness > 50 :
        sONOFF='ON '
    else:
        sONOFF='OFF '


##    rect = cv2.Rect(x, y, width, height)
##    region = image(rect)

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (50, 50)
    # fontScale
    fontScale = 0.5
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2
    # Using cv2.putText() method
    image = cv2.putText(grey_img_2, sONOFF + str(sBrightness), org, font,
                       fontScale, color, thickness, cv2.LINE_AA)
##=============================================================================
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('grey_img.png',grey_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    img_3 = np.concatenate((grey_img, grey_img_2), axis=1)

##=============================================================================

##=============================================================================
    cv2.imshow('frame',img_3)

    cv2.setMouseCallback('frame', mousePoints)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()