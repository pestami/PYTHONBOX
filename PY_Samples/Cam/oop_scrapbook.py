#-------------------------------------------------------------------------------
# Name:        oop_scrapbook.py
# Purpose:
#
# Author:      SESA237770
#
# Created:     08.07.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# #### SELF ###################################################################
# self is is best practice but any name can be used ???
# https://www.tutorialspoint.com/self-in-python-class

# #### Instance Variable  vs Class Variable####################################
# this is only for C++
# Instance Variable: It is basically a class variable without a static modifier
# and is usually shared by all class instances.
# Across different objects, these variables can have different values.
## static int count;
# Class Variable: It is basically a static variable that can be declared anywhere at class level with static.
# Across different objects, these variables can have only one value.
# These variables are not tied to any particular object of the class,
# therefore, can share across all objects of the class.
# https://www.geeksforgeeks.org/difference-between-instance-variable-and-class-variable/


## CLASS - OBJECT - INSTANCE
# https://isbe.bwk.tue.nl/education/Python/02_03_Objects.html

##There are several kinds of variables in Python:
##
##    Instance variables in a class: these are called fields or attributes of an object
##    Local Variables: Variables in a method or block of code
##    Parameters: Variables in method declarations
##    Class variables: This variable is shared between all objects of a class
#https://pynative.com/python-instance-variables/
## Also atrributes can be set at runtime !!!!


class data_points:

##  Class variables: This variable is shared between all objects of a class
    aGLOBAL_IMAGE=["XoX0X"]
    aGLOBAL_sPathFile=["c:\...."]


#========================================================
    def __init__(self, sPathFile,aIMAGE,aPOINTS_):

        data_points.aGLOBAL_sPathFile=sPathFile
        ##  Class variables?
        self.__class__.aGLOBAL_IMAGE=aIMAGE

        # Instance variable or attribute
        self.aPOINTS=aPOINTS_
#-------------------------------------------------------
    @classmethod
    def setGlobal(blabla):
        blabla.aPOINTS_GLOBAL="GLOBAL1"

#-------------------------------------------------------
    def setGlobal2(self):
        self.__class__.aPOINTS_GLOBAL="GLOBAL2"

#-------------------------------------------------------
    def DumpAllVar(self):
        print('\n...METHOD OUTPUT................................')
        print('This Name:',type(data_points).__name__)


#        print('aGLOBAL_IMAGE_DIM=',self.__class__.aGLOBAL_IMAGE_DIM)  #>>> name 'self' is not defined
#        print('aGLOBAL_IMAGE_DIM=',aGLOBAL_IMAGE_DIM)                  #>>>  name 'aGLOBAL_IMAGE_DIM' is not defined

        print('aGLOBAL_IMAGE_DIM=',data_points.aGLOBAL_IMAGE)
        print('aGLOBAL_sPathFile=',data_points.aGLOBAL_sPathFile)
       # print('Attribute Points=',data_points.aPOINTS)
        print('Attribute Points=',self.aPOINTS)
##        print('aIMAGE=',aIMAGE)

        print('............................................')
#-------------------------------------------------------

#========================================================

#-------------------------------------------------------------------------------
if __name__ == '__main__':

    print('===MAIN TEST=====================================')
    #----------------instans 1-------
    sPathFile='datapointsWORLD.csv'
    aPOINTS_image1=[(1,2),(2,3)]
    PointsA=data_points(sPathFile," :-) ",aPOINTS_image1)

    #---------------instans 2
    sPathFile='datapointsIMAGE.csv'
    aPOINTS_image2=[(10,20),(20,30)]
    PointsB=data_points(sPathFile," ;-D ",aPOINTS_image2)

    #--------------------------------


    print('\n----Dump Vars instanc A---------------')
    print("aIMAGE=",PointsA.aGLOBAL_IMAGE)
    PointsA.DumpAllVar()


    print('\n----Dump Vars instanc B---------------')
    print("aIMAGE=",PointsB.aGLOBAL_IMAGE)
    PointsB.DumpAllVar()

#-------------------------------------------------------------------------------
print('\n---List all atrributes in OBJECT---------------')
    # Get each instance variable
for key_value in PointsB.__dict__.items():
    print(key_value[0], '=', key_value[1])

print( 'Points attribute: ',PointsB.aPOINTS)








