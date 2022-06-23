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
# pip install Pillow
def main():
    pass

if __name__ == '__main__':
    main()

# Importing Image from PIL package
from PIL import Image

# creating a image object
#im = Image.open(r'C:\Users\sesa237770\Documents\Lagrange\PIXEL\invader.jpg')

im = Image.open(r'C:\Users\sesa237770\Pictures\invader.jpg')


px = im.load()
print (px[4, 4])
px[4, 4] = (0, 0, 0)
print (px[4, 4])
cordinate = x, y = 150, 59

# using getpixel method
print (im.getpixel(cordinate));