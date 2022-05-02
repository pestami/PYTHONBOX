// auto scaling with previous plots + style
clf();
x=[-100:1:100];

function [y] = fx(x)
a=1;
b=2;
c=4;
    y=a*x^2+b*x+c
endfunction


plot(x,fx(x),1);
