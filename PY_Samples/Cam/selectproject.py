#-------------------------------------------------------------------------------
# Name:       selectproject.py
# Purpose:
#
# Author:      SESA237770
#
# Created:     21.07.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

#==============================================================================
class DialogProjectChoice:

    ##  Class variables: This variable is shared between all objects of a class
    sProjectList=[]
    sSelection=""
    #------------------------------------------------------------------------
    # oDialog=DialogProjectChoice(["workspace_1X2","workspace_1X2_ojs","workspace_2x2","workspace_2x2_Elastic","workspace_1X2_Perspective"])

    def __init__(self, sProjectList):

        self.sProjectList = sProjectList

        print("Projects:", sProjectList)

    def Show(self):

            print("SHOWING DIALOG ")

            root = Tk()
            var = IntVar()

            print("SHOWING DIALOG")

            def sel():
                selection = "You selected the option " + str(var.get())
                label.config(text = selection)
                nSELECT= var.get()
                if nSELECT ==1 :
                    self.sSelection=self.sProjectList[0]
                if nSELECT ==2 :
                    self.sSelection=self.sProjectList[1]
                if nSELECT ==3 :
                    self.sSelection=self.sProjectList[2]
                if nSELECT ==4 :
                    self.sSelection=self.sProjectList[3]
                if nSELECT ==5 :
                    self.sSelection=self.sProjectList[4]


            R1 = Radiobutton(root, text=self.sProjectList[0], variable=var, value=1, command=sel)
            R1.pack( anchor = W )

            R2 = Radiobutton(root, text=self.sProjectList[1], variable=var, value=2, command=sel)
            R2.pack( anchor = W )

            R3 = Radiobutton(root, text=self.sProjectList[2], variable=var, value=3, command=sel)
            R3.pack( anchor = W)

            R4 = Radiobutton(root, text=self.sProjectList[3], variable=var, value=4, command=sel)
            R4.pack( anchor = W)

            R5 = Radiobutton(root, text=self.sProjectList[4], variable=var, value=5, command=sel)
            R5.pack( anchor = W)


            label = Label(root)
            label.pack()
            root.mainloop()

            return self.sSelection

#===============================================================================

def main():

    oDialog=DialogProjectChoice(["workspace_1X2","workspace_1X2_ojs","workspace_2x2","workspace_2x2_Elastic","workspace_1X2_Perspective"])

    sPrefix = oDialog.Show()

    print("Projects:", oDialog.sProjectList)
    print("Projects Selected:", sPrefix)

    pass

if __name__ == '__main__':
    main()
