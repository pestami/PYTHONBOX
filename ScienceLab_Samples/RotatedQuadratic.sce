// auto scaling with previous plots + style
clf();
clc(); // clear console window
clear; // kills variables
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
function [y] = MyQuadratic(x)
a=1;
b=2;
c=4;
    y=a*x^2+b*x+c
endfunction

function [yi] = MyDecay(xi)
a=1;
b=2;
c=4;
    //y=(a*x) * (2.17^(-x))

    yi=(a*xi) .* (exp(-xi))
    
endfunction
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].

//xdata = linspace ( 0 , 10 , 5 );
xdata = [0,1,2,3,4,5,6,7,8,9,10];
xdata=[0:0.01:10]; 
//ydata = MyQuadratic (xdata);
disp('=====MyDECAY===========')
ydata = MyDecay (xdata);
//ydata = MyQuadratic (xdata);

//---------------------------------------------------
//print('file-name',x1,[x2,...xn])

disp(xdata)

plot(xdata,ydata);
