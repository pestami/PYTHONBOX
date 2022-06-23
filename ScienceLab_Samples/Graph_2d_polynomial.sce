// auto scaling with previous plots + style
clf();
x=[-100:1:100];
//----------------------------------------------------
function [y] = MyQuadratic(x)
a=1;
b=2;
c=4;
    y=a*x^2+b*x+c
endfunction
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].

xdata = linspace ( 1 , 10 , 5 );
ydata = MyQuadratic (xdata);
//---------------------------------------------------


plot(xdata,ydata);
