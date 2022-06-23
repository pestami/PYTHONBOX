// auto scaling with previous plots + style
//clf();
clc(); // clear console window
clear; // kills variables
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
disp('=====VECTORS===========')

x=[1,1,0]
y=[0,0,1]

disp('=====VECTORS ADD===========')
disp(x)
disp(y)
s=x + y
disp('x + y =')
disp(s)

disp('=====VECTORS CROSS===========')
x=[1,0,0]
y=[0,1,0]
disp(x)
disp(y)
disp('x X y =')
disp(cross(x,y))
disp('=====Element wise Multiplication===========')
x=[2,4,1]
y=[3,5,2]
disp(x)
disp(y)
disp('x .* y =') //Element-wise multiplication is denoted x.*y
disp(x.*y)
