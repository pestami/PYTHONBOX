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

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
##=============================================================================
    # Our operations on the frame come here
    frame = cv2.resize(frame, (400, 400))

    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##    grey_img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    grey_img_2=grey_img
##=============================================================================
    print('Original Dimensions : ',grey_img.shape)

    scale_percent = 50 # percent of original size
    width = int(grey_img.shape[1] * scale_percent / 100)
    height = int(grey_img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    grey_img = cv2.resize(grey_img, dim, interpolation = cv2.INTER_AREA)
    grey_img_2 = grey_img.copy()


##    print('Resized Dimensions : ',resized.shape)
##=============================================================================

    # Display the resulting frame
    thresh = 128

##    grey_img_2 = cv2.cvtColor(grey_img_2, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('b'):
         grey_img_2 = cv2.threshold(grey_img_2, thresh, 255, cv2.THRESH_BINARY)[1]
##    cv2.line(img= grey_img_2, pt1=(10, 10), pt2=(100, 100), color=(0, 0, 0), thickness=5, lineType=8, shift=0)
    cv2.circle(grey_img_2,(100,100), 20, (0,0,255),1)
    cv2.rectangle(grey_img_2,(20,20),(180,180),(0,255,0),3)


##=============================================================================
    for i in [(100,100),(101,101),(101,100),(100,101)]:
        grey_img_2[ i[0] ][ i[1] ]  = 0

##    grey_img_2[ 15 ][ 15]  = [0, 0, 0]
    grey_img_2[ 15 ][ 15]  = 255
##=============================================================================
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('grey_img.png',grey_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    qqqqqqqqqimg_3 = np.concatenate((grey_img, grey_img_2), axis=1)
    cv2.imshow('frame',img_3)

##=============================================================================
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()