// auto scaling with previous plots + style
//clf();
//clc(); // clear console window
//clear; // kills variables
//xdel(0); // delete the first graphic
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
// read csv file
filename='..\workspace_2x2\LED_Stack.log'

filename='..\workspace_2x2\LED_Stack.log'

M = csvRead(filename,ascii(9), [], 'string')

clc();
//----------------------------------------------------
//--testing sort--------------------------------------
//Ms=gsort(M,'r')
//----------------------------------------------------
//LED=M(:,[
M(:,1) = []  // remove column 1
% Specify you conditions
TF = M(:,1)=="0"   // "0" "1" ... LED NUMBER
//M=[M';TF1']' // transpose add row transpose back
MT=M'
TFT=TF'
D=[MT;TFT]
