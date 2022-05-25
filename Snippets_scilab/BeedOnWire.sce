// auto scaling with previous plots + style
clf();
clc(); // clear console window
clear; // kills variables
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
function [yi] = MyDecay(xi)
a=10;
b=10;

    //y=(a*x) * (2.17^(-x))

    yi=(a*xi) .* (exp(-xi/b))
    
endfunction
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].

//xdata = linspace ( 0 , 10 , 5 );
xdata1 = [0,1,2,3,4,5,6,7,8,9,10];
res=1
xdata1=[0:res:100]; 
ydata1=[100:-res:0]; 

//ydata = MyQuadratic (xdata);
disp('=====MyDECAY===========')
ydata2 = MyDecay (xdata1);
ydata3=ydata1 -ydata2
//ydata = MyQuadratic (xdata);

//---------------------------------------------------
//print('file-name',x1,[x2,...xn])

//disp(xdata)
subplot(1,3,1) // 1 row 2 column
plot(xdata1,ydata1);
subplot(1,3,2)
plot(xdata1,ydata2);
subplot(1,3,3)
plot(xdata1,ydata3);
//plot(xdata,ydata2);
