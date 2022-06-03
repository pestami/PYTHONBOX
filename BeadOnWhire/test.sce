// auto scaling with previous plots + style
//clf();
//clc(); // clear console window
//clear; // kills variables
//xdel(0); // delete the first graphic
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
//---------------------------------------------------
function [yi] = MySin(xi)

     yi=100*sin(2*xi*3.1415/100) 
    
endfunction
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].

//xdata = linspace ( 0 , 10 , 5 );
//xdata1 = [0,1,2,3,4,5,6,7,8,9,10];
res=1
xdata1=[0:res:100]; 
ydata1=[100:-res:0]; 

//ydata = MyQuadratic (xdata);
disp('=====MyDECAY===========')

ydata3=MySin(xdata1)

//ydata = MyQuadratic (xdata);

//---------------------------------------------------
//print('file-name',x1,[x2,...xn])

//disp(xdata)
//subplot(1,3,1) // 1 row 2 column

plot(xdata1,ydata3,"y");

//subplot(1,3,2)
//plot(xdata1,ydata2);
//subplot(1,3,3)
//plot(xdata1,ydata3);
//plot(xdata,ydata2);
