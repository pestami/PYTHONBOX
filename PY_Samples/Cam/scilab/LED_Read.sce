// read csv file
filename='C:\Users\sesa237770\Documents\GITBOX\PY_Samples\Cam\workspace_2x2\LED_Stack.log'
M1 = csvRead(filename,ascii(9), [], 'string')

Me=gsort(M1,'r')
